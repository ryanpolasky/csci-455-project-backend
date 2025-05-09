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
logger = logging.getLogger("physicians")


class PhysicianCreate(BaseModel):
    name: str
    specialty: str


class PhysicianResponse(BaseModel):
    physicianid: int
    name: str
    specialty: str


router = APIRouter(
    prefix="/physicians",
    tags=["physicians"],
)


@router.post("/", response_model=PhysicianResponse, status_code=status.HTTP_201_CREATED)
def create_physician(physician: PhysicianCreate):
    logger.info(f"POST /physicians - Payload: {physician.dict()}")
    query = """
    INSERT INTO physician (name, specialty) 
    VALUES (%s, %s) 
    RETURNING physicianid, name, specialty
    """
    params = (physician.name, physician.specialty)
    try:
        result = execute_query_single_row(query, params)
    except Exception as e:
        logger.error(f"DB error on create_physician: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create physician"
        )
    if not result:
        logger.error("Failed to create physician: DB returned no result.")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create physician"
        )
    logger.info(f"Physician created: {result}")
    return result


@router.get("/", response_model=List[PhysicianResponse])
def get_physicians(skip: int = 0, limit: int = 100):
    logger.info(f"GET /physicians - skip: {skip}, limit: {limit}")
    query = """
    SELECT physicianid, name, specialty 
    FROM physician 
    ORDER BY physicianid 
    LIMIT %s OFFSET %s
    """
    try:
        result = execute_query(query, (limit, skip))
    except Exception as e:
        logger.error(f"DB error on get_physicians: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch physicians"
        )
    logger.info(f"Fetched {len(result)} physicians")
    return result


@router.get("/{physician_id}", response_model=PhysicianResponse)
def get_physician(physician_id: int):
    logger.info(f"GET /physicians/{physician_id}")
    query = """
    SELECT physicianid, name, specialty 
    FROM physician 
    WHERE physicianid = %s
    """
    try:
        result = execute_query_single_row(query, (physician_id,))
    except Exception as e:
        logger.error(f"DB error on get_physician: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch physician"
        )
    if not result:
        logger.warning(f"Physician ID {physician_id} not found")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Physician with ID {physician_id} not found"
        )
    return result


@router.get("/specialty/{specialty}", response_model=List[PhysicianResponse])
def get_physicians_by_specialty(specialty: str):
    logger.info(f"GET /physicians/specialty/{specialty}")
    query = """
    SELECT physicianid, name, specialty 
    FROM physician 
    WHERE specialty = %s
    ORDER BY name
    """
    try:
        result = execute_query(query, (specialty,))
    except Exception as e:
        logger.error(f"DB error on get_physicians_by_specialty: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch physicians by specialty"
        )
    logger.info(f"Fetched {len(result)} physicians with specialty '{specialty}'")
    return result


@router.put("/{physician_id}", response_model=PhysicianResponse)
def update_physician(physician_id: int, physician: PhysicianCreate):
    logger.info(f"PUT /physicians/{physician_id} - Payload: {physician.dict()}")
    query = """
    UPDATE physician 
    SET name = %s, specialty = %s 
    WHERE physicianid = %s 
    RETURNING physicianid, name, specialty
    """
    params = (physician.name, physician.specialty, physician_id)
    try:
        result = execute_query_single_row(query, params)
    except Exception as e:
        logger.error(f"DB error on update_physician: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to update physician"
        )
    if not result:
        logger.warning(f"Physician ID {physician_id} not found for update")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Physician with ID {physician_id} not found"
        )
    logger.info(f"Physician {physician_id} updated.")
    return result


@router.delete("/{physician_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_physician(physician_id: int):
    logger.info(f"DELETE /physicians/{physician_id}")
    query = "DELETE FROM physician WHERE physicianid = %s RETURNING physicianid"
    try:
        result = execute_query_single_row(query, (physician_id,))
    except Exception as e:
        logger.error(f"DB error on delete_physician: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to delete physician"
        )
    if not result:
        logger.warning(f"Physician ID {physician_id} not found for delete")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Physician with ID {physician_id} not found"
        )
    logger.info(f"Physician {physician_id} deleted.")
