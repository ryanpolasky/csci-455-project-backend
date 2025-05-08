# Created by Ryan Polasky - 5/1/25

from fastapi import APIRouter, HTTPException, status
from datetime import date
from typing import List, Optional
from pydantic import BaseModel
from database import execute_query, execute_query_single_row


# Pydantic models for request/response
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
    query = """
    INSERT INTO patient (name, dob, address, phone, insurance) 
    VALUES (%s, %s, %s, %s, %s) 
    RETURNING patientID, name, dob, address, phone, insurance
    """
    params = (patient.name, patient.dob, patient.address, patient.phone, patient.insurance)
    result = execute_query_single_row(query, params)

    if not result:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create patient"
        )

    return result


@router.get("/", response_model=List[PatientResponse])
def get_patients(skip: int = 0, limit: int = 100):
    query = """
    SELECT patientID, name, dob, address, phone, insurance 
    FROM patient 
    ORDER BY patientID 
    LIMIT %s OFFSET %s
    """
    result = execute_query(query, (limit, skip))
    return result


@router.get("/{patient_id}", response_model=PatientResponse)
def get_patient(patient_id: int):
    query = """
    SELECT patientID, name, dob, address, phone, insurance 
    FROM patient 
    WHERE patientID = %s
    """
    result = execute_query_single_row(query, (patient_id,))

    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Patient with ID {patient_id} not found"
        )

    return result


@router.put("/{patient_id}", response_model=PatientResponse)
def update_patient(patient_id: int, patient: PatientCreate):
    query = """
    UPDATE patient 
    SET name = %s, dob = %s, address = %s, phone = %s, insurance = %s 
    WHERE patientID = %s 
    RETURNING patientID, name, dob, address, phone, insurance
    """
    params = (patient.name, patient.dob, patient.address, patient.phone, patient.insurance, patient_id)
    result = execute_query_single_row(query, params)

    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Patient with ID {patient_id} not found"
        )

    return result


@router.delete("/{patient_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_patient(patient_id: int):
    query = "DELETE FROM patient WHERE patientID = %s RETURNING patientID"
    result = execute_query_single_row(query, (patient_id,))

    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Patient with ID {patient_id} not found"
        )
