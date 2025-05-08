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
logger = logging.getLogger("lab_tests")


class LabTestCreate(BaseModel):
    patientid: int
    testType: str
    results: Optional[str] = None


class LabTestResponse(BaseModel):
    testid: int
    patientid: int
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
    logger.info(f"POST /lab-tests - Payload: {lab_test.dict()}")
    query = """
    INSERT INTO lab_tests (patientID, testType, results) 
    VALUES (%s, %s, %s) 
    RETURNING testID, patientID, testType, results
    """
    params = (lab_test.patientID, lab_test.testType, lab_test.results)
    try:
        result = execute_query_single_row(query, params)
    except Exception as e:
        logger.error(f"DB error on create_lab_test: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create lab test"
        )
    if not result:
        logger.error("Failed to create lab test: DB returned no result.")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create lab test"
        )
    logger.info(f"Lab test created: {result}")
    return result


@router.get("/", response_model=List[LabTestResponse])
def get_lab_tests(skip: int = 0, limit: int = 100):
    logger.info(f"GET /lab-tests - skip: {skip}, limit: {limit}")
    query = """
    SELECT testID, patientID, testType, results 
    FROM lab_tests 
    ORDER BY testID 
    LIMIT %s OFFSET %s
    """
    try:
        result = execute_query(query, (limit, skip))
    except Exception as e:
        logger.error(f"DB error on get_lab_tests: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch lab tests"
        )
    logger.info(f"Fetched {len(result)} lab tests")
    return result


@router.get("/with-patient", response_model=List[LabTestWithPatient])
def get_lab_tests_with_patient(skip: int = 0, limit: int = 100):
    logger.info(f"GET /lab-tests/with-patient - skip: {skip}, limit: {limit}")
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
    try:
        result = execute_query(query, (limit, skip))
    except Exception as e:
        logger.error(f"DB error on get_lab_tests_with_patient: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch lab tests with patient"
        )
    logger.info(f"Fetched {len(result)} lab tests (with patient)")
    return result


@router.get("/{test_id}", response_model=LabTestResponse)
def get_lab_test(test_id: int):
    logger.info(f"GET /lab-tests/{test_id}")
    query = """
    SELECT testID, patientID, testType, results 
    FROM lab_tests 
    WHERE testID = %s
    """
    try:
        result = execute_query_single_row(query, (test_id,))
    except Exception as e:
        logger.error(f"DB error on get_lab_test: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch lab test"
        )
    if not result:
        logger.warning(f"Lab test ID {test_id} not found")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Lab test with ID {test_id} not found"
        )
    return result


@router.get("/patient/{patient_id}", response_model=List[LabTestResponse])
def get_patient_lab_tests(patient_id: int):
    logger.info(f"GET /lab-tests/patient/{patient_id}")
    query = """
    SELECT testID, patientID, testType, results 
    FROM lab_tests 
    WHERE patientID = %s
    ORDER BY testID
    """
    try:
        result = execute_query(query, (patient_id,))
    except Exception as e:
        logger.error(f"DB error on get_patient_lab_tests: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch patient's lab tests"
        )
    logger.info(f"Fetched {len(result)} lab tests for patient {patient_id}")
    return result


@router.put("/{test_id}", response_model=LabTestResponse)
def update_lab_test(test_id: int, lab_test: LabTestCreate):
    logger.info(f"PUT /lab-tests/{test_id} - Payload: {lab_test.dict()}")
    query = """
    UPDATE lab_tests 
    SET patientID = %s, testType = %s, results = %s 
    WHERE testID = %s 
    RETURNING testID, patientID, testType, results
    """
    params = (lab_test.patientID, lab_test.testType, lab_test.results, test_id)
    try:
        result = execute_query_single_row(query, params)
    except Exception as e:
        logger.error(f"DB error on update_lab_test: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to update lab test"
        )
    if not result:
        logger.warning(f"Lab test ID {test_id} not found for update")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Lab test with ID {test_id} not found"
        )
    logger.info(f"Lab test {test_id} updated.")
    return result


@router.patch("/{test_id}/update-results", response_model=LabTestResponse)
def update_lab_test_results(test_id: int, results: str):
    logger.info(f"PATCH /lab-tests/{test_id}/update-results - results: {results}")
    query = """
    UPDATE lab_tests 
    SET results = %s 
    WHERE testID = %s 
    RETURNING testID, patientID, testType, results
    """
    try:
        result = execute_query_single_row(query, (results, test_id))
    except Exception as e:
        logger.error(f"DB error on update_lab_test_results: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to update lab test results"
        )
    if not result:
        logger.warning(f"Lab test ID {test_id} not found for results update")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Lab test with ID {test_id} not found"
        )
    logger.info(f"Lab test {test_id} results updated.")
    return result


@router.delete("/{test_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_lab_test(test_id: int):
    logger.info(f"DELETE /lab-tests/{test_id}")
    query = "DELETE FROM lab_tests WHERE testID = %s RETURNING testID"
    try:
        result = execute_query_single_row(query, (test_id,))
    except Exception as e:
        logger.error(f"DB error on delete_lab_test: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to delete lab test"
        )
    if not result:
        logger.warning(f"Lab test ID {test_id} not found for delete")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Lab test with ID {test_id} not found"
        )
    logger.info(f"Lab test {test_id} deleted.")
