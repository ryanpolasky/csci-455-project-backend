# Created by Ryan Polasky - 5/1/25

from fastapi import APIRouter, HTTPException, status
from datetime import date, time
from typing import List, Optional
from pydantic import BaseModel
from database import execute_query, execute_query_single_row


class AppointmentCreate(BaseModel):
    patientID: int
    physicianID: int
    date: date
    time: time


class AppointmentResponse(BaseModel):
    appointmentID: int
    patientID: int
    physicianID: int
    date: date
    time: time


router = APIRouter(
    prefix="/appointments",
    tags=["appointments"],
)


@router.post("/", response_model=AppointmentResponse, status_code=status.HTTP_201_CREATED)
def create_appointment(appointment: AppointmentCreate):
    query = """
    INSERT INTO appointments (patientID, physicianID, date, time) 
    VALUES (%s, %s, %s, %s) 
    RETURNING appointmentID, patientID, physicianID, date, time
    """
    params = (appointment.patientID, appointment.physicianID, appointment.date, appointment.time)
    result = execute_query_single_row(query, params)

    if not result:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create appointment"
        )

    return result


@router.get("/", response_model=List[AppointmentResponse])
def get_appointments(skip: int = 0, limit: int = 100):
    query = """
    SELECT appointmentID, patientID, physicianID, date, time 
    FROM appointments 
    ORDER BY date, time 
    LIMIT %s OFFSET %s
    """
    result = execute_query(query, (limit, skip))
    return result


@router.get("/{appointment_id}", response_model=AppointmentResponse)
def get_appointment(appointment_id: int):
    query = """
    SELECT appointmentID, patientID, physicianID, date, time 
    FROM appointments 
    WHERE appointmentID = %s
    """
    result = execute_query_single_row(query, (appointment_id,))

    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Appointment with ID {appointment_id} not found"
        )

    return result


@router.get("/patient/{patient_id}", response_model=List[AppointmentResponse])
def get_patient_appointments(patient_id: int):
    query = """
    SELECT appointmentID, patientID, physicianID, date, time 
    FROM appointments 
    WHERE patientID = %s 
    ORDER BY date, time
    """
    result = execute_query(query, (patient_id,))
    return result


@router.get("/physician/{physician_id}", response_model=List[AppointmentResponse])
def get_physician_appointments(physician_id: int):
    query = """
    SELECT appointmentID, patientID, physicianID, date, time 
    FROM appointments 
    WHERE physicianID = %s 
    ORDER BY date, time
    """
    result = execute_query(query, (physician_id,))
    return result


@router.delete("/{appointment_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_appointment(appointment_id: int):
    query = "DELETE FROM appointments WHERE appointmentID = %s RETURNING appointmentID"
    result = execute_query_single_row(query, (appointment_id,))

    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Appointment with ID {appointment_id} not found"
        )
