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
logger = logging.getLogger("nurses")


class NurseCreate(BaseModel):
    name: str


class NurseResponse(BaseModel):
    nurseID: int
    name: str


router = APIRouter(
    prefix="/nurses",
    tags=["nurses"],
)


@router.post("/", response_model=NurseResponse, status_code=status.HTTP_201_CREATED)
def create_nurse(nurse: NurseCreate):
    logger.info(f"POST /nurses - Payload: {nurse.dict()}")
    query = """
    INSERT INTO nurses (name) 
    VALUES (%s) 
    RETURNING nurseID, name
    """
    try:
        result = execute_query_single_row(query, (nurse.name,))
    except Exception as e:
        logger.error(f"DB error on create_nurse: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create nurse"
        )
    if not result:
        logger.error("Failed to create nurse: DB returned no result.")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create nurse"
        )
    logger.info(f"Nurse created: {result}")
    return result


@router.get("/", response_model=List[NurseResponse])
def get_nurses(skip: int = 0, limit: int = 100):
    logger.info(f"GET /nurses - skip: {skip}, limit: {limit}")
    query = """
    SELECT nurseID, name 
    FROM nurses 
    ORDER BY nurseID 
    LIMIT %s OFFSET %s
    """
    try:
        result = execute_query(query, (limit, skip))
    except Exception as e:
        logger.error(f"DB error on get_nurses: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch nurses"
        )
    logger.info(f"Fetched {len(result)} nurses")
    return result


@router.get("/{nurse_id}", response_model=NurseResponse)
def get_nurse(nurse_id: int):
    logger.info(f"GET /nurses/{nurse_id}")
    query = """
    SELECT nurseID, name 
    FROM nurses 
    WHERE nurseID = %s
    """
    try:
        result = execute_query_single_row(query, (nurse_id,))
    except Exception as e:
        logger.error(f"DB error on get_nurse: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch nurse"
        )
    if not result:
        logger.warning(f"Nurse ID {nurse_id} not found")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Nurse with ID {nurse_id} not found"
        )
    return result


@router.put("/{nurse_id}", response_model=NurseResponse)
def update_nurse(nurse_id: int, nurse: NurseCreate):
    logger.info(f"PUT /nurses/{nurse_id} - Payload: {nurse.dict()}")
    query = """
    UPDATE nurses 
    SET name = %s 
    WHERE nurseID = %s 
    RETURNING nurseID, name
    """
    try:
        result = execute_query_single_row(query, (nurse.name, nurse_id))
    except Exception as e:
        logger.error(f"DB error on update_nurse: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to update nurse"
        )
    if not result:
        logger.warning(f"Nurse ID {nurse_id} not found for update")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Nurse with ID {nurse_id} not found"
        )
    logger.info(f"Nurse {nurse_id} updated.")
    return result


@router.delete("/{nurse_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_nurse(nurse_id: int):
    logger.info(f"DELETE /nurses/{nurse_id}")
    query = "DELETE FROM nurses WHERE nurseID = %s RETURNING nurseID"
    try:
        result = execute_query_single_row(query, (nurse_id,))
    except Exception as e:
        logger.error(f"DB error on delete_nurse: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to delete nurse"
        )
    if not result:
        logger.warning(f"Nurse ID {nurse_id} not found for delete")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Nurse with ID {nurse_id} not found"
        )
    logger.info(f"Nurse {nurse_id} deleted.")
