# Created by Ryan Polasky - 5/1/25

from fastapi import APIRouter, HTTPException, status
from typing import List, Optional
from pydantic import BaseModel
from database import execute_query, execute_query_single_row


class StaffCreate(BaseModel):
    name: str
    role: str


class StaffResponse(BaseModel):
    staffID: int
    name: str
    role: str


router = APIRouter(
    prefix="/staff",
    tags=["staff"],
)


@router.post("/", response_model=StaffResponse, status_code=status.HTTP_201_CREATED)
def create_staff(staff: StaffCreate):
    query = """
    INSERT INTO staff (name, role) 
    VALUES (%s, %s) 
    RETURNING staffID, name, role
    """
    params = (staff.name, staff.role)
    result = execute_query_single_row(query, params)

    if not result:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create staff"
        )

    return result


@router.get("/", response_model=List[StaffResponse])
def get_all_staff(skip: int = 0, limit: int = 100):
    query = """
    SELECT staffID, name, role 
    FROM staff 
    ORDER BY staffID 
    LIMIT %s OFFSET %s
    """
    result = execute_query(query, (limit, skip))
    return result


@router.get("/{staff_id}", response_model=StaffResponse)
def get_staff(staff_id: int):
    query = """
    SELECT staffID, name, role 
    FROM staff 
    WHERE staffID = %s
    """
    result = execute_query_single_row(query, (staff_id,))

    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Staff with ID {staff_id} not found"
        )

    return result


@router.put("/{staff_id}", response_model=StaffResponse)
def update_staff(staff_id: int, staff: StaffCreate):
    query = """
    UPDATE staff 
    SET name = %s, role = %s 
    WHERE staffID = %s 
    RETURNING staffID, name, role
    """
    params = (staff.name, staff.role, staff_id)
    result = execute_query_single_row(query, params)

    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Staff with ID {staff_id} not found"
        )

    return result


@router.delete("/{staff_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_staff(staff_id: int):
    query = "DELETE FROM staff WHERE staffID = %s RETURNING staffID"
    result = execute_query_single_row(query, (staff_id,))

    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Staff with ID {staff_id} not found"
        )
