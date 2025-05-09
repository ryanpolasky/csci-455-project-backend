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
logger = logging.getLogger("staff")


class StaffCreate(BaseModel):
    name: str
    role: str


class StaffResponse(BaseModel):
    staffid: int
    name: str
    role: str


router = APIRouter(
    prefix="/staff",
    tags=["staff"],
)


@router.post("/", response_model=StaffResponse, status_code=status.HTTP_201_CREATED)
def create_staff(staff: StaffCreate):
    logger.info(f"POST /staff - Payload: {staff.dict()}")
    query = """
    INSERT INTO staff (name, role) 
    VALUES (%s, %s) 
    RETURNING staffid, name, role
    """
    params = (staff.name, staff.role)
    try:
        result = execute_query_single_row(query, params)
    except Exception as e:
        logger.error(f"DB error on create_staff: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create staff"
        )
    if not result:
        logger.error("Failed to create staff: DB returned no result.")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create staff"
        )
    logger.info(f"Staff created: {result}")
    return result


@router.get("/", response_model=List[StaffResponse])
def get_all_staff(skip: int = 0, limit: int = 100):
    logger.info(f"GET /staff - skip: {skip}, limit: {limit}")
    query = """
    SELECT staffid, name, role 
    FROM staff 
    ORDER BY staffid 
    LIMIT %s OFFSET %s
    """
    try:
        result = execute_query(query, (limit, skip))
    except Exception as e:
        logger.error(f"DB error on get_all_staff: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch staff"
        )
    logger.info(f"Fetched {len(result)} staff records")
    return result


@router.get("/{staff_id}", response_model=StaffResponse)
def get_staff(staff_id: int):
    logger.info(f"GET /staff/{staff_id}")
    query = """
    SELECT staffid, name, role 
    FROM staff 
    WHERE staffid = %s
    """
    try:
        result = execute_query_single_row(query, (staff_id,))
    except Exception as e:
        logger.error(f"DB error on get_staff: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch staff"
        )
    if not result:
        logger.warning(f"Staff ID {staff_id} not found")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Staff with ID {staff_id} not found"
        )
    return result


@router.put("/{staff_id}", response_model=StaffResponse)
def update_staff(staff_id: int, staff: StaffCreate):
    logger.info(f"PUT /staff/{staff_id} - Payload: {staff.dict()}")
    query = """
    UPDATE staff 
    SET name = %s, role = %s 
    WHERE staffid = %s 
    RETURNING staffid, name, role
    """
    params = (staff.name, staff.role, staff_id)
    try:
        result = execute_query_single_row(query, params)
    except Exception as e:
        logger.error(f"DB error on update_staff: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to update staff"
        )
    if not result:
        logger.warning(f"Staff ID {staff_id} not found for update")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Staff with ID {staff_id} not found"
        )
    logger.info(f"Staff {staff_id} updated.")
    return result


@router.delete("/{staff_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_staff(staff_id: int):
    logger.info(f"DELETE /staff/{staff_id}")
    query = "DELETE FROM staff WHERE staffid = %s RETURNING staffid"
    try:
        result = execute_query_single_row(query, (staff_id,))
    except Exception as e:
        logger.error(f"DB error on delete_staff: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to delete staff"
        )
    if not result:
        logger.warning(f"Staff ID {staff_id} not found for delete")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Staff with ID {staff_id} not found"
        )
    logger.info(f"Staff {staff_id} deleted.")
