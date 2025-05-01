# Created by Ryan Polasky - 5/1/25

from fastapi import APIRouter, HTTPException, status
from typing import List, Optional
from pydantic import BaseModel
from database import execute_query, execute_query_single_row


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
    query = """
    INSERT INTO nurses (name) 
    VALUES (%s) 
    RETURNING nurseID, name
    """
    result = execute_query_single_row(query, (nurse.name,))

    if not result:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create nurse"
        )

    return result


@router.get("/", response_model=List[NurseResponse])
def get_nurses(skip: int = 0, limit: int = 100):
    query = """
    SELECT nurseID, name 
    FROM nurses 
    ORDER BY nurseID 
    LIMIT %s OFFSET %s
    """
    result = execute_query(query, (limit, skip))
    return result


@router.get("/{nurse_id}", response_model=NurseResponse)
def get_nurse(nurse_id: int):
    query = """
    SELECT nurseID, name 
    FROM nurses 
    WHERE nurseID = %s
    """
    result = execute_query_single_row(query, (nurse_id,))

    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Nurse with ID {nurse_id} not found"
        )

    return result


@router.put("/{nurse_id}", response_model=NurseResponse)
def update_nurse(nurse_id: int, nurse: NurseCreate):
    query = """
    UPDATE nurses 
    SET name = %s 
    WHERE nurseID = %s 
    RETURNING nurseID, name
    """
    result = execute_query_single_row(query, (nurse.name, nurse_id))

    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Nurse with ID {nurse_id} not found"
        )

    return result


@router.delete("/{nurse_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_nurse(nurse_id: int):
    query = "DELETE FROM nurses WHERE nurseID = %s RETURNING nurseID"
    result = execute_query_single_row(query, (nurse_id,))

    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Nurse with ID {nurse_id} not found"
        )
