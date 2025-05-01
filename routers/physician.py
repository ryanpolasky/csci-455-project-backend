# Created by Ryan Polasky - 5/1/25

from fastapi import APIRouter, HTTPException, status
from typing import List, Optional
from pydantic import BaseModel
from database import execute_query, execute_query_single_row


class PhysicianCreate(BaseModel):
    name: str
    specialty: str


class PhysicianResponse(BaseModel):
    physicianID: int
    name: str
    specialty: str


router = APIRouter(
    prefix="/physicians",
    tags=["physicians"],
)


@router.post("/", response_model=PhysicianResponse, status_code=status.HTTP_201_CREATED)
def create_physician(physician: PhysicianCreate):
    query = """
    INSERT INTO physicians (name, specialty) 
    VALUES (%s, %s) 
    RETURNING physicianID, name, specialty
    """
    params = (physician.name, physician.specialty)
    result = execute_query_single_row(query, params)

    if not result:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create physician"
        )

    return result


@router.get("/", response_model=List[PhysicianResponse])
def get_physicians(skip: int = 0, limit: int = 100):
    query = """
    SELECT physicianID, name, specialty 
    FROM physicians 
    ORDER BY physicianID 
    LIMIT %s OFFSET %s
    """
    result = execute_query(query, (limit, skip))
    return result


@router.get("/{physician_id}", response_model=PhysicianResponse)
def get_physician(physician_id: int):
    query = """
    SELECT physicianID, name, specialty 
    FROM physicians 
    WHERE physicianID = %s
    """
    result = execute_query_single_row(query, (physician_id,))

    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Physician with ID {physician_id} not found"
        )

    return result


@router.get("/specialty/{specialty}", response_model=List[PhysicianResponse])
def get_physicians_by_specialty(specialty: str):
    query = """
    SELECT physicianID, name, specialty 
    FROM physicians 
    WHERE specialty = %s
    ORDER BY name
    """
    result = execute_query(query, (specialty,))
    return result


@router.put("/{physician_id}", response_model=PhysicianResponse)
def update_physician(physician_id: int, physician: PhysicianCreate):
    query = """
    UPDATE physicians 
    SET name = %s, specialty = %s 
    WHERE physicianID = %s 
    RETURNING physicianID, name, specialty
    """
    params = (physician.name, physician.specialty, physician_id)
    result = execute_query_single_row(query, params)

    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Physician with ID {physician_id} not found"
        )

    return result


@router.delete("/{physician_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_physician(physician_id: int):
    query = "DELETE FROM physicians WHERE physicianID = %s RETURNING physicianID"
    result = execute_query_single_row(query, (physician_id,))

    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Physician with ID {physician_id} not found"
        )
