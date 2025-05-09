# Created by Ryan Polasky - 5/1/25

from fastapi import APIRouter, HTTPException, status
from typing import List, Optional
from pydantic import BaseModel
from database import execute_query, execute_query_single_row
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)
logger = logging.getLogger("prescriptions")


class PrescriptionCreate(BaseModel):
    patientid: int
    physicianid: int
    medication: str
    dosage: str


class PrescriptionResponse(BaseModel):
    prescriptionid: int
    patientid: int
    physicianid: int
    medication: str
    dosage: str


class PrescriptionWithDetails(PrescriptionResponse):
    patient_name: str
    physician_name: str


router = APIRouter(
    prefix="/prescriptions",
    tags=["prescriptions"],
)


@router.post("/", response_model=PrescriptionResponse, status_code=status.HTTP_201_CREATED)
def create_prescription(prescription: PrescriptionCreate):
    logger.info(f"POST /prescriptions - Payload: {prescription.dict()}")
    query = """
    INSERT INTO prescription (patientid, physicianid, medication, dosage) 
    VALUES (%s, %s, %s, %s) 
    RETURNING prescriptionid, patientid, physicianid, medication, dosage
    """
    params = (
        prescription.patientID,
        prescription.physicianID,
        prescription.medication,
        prescription.dosage
    )
    try:
        result = execute_query_single_row(query, params)
    except Exception as e:
        logger.error(f"DB error on create_prescription: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create prescription"
        )
    if not result:
        logger.error("Failed to create prescription: DB returned no result.")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create prescription"
        )
    logger.info(f"Prescription created: {result}")
    return result


@router.get("/", response_model=List[PrescriptionResponse])
def get_prescriptions(skip: int = 0, limit: int = 100):
    logger.info(f"GET /prescriptions - skip: {skip}, limit: {limit}")
    query = """
    SELECT prescriptionid, patientid, physicianid, medication, dosage
    FROM prescription
    ORDER BY prescriptionid
    LIMIT %s OFFSET %s
    """
    try:
        result = execute_query(query, (limit, skip))
    except Exception as e:
        logger.error(f"DB error on get_prescriptions: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch prescriptions"
        )
    logger.info(f"Fetched {len(result)} prescriptions")
    return result


@router.get("/with-details", response_model=List[PrescriptionWithDetails])
def get_prescriptions_with_details(skip: int = 0, limit: int = 100):
    logger.info(f"GET /prescriptions/with-details - skip: {skip}, limit: {limit}")
    query = """
    SELECT 
        p.prescriptionid, 
        p.patientid, 
        p.physicianid, 
        p.medication, 
        p.dosage,
        pt.name as patient_name,
        ph.name as physician_name
    FROM prescription p
    JOIN patient pt ON p.patientid = pt.patientid
    JOIN physician ph ON p.physicianid = ph.physicianid
    ORDER BY p.prescriptionid
    LIMIT %s OFFSET %s
    """
    try:
        result = execute_query(query, (limit, skip))
    except Exception as e:
        logger.error(f"DB error on get_prescriptions_with_details: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch prescriptions with details"
        )
    logger.info(f"Fetched {len(result)} prescriptions (with details)")
    return result


@router.get("/{prescription_id}", response_model=PrescriptionResponse)
def get_prescription(prescription_id: int):
    logger.info(f"GET /prescriptions/{prescription_id}")
    query = """
    SELECT prescriptionid, patientid, physicianid, medication, dosage
    FROM prescription 
    WHERE prescriptionid = %s
    """
    try:
        result = execute_query_single_row(query, (prescription_id,))
    except Exception as e:
        logger.error(f"DB error on get_prescription: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch prescription"
        )
    if not result:
        logger.warning(f"Prescription ID {prescription_id} not found")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Prescription with ID {prescription_id} not found"
        )
    return result


@router.get("/patient/{patient_id}", response_model=List[PrescriptionResponse])
def get_patient_prescriptions(patient_id: int):
    logger.info(f"GET /prescriptions/patient/{patient_id}")
    query = """
    SELECT prescriptionid, patientid, physicianid, medication, dosage
    FROM prescription 
    WHERE patientid = %s
    ORDER BY prescriptionid
    """
    try:
        result = execute_query(query, (patient_id,))
    except Exception as e:
        logger.error(f"DB error on get_patient_prescriptions: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch patient prescriptions"
        )
    logger.info(f"Fetched {len(result)} prescriptions for patient {patient_id}")
    return result


@router.get("/physician/{physician_id}", response_model=List[PrescriptionResponse])
def get_physician_prescriptions(physician_id: int):
    logger.info(f"GET /prescriptions/physician/{physician_id}")
    query = """
    SELECT prescriptionid, patientid, physicianid, medication, dosage
    FROM prescription 
    WHERE physicianid = %s
    ORDER BY prescriptionid
    """
    try:
        result = execute_query(query, (physician_id,))
    except Exception as e:
        logger.error(f"DB error on get_physician_prescriptions: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch physician prescriptions"
        )
    logger.info(f"Fetched {len(result)} prescriptions for physician {physician_id}")
    return result


@router.put("/{prescription_id}", response_model=PrescriptionResponse)
def update_prescription(prescription_id: int, prescription: PrescriptionCreate):
    logger.info(f"PUT /prescriptions/{prescription_id} - Payload: {prescription.dict()}")
    query = """
    UPDATE prescription 
    SET patientid = %s, physicianid = %s, medication = %s, dosage = %s 
    WHERE prescriptionid = %s 
    RETURNING prescriptionid, patientid, physicianid, medication, dosage
    """
    params = (
        prescription.patientID,
        prescription.physicianID,
        prescription.medication,
        prescription.dosage,
        prescription_id
    )
    try:
        result = execute_query_single_row(query, params)
    except Exception as e:
        logger.error(f"DB error on update_prescription: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to update prescription"
        )
    if not result:
        logger.warning(f"Prescription ID {prescription_id} not found for update")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Prescription with ID {prescription_id} not found"
        )
    logger.info(f"Prescription {prescription_id} updated.")
    return result


@router.delete("/{prescription_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_prescription(prescription_id: int):
    logger.info(f"DELETE /prescriptions/{prescription_id}")
    query = "DELETE FROM prescription WHERE prescriptionid = %s RETURNING prescriptionid"
    try:
        result = execute_query_single_row(query, (prescription_id,))
    except Exception as e:
        logger.error(f"DB error on delete_prescription: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to delete prescription"
        )
    if not result:
        logger.warning(f"Prescription ID {prescription_id} not found for delete")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Prescription with ID {prescription_id} not found"
        )
    logger.info(f"Prescription {prescription_id} deleted.")
