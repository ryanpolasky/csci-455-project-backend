# Created by Ryan Polasky - 5/1/25

from fastapi import APIRouter, HTTPException, status
from datetime import date
from typing import List, Optional
from pydantic import BaseModel
from database import execute_query, execute_query_single_row
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)
logger = logging.getLogger("billing")


class BillingCreate(BaseModel):
    patientID: int
    amountDue: float
    dateIssued: Optional[date] = None


class BillingResponse(BaseModel):
    billID: int
    patientID: int
    amountDue: float
    dateIssued: date


class BillingWithPatient(BillingResponse):
    patient_name: str


router = APIRouter(
    prefix="/billing",
    tags=["billing"],
)


@router.post("/", response_model=BillingResponse, status_code=status.HTTP_201_CREATED)
def create_billing(billing: BillingCreate):
    logger.info(f"POST /billing - Payload: {billing.dict()}")
    if billing.dateIssued:
        query = """
        INSERT INTO billing (patientID, amountDue, dateIssued) 
        VALUES (%s, %s, %s) 
        RETURNING billID, patientID, amountDue, dateIssued
        """
        params = (billing.patientID, billing.amountDue, billing.dateIssued)
    else:
        query = """
        INSERT INTO billing (patientID, amountDue) 
        VALUES (%s, %s) 
        RETURNING billID, patientID, amountDue, dateIssued
        """
        params = (billing.patientID, billing.amountDue)
    try:
        result = execute_query_single_row(query, params)
    except Exception as e:
        logger.error(f"DB error on create_billing: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create billing"
        )
    if not result:
        logger.error("Failed to create billing: DB returned no result.")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create billing"
        )
    logger.info(f"Billing created: {result}")
    return result


@router.get("/", response_model=List[BillingResponse])
def get_billings(skip: int = 0, limit: int = 100):
    logger.info(f"GET /billing - skip: {skip}, limit: {limit}")
    query = """
    SELECT billID, patientID, amountDue, dateIssued 
    FROM billing 
    ORDER BY dateIssued DESC, billID 
    LIMIT %s OFFSET %s
    """
    try:
        result = execute_query(query, (limit, skip))
    except Exception as e:
        logger.error(f"DB error on get_billings: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch billings"
        )
    logger.info(f"Fetched {len(result)} billing rows")
    return result


@router.get("/with-patient", response_model=List[BillingWithPatient])
def get_billings_with_patient(skip: int = 0, limit: int = 100):
    logger.info(f"GET /billing/with-patient - skip: {skip}, limit: {limit}")
    query = """
    SELECT 
        b.billID, 
        b.patientID, 
        b.amountDue, 
        b.dateIssued,
        p.name as patient_name
    FROM billing b
    JOIN patients p ON b.patientID = p.patientID
    ORDER BY b.dateIssued DESC, b.billID
    LIMIT %s OFFSET %s
    """
    try:
        result = execute_query(query, (limit, skip))
    except Exception as e:
        logger.error(f"DB error on get_billings_with_patient: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch billings with patient"
        )
    logger.info(f"Fetched {len(result)} billing rows (with patient)")
    return result


@router.get("/{bill_id}", response_model=BillingResponse)
def get_billing(bill_id: int):
    logger.info(f"GET /billing/{bill_id}")
    query = """
    SELECT billID, patientID, amountDue, dateIssued 
    FROM billing 
    WHERE billID = %s
    """
    try:
        result = execute_query_single_row(query, (bill_id,))
    except Exception as e:
        logger.error(f"DB error on get_billing: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch billing"
        )
    if not result:
        logger.warning(f"Billing ID {bill_id} not found")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Billing with ID {bill_id} not found"
        )
    return result


@router.get("/patient/{patient_id}", response_model=List[BillingResponse])
def get_patient_billings(patient_id: int):
    logger.info(f"GET /billing/patient/{patient_id}")
    query = """
    SELECT billID, patientID, amountDue, dateIssued 
    FROM billing 
    WHERE patientID = %s
    ORDER BY dateIssued DESC
    """
    try:
        result = execute_query(query, (patient_id,))
    except Exception as e:
        logger.error(f"DB error on get_patient_billings: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch patient billing"
        )
    logger.info(f"Fetched {len(result)} billings for patient {patient_id}")
    return result


@router.get("/patient/{patient_id}/total", response_model=float)
def calculate_patient_total_billing(patient_id: int):
    logger.info(f"GET /billing/patient/{patient_id}/total")
    query = """
    SELECT SUM(amountDue) as total
    FROM billing 
    WHERE patientID = %s
    """
    try:
        result = execute_query_single_row(query, (patient_id,))
    except Exception as e:
        logger.error(f"DB error on calculate_patient_total_billing: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to calculate patient total billing"
        )
    if not result or result['total'] is None:
        logger.info("No patient total, returning 0.0")
        return 0.0
    logger.info(f"Patient {patient_id} total billing: {result['total']}")
    return float(result['total'])


@router.put("/{bill_id}", response_model=BillingResponse)
def update_billing(bill_id: int, billing: BillingCreate):
    logger.info(f"PUT /billing/{bill_id} - Payload: {billing.dict()}")
    query = """
    UPDATE billing 
    SET patientID = %s, amountDue = %s, dateIssued = %s 
    WHERE billID = %s 
    RETURNING billID, patientID, amountDue, dateIssued
    """
    date_issued = billing.dateIssued if billing.dateIssued else date.today()
    params = (billing.patientID, billing.amountDue, date_issued, bill_id)
    try:
        result = execute_query_single_row(query, params)
    except Exception as e:
        logger.error(f"DB error on update_billing: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to update billing"
        )
    if not result:
        logger.warning(f"Billing ID {bill_id} not found for update")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Billing with ID {bill_id} not found"
        )
    logger.info(f"Billing {bill_id} updated.")
    return result


@router.delete("/{bill_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_billing(bill_id: int):
    logger.info(f"DELETE /billing/{bill_id}")
    query = "DELETE FROM billing WHERE billID = %s RETURNING billID"
    try:
        result = execute_query_single_row(query, (bill_id,))
    except Exception as e:
        logger.error(f"DB error on delete_billing: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to delete billing"
        )
    if not result:
        logger.warning(f"Billing ID {bill_id} not found for delete")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Billing with ID {bill_id} not found"
        )
    logger.info(f"Billing {bill_id} deleted.")
