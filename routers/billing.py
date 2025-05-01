# Created by Ryan Polasky - 5/1/25

from fastapi import APIRouter, HTTPException, status
from datetime import date
from typing import List, Optional
from pydantic import BaseModel
from database import execute_query, execute_query_single_row


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

    result = execute_query_single_row(query, params)

    if not result:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create billing"
        )

    return result


@router.get("/", response_model=List[BillingResponse])
def get_billings(skip: int = 0, limit: int = 100):
    query = """
    SELECT billID, patientID, amountDue, dateIssued 
    FROM billing 
    ORDER BY dateIssued DESC, billID 
    LIMIT %s OFFSET %s
    """
    result = execute_query(query, (limit, skip))
    return result


@router.get("/with-patient", response_model=List[BillingWithPatient])
def get_billings_with_patient(skip: int = 0, limit: int = 100):
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
    result = execute_query(query, (limit, skip))
    return result


@router.get("/{bill_id}", response_model=BillingResponse)
def get_billing(bill_id: int):
    query = """
    SELECT billID, patientID, amountDue, dateIssued 
    FROM billing 
    WHERE billID = %s
    """
    result = execute_query_single_row(query, (bill_id,))

    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Billing with ID {bill_id} not found"
        )

    return result


@router.get("/patient/{patient_id}", response_model=List[BillingResponse])
def get_patient_billings(patient_id: int):
    query = """
    SELECT billID, patientID, amountDue, dateIssued 
    FROM billing 
    WHERE patientID = %s
    ORDER BY dateIssued DESC
    """
    result = execute_query(query, (patient_id,))
    return result


@router.get("/patient/{patient_id}/total", response_model=float)
def calculate_patient_total_billing(patient_id: int):
    query = """
    SELECT SUM(amountDue) as total
    FROM billing 
    WHERE patientID = %s
    """
    result = execute_query_single_row(query, (patient_id,))

    if not result or result['total'] is None:
        return 0.0

    return float(result['total'])


@router.put("/{bill_id}", response_model=BillingResponse)
def update_billing(bill_id: int, billing: BillingCreate):
    query = """
    UPDATE billing 
    SET patientID = %s, amountDue = %s, dateIssued = %s 
    WHERE billID = %s 
    RETURNING billID, patientID, amountDue, dateIssued
    """
    date_issued = billing.dateIssued if billing.dateIssued else date.today()
    params = (billing.patientID, billing.amountDue, date_issued, bill_id)
    result = execute_query_single_row(query, params)

    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Billing with ID {bill_id} not found"
        )

    return result


@router.delete("/{bill_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_billing(bill_id: int):
    query = "DELETE FROM billing WHERE billID = %s RETURNING billID"
    result = execute_query_single_row(query, (bill_id,))

    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Billing with ID {bill_id} not found"
        )
