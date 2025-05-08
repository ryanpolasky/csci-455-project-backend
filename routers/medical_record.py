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
logger = logging.getLogger("medical_records")


class MedicalRecordCreate(BaseModel):
    patientid: int
    allergies: Optional[str] = None
    medications: Optional[str] = None
    diagnoses: Optional[str] = None


class MedicalRecordResponse(BaseModel):
    recordid: int
    patientid: int
    dateCreated: date
    allergies: Optional[str] = None
    medications: Optional[str] = None
    diagnoses: Optional[str] = None


class MedicalRecordWithPatient(MedicalRecordResponse):
    patient_name: str


router = APIRouter(
    prefix="/medical-records",
    tags=["medical_records"],
)


@router.post("/", response_model=MedicalRecordResponse, status_code=status.HTTP_201_CREATED)
def create_medical_record(record: MedicalRecordCreate):
    logger.info(f"POST /medical-records - Payload: {record.dict()}")
    query = """
    INSERT INTO medical_records (patientID, allergies, medications, diagnoses) 
    VALUES (%s, %s, %s, %s) 
    RETURNING recordID, patientID, dateCreated, allergies, medications, diagnoses
    """
    params = (record.patientID, record.allergies, record.medications, record.diagnoses)
    try:
        result = execute_query_single_row(query, params)
    except Exception as e:
        logger.error(f"DB error on create_medical_record: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create medical record"
        )
    if not result:
        logger.error("Failed to create medical record: DB returned no result.")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create medical record"
        )
    logger.info(f"Medical record created: {result}")
    return result


@router.get("/", response_model=List[MedicalRecordResponse])
def get_medical_records(skip: int = 0, limit: int = 100):
    logger.info(f"GET /medical-records - skip: {skip}, limit: {limit}")
    query = """
    SELECT recordID, patientID, dateCreated, allergies, medications, diagnoses 
    FROM medical_records 
    ORDER BY dateCreated DESC 
    LIMIT %s OFFSET %s
    """
    try:
        result = execute_query(query, (limit, skip))
    except Exception as e:
        logger.error(f"DB error on get_medical_records: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch medical records"
        )
    logger.info(f"Fetched {len(result)} medical records")
    return result


@router.get("/with-patient-info", response_model=List[MedicalRecordWithPatient])
def get_medical_records_with_patient_info(skip: int = 0, limit: int = 100):
    logger.info(f"GET /medical-records/with-patient-info - skip: {skip}, limit: {limit}")
    query = """
    SELECT mr.recordID, mr.patientID, mr.dateCreated, mr.allergies, 
           mr.medications, mr.diagnoses, p.name as patient_name
    FROM medical_records mr
    JOIN patients p ON mr.patientID = p.patientID
    ORDER BY mr.dateCreated DESC
    LIMIT %s OFFSET %s
    """
    try:
        result = execute_query(query, (limit, skip))
    except Exception as e:
        logger.error(f"DB error on get_medical_records_with_patient_info: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch medical records with patient info"
        )
    logger.info(f"Fetched {len(result)} medical records (with patient info)")
    return result


@router.get("/{record_id}", response_model=MedicalRecordResponse)
def get_medical_record(record_id: int):
    logger.info(f"GET /medical-records/{record_id}")
    query = """
    SELECT recordID, patientID, dateCreated, allergies, medications, diagnoses 
    FROM medical_records 
    WHERE recordID = %s
    """
    try:
        result = execute_query_single_row(query, (record_id,))
    except Exception as e:
        logger.error(f"DB error on get_medical_record: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch medical record"
        )
    if not result:
        logger.warning(f"Medical record ID {record_id} not found")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Medical record with ID {record_id} not found"
        )
    return result


@router.get("/patient/{patient_id}", response_model=List[MedicalRecordResponse])
def get_patient_medical_records(patient_id: int):
    logger.info(f"GET /medical-records/patient/{patient_id}")
    query = """
    SELECT recordID, patientID, dateCreated, allergies, medications, diagnoses 
    FROM medical_records 
    WHERE patientID = %s 
    ORDER BY dateCreated DESC
    """
    try:
        result = execute_query(query, (patient_id,))
    except Exception as e:
        logger.error(f"DB error on get_patient_medical_records: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch patient medical records"
        )
    logger.info(f"Fetched {len(result)} medical records for patient {patient_id}")
    return result


@router.put("/{record_id}", response_model=MedicalRecordResponse)
def update_medical_record(record_id: int, record: MedicalRecordCreate):
    logger.info(f"PUT /medical-records/{record_id} - Payload: {record.dict()}")
    query = """
    UPDATE medical_records 
    SET patientID = %s, allergies = %s, medications = %s, diagnoses = %s 
    WHERE recordID = %s 
    RETURNING recordID, patientID, dateCreated, allergies, medications, diagnoses
    """
    params = (record.patientID, record.allergies, record.medications, record.diagnoses, record_id)
    try:
        result = execute_query_single_row(query, params)
    except Exception as e:
        logger.error(f"DB error on update_medical_record: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to update medical record"
        )
    if not result:
        logger.warning(f"Medical record ID {record_id} not found for update")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Medical record with ID {record_id} not found"
        )
    logger.info(f"Medical record {record_id} updated.")
    return result


@router.patch("/{record_id}/add-diagnosis", response_model=MedicalRecordResponse)
def add_diagnosis(record_id: int, diagnosis: str):
    logger.info(f"PATCH /medical-records/{record_id}/add-diagnosis - diagnosis: {diagnosis}")
    get_query = """
    SELECT diagnoses FROM medical_records WHERE recordID = %s
    """
    try:
        current = execute_query_single_row(get_query, (record_id,))
    except Exception as e:
        logger.error(f"DB error on add_diagnosis (SELECT): {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to get current diagnoses"
        )
    if not current:
        logger.warning(f"Medical record ID {record_id} not found when adding diagnosis")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Medical record with ID {record_id} not found"
        )
    new_diagnoses = current['diagnoses'] or ''
    if new_diagnoses:
        new_diagnoses += "; " + diagnosis
    else:
        new_diagnoses = diagnosis
    update_query = """
    UPDATE medical_records 
    SET diagnoses = %s 
    WHERE recordID = %s 
    RETURNING recordID, patientID, dateCreated, allergies, medications, diagnoses
    """
    try:
        result = execute_query_single_row(update_query, (new_diagnoses, record_id))
    except Exception as e:
        logger.error(f"DB error on add_diagnosis (UPDATE): {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to update diagnoses"
        )
    logger.info(f"Added diagnosis to record {record_id}")
    return result
