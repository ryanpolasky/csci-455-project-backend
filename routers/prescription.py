# Created by Ryan Polasky - 5/1/25

from fastapi import APIRouter, HTTPException, status
from typing import List, Optional
from pydantic import BaseModel
from database import execute_query, execute_query_single_row


class PrescriptionCreate(BaseModel):
    patientID: int
    physicianID: int
    medication: str
    dosage: str


class PrescriptionResponse(BaseModel):
    prescriptionID: int
    patientID: int
    physicianID: int
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
    query = """
    INSERT INTO prescriptions (patientID, physicianID, medication, dosage) 
    VALUES (%s, %s, %s, %s) 
    RETURNING prescriptionID, patientID, physicianID, medication, dosage
    """
    params = (
        prescription.patientID,
        prescription.physicianID,
        prescription.medication,
        prescription.dosage
    )
    result = execute_query_single_row(query, params)

    if not result:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create prescription"
        )

    return result


@router.get("/", response_model=List[PrescriptionResponse])
def get_prescriptions(skip: int = 0, limit: int = 100):
    query = """
    SELECT prescriptionID, patientID, physicianID, medication, dosage
    FROM prescriptions 
    ORDER BY prescriptionID 
    LIMIT %s OFFSET %s
    """
    result = execute_query(query, (limit, skip))
    return result


@router.get("/with-details", response_model=List[PrescriptionWithDetails])
def get_prescriptions_with_details(skip: int = 0, limit: int = 100):
    query = """
    SELECT 
        p.prescriptionID, 
        p.patientID, 
        p.physicianID, 
        p.medication, 
        p.dosage,
        pt.name as patient_name,
        ph.name as physician_name
    FROM prescriptions p
    JOIN patients pt ON p.patientID = pt.patientID
    JOIN physicians ph ON p.physicianID = ph.physicianID
    ORDER BY p.prescriptionID
    LIMIT %s OFFSET %s
    """
    result = execute_query(query, (limit, skip))
    return result


@router.get("/{prescription_id}", response_model=PrescriptionResponse)
def get_prescription(prescription_id: int):
    query = """
    SELECT prescriptionID, patientID, physicianID, medication, dosage
    FROM prescriptions 
    WHERE prescriptionID = %s
    """
    result = execute_query_single_row(query, (prescription_id,))

    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Prescription with ID {prescription_id} not found"
        )

    return result


@router.get("/patient/{patient_id}", response_model=List[PrescriptionResponse])
def get_patient_prescriptions(patient_id: int):
    query = """
    SELECT prescriptionID, patientID, physicianID, medication, dosage
    FROM prescriptions 
    WHERE patientID = %s
    ORDER BY prescriptionID
    """
    result = execute_query(query, (patient_id,))
    return result


@router.get("/physician/{physician_id}", response_model=List[PrescriptionResponse])
def get_physician_prescriptions(physician_id: int):
    query = """
    SELECT prescriptionID, patientID, physicianID, medication, dosage
    FROM prescriptions 
    WHERE physicianID = %s
    ORDER BY prescriptionID
    """
    result = execute_query(query, (physician_id,))
    return result


@router.put("/{prescription_id}", response_model=PrescriptionResponse)
def update_prescription(prescription_id: int, prescription: PrescriptionCreate):
    query = """
    UPDATE prescriptions 
    SET patientID = %s, physicianID = %s, medication = %s, dosage = %s 
    WHERE prescriptionID = %s 
    RETURNING prescriptionID, patientID, physicianID, medication, dosage
    """
    params = (
        prescription.patientID,
        prescription.physicianID,
        prescription.medication,
        prescription.dosage,
        prescription_id
    )
    result = execute_query_single_row(query, params)

    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Prescription with ID {prescription_id} not found"
        )

    return result


@router.delete("/{prescription_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_prescription(prescription_id: int):
    query = "DELETE FROM prescriptions WHERE prescriptionID = %s RETURNING prescriptionID"
    result = execute_query_single_row(query, (prescription_id,))

    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Prescription with ID {prescription_id} not found"
        )
