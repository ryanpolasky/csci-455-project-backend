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
logger = logging.getLogger("patients")


class PatientCreate(BaseModel):
    name: str
    dob: date
    address: str
    phone: str
    insurance: str


class PatientResponse(BaseModel):
    patientID: int
    name: str
    dob: date
    address: str
    phone: str
    insurance: str


router = APIRouter(
    prefix="/patients",
    tags=["patients"],
)


@router.post("/", response_model=PatientResponse, status_code=status.HTTP_201_CREATED)
def create_patient(patient: PatientCreate):
    logger.info(f"POST /patients - Payload: {patient.dict()}")
    query = """
    INSERT INTO patient (name, dob, address, phone, insurance) 
    VALUES (%s, %s, %s, %s, %s) 
    RETURNING patientID, name, dob, address, phone, insurance
    """
    params = (patient.name, patient.dob, patient.address, patient.phone, patient.insurance)
    try:
        result = execute_query_single_row(query, params)
    except Exception as e:
        logger.error(f"DB error on create_patient: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create patient"
        )
    if not result:
        logger.error("Failed to create patient: DB returned no result.")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create patient"
        )
    logger.info(f"Patient created: {result}")
    return result


@router.get("/", response_model=List[PatientResponse])
def get_patients(skip: int = 0, limit: int = 100):
    logger.info(f"GET /patients - skip: {skip}, limit: {limit}")
    query = """
    SELECT patientID, name, dob, address, phone, insurance 
    FROM patient 
    ORDER BY patientID 
    LIMIT %s OFFSET %s
    """
    try:
        result = execute_query(query, (limit, skip))
    except Exception as e:
        logger.error(f"DB error on get_patients: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch patients"
        )
    logger.info(f"Fetched {len(result)} patients")
    return result


@router.get("/{patient_id}", response_model=PatientResponse)
def get_patient(patient_id: int):
    logger.info(f"GET /patients/{patient_id}")
    query = """
    SELECT patientID, name, dob, address, phone, insurance 
    FROM patient 
    WHERE patientID = %s
    """
    try:
        result = execute_query_single_row(query, (patient_id,))
    except Exception as e:
        logger.error(f"DB error on get_patient: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch patient"
        )
    if not result:
        logger.warning(f"Patient ID {patient_id} not found")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Patient with ID {patient_id} not found"
        )
    return result


@router.put("/{patient_id}", response_model=PatientResponse)
def update_patient(patient_id: int, patient: PatientCreate):
    logger.info(f"PUT /patients/{patient_id} - Payload: {patient.dict()}")
    query = """
    UPDATE patient 
    SET name = %s, dob = %s, address = %s, phone = %s, insurance = %s 
    WHERE patientID = %s 
    RETURNING patientID, name, dob, address, phone, insurance
    """
    params = (patient.name, patient.dob, patient.address, patient.phone, patient.insurance, patient_id)
    try:
        result = execute_query_single_row(query, params)
    except Exception as e:
        logger.error(f"DB error on update_patient: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to update patient"
        )
    if not result:
        logger.warning(f"Patient ID {patient_id} not found for update")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Patient with ID {patient_id} not found"
        )
    logger.info(f"Patient {patient_id} updated.")
    return result


@router.delete("/{patient_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_patient(patient_id: int):
    logger.info(f"DELETE /patients/{patient_id}")
    query = "DELETE FROM patient WHERE patientID = %s RETURNING patientID"
    try:
        result = execute_query_single_row(query, (patient_id,))
    except Exception as e:
        logger.error(f"DB error on delete_patient: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to delete patient"
        )
    if not result:
        logger.warning(f"Patient ID {patient_id} not found for delete")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Patient with ID {patient_id} not found"
        )
    logger.info(f"Patient {patient_id} deleted.")
