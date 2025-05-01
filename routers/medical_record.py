# Created by Ryan Polasky - 5/1/25

from fastapi import APIRouter, HTTPException, status
from datetime import date
from typing import List, Optional
from pydantic import BaseModel
from database import execute_query, execute_query_single_row


class MedicalRecordCreate(BaseModel):
    patientID: int
    allergies: Optional[str] = None
    medications: Optional[str] = None
    diagnoses: Optional[str] = None


class MedicalRecordResponse(BaseModel):
    recordID: int
    patientID: int
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
    query = """
    INSERT INTO medical_records (patientID, allergies, medications, diagnoses) 
    VALUES (%s, %s, %s, %s) 
    RETURNING recordID, patientID, dateCreated, allergies, medications, diagnoses
    """
    params = (record.patientID, record.allergies, record.medications, record.diagnoses)
    result = execute_query_single_row(query, params)

    if not result:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create medical record"
        )

    return result


@router.get("/", response_model=List[MedicalRecordResponse])
def get_medical_records(skip: int = 0, limit: int = 100):
    query = """
    SELECT recordID, patientID, dateCreated, allergies, medications, diagnoses 
    FROM medical_records 
    ORDER BY dateCreated DESC 
    LIMIT %s OFFSET %s
    """
    result = execute_query(query, (limit, skip))
    return result


@router.get("/with-patient-info", response_model=List[MedicalRecordWithPatient])
def get_medical_records_with_patient_info(skip: int = 0, limit: int = 100):
    query = """
    SELECT mr.recordID, mr.patientID, mr.dateCreated, mr.allergies, 
           mr.medications, mr.diagnoses, p.name as patient_name
    FROM medical_records mr
    JOIN patients p ON mr.patientID = p.patientID
    ORDER BY mr.dateCreated DESC
    LIMIT %s OFFSET %s
    """
    result = execute_query(query, (limit, skip))
    return result


@router.get("/{record_id}", response_model=MedicalRecordResponse)
def get_medical_record(record_id: int):
    query = """
    SELECT recordID, patientID, dateCreated, allergies, medications, diagnoses 
    FROM medical_records 
    WHERE recordID = %s
    """
    result = execute_query_single_row(query, (record_id,))

    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Medical record with ID {record_id} not found"
        )

    return result


@router.get("/patient/{patient_id}", response_model=List[MedicalRecordResponse])
def get_patient_medical_records(patient_id: int):
    query = """
    SELECT recordID, patientID, dateCreated, allergies, medications, diagnoses 
    FROM medical_records 
    WHERE patientID = %s 
    ORDER BY dateCreated DESC
    """
    result = execute_query(query, (patient_id,))
    return result


@router.put("/{record_id}", response_model=MedicalRecordResponse)
def update_medical_record(record_id: int, record: MedicalRecordCreate):
    query = """
    UPDATE medical_records 
    SET patientID = %s, allergies = %s, medications = %s, diagnoses = %s 
    WHERE recordID = %s 
    RETURNING recordID, patientID, dateCreated, allergies, medications, diagnoses
    """
    params = (record.patientID, record.allergies, record.medications, record.diagnoses, record_id)
    result = execute_query_single_row(query, params)

    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Medical record with ID {record_id} not found"
        )

    return result


@router.patch("/{record_id}/add-diagnosis", response_model=MedicalRecordResponse)
def add_diagnosis(record_id: int, diagnosis: str):
    # First get current diagnoses
    get_query = """
    SELECT diagnoses FROM medical_records WHERE recordID = %s
    """
    current = execute_query_single_row(get_query, (record_id,))

    if not current:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Medical record with ID {record_id} not found"
        )

    # Update with new diagnosis
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
    result = execute_query_single_row(update_query, (new_diagnoses, record_id))

    return result
