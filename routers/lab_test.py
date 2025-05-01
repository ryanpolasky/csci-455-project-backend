# Created by Ryan Polasky - 5/1/25

from fastapi import APIRouter, HTTPException, status
from typing import List, Optional
from pydantic import BaseModel
from database import execute_query, execute_query_single_row


class LabTestCreate(BaseModel):
    patientID: int
    testType: str
    results: Optional[str] = None


class LabTestResponse(BaseModel):
    testID: int
    patientID: int
    testType: str
    results: Optional[str] = None


class LabTestWithPatient(LabTestResponse):
    patient_name: str


router = APIRouter(
    prefix="/lab-tests",
    tags=["lab_tests"],
)


@router.post("/", response_model=LabTestResponse, status_code=status.HTTP_201_CREATED)
def create_lab_test(lab_test: LabTestCreate):
    query = """
    INSERT INTO lab_tests (patientID, testType, results) 
    VALUES (%s, %s, %s) 
    RETURNING testID, patientID, testType, results
    """
    params = (lab_test.patientID, lab_test.testType, lab_test.results)
    result = execute_query_single_row(query, params)

    if not result:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create lab test"
        )

    return result


@router.get("/", response_model=List[LabTestResponse])
def get_lab_tests(skip: int = 0, limit: int = 100):
    query = """
    SELECT testID, patientID, testType, results 
    FROM lab_tests 
    ORDER BY testID 
    LIMIT %s OFFSET %s
    """
    result = execute_query(query, (limit, skip))
    return result


@router.get("/with-patient", response_model=List[LabTestWithPatient])
def get_lab_tests_with_patient(skip: int = 0, limit: int = 100):
    query = """
    SELECT 
        lt.testID, 
        lt.patientID, 
        lt.testType, 
        lt.results,
        p.name as patient_name
    FROM lab_tests lt
    JOIN patients p ON lt.patientID = p.patientID
    ORDER BY lt.testID
    LIMIT %s OFFSET %s
    """
    result = execute_query(query, (limit, skip))
    return result


@router.get("/{test_id}", response_model=LabTestResponse)
def get_lab_test(test_id: int):
    query = """
    SELECT testID, patientID, testType, results 
    FROM lab_tests 
    WHERE testID = %s
    """
    result = execute_query_single_row(query, (test_id,))

    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Lab test with ID {test_id} not found"
        )

    return result


@router.get("/patient/{patient_id}", response_model=List[LabTestResponse])
def get_patient_lab_tests(patient_id: int):
    query = """
    SELECT testID, patientID, testType, results 
    FROM lab_tests 
    WHERE patientID = %s
    ORDER BY testID
    """
    result = execute_query(query, (patient_id,))
    return result


@router.put("/{test_id}", response_model=LabTestResponse)
def update_lab_test(test_id: int, lab_test: LabTestCreate):
    query = """
    UPDATE lab_tests 
    SET patientID = %s, testType = %s, results = %s 
    WHERE testID = %s 
    RETURNING testID, patientID, testType, results
    """
    params = (lab_test.patientID, lab_test.testType, lab_test.results, test_id)
    result = execute_query_single_row(query, params)

    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Lab test with ID {test_id} not found"
        )

    return result


@router.patch("/{test_id}/update-results", response_model=LabTestResponse)
def update_lab_test_results(test_id: int, results: str):
    query = """
    UPDATE lab_tests 
    SET results = %s 
    WHERE testID = %s 
    RETURNING testID, patientID, testType, results
    """
    result = execute_query_single_row(query, (results, test_id))

    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Lab test with ID {test_id} not found"
        )

    return result


@router.delete("/{test_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_lab_test(test_id: int):
    query = "DELETE FROM lab_tests WHERE testID = %s RETURNING testID"
    result = execute_query_single_row(query, (test_id,))

    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Lab test with ID {test_id} not found"
        )
