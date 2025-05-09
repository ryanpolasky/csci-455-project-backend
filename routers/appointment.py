# Created by Ryan Polasky - 5/1/25

from fastapi import APIRouter, HTTPException, status
from datetime import date, time
from typing import List, Optional
from pydantic import BaseModel
from database import execute_query, execute_query_single_row
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)
logger = logging.getLogger("appointments")


class AppointmentCreate(BaseModel):
    patientid: int
    physicianid: int
    date: date
    time: time


class AppointmentResponse(BaseModel):
    appointmentid: int
    patientid: int
    physicianid: int
    date: date
    time: time


router = APIRouter(
    prefix="/appointments",
    tags=["appointments"],
)


@router.post("/", response_model=AppointmentResponse, status_code=status.HTTP_201_CREATED)
def create_appointment(appointment: AppointmentCreate):
    logger.info(f"POST /appointments - Payload: {appointment.dict()}")
    query = """
    INSERT INTO appointment (patientid, physicianid, date, time) 
    VALUES (%s, %s, %s, %s) 
    RETURNING appointmentid, patientid, physicianid, date, time
    """
    params = (appointment.patientid, appointment.physicianid, appointment.date, appointment.time)
    try:
        result = execute_query_single_row(query, params)
    except Exception as e:
        logger.error(f"DB error on create_appointment: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create appointment"
        )
    if not result:
        logger.error("Failed to create appointment: DB returned no result.")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create appointment"
        )
    logger.info(f"Appointment created: {result}")
    return result


@router.get("/", response_model=List[AppointmentResponse])
def get_appointments(skip: int = 0, limit: int = 100):
    logger.info(f"GET /appointments - skip: {skip}, limit: {limit}")
    query = """
    SELECT appointmentid, patientid, physicianid, date, time 
    FROM appointment 
    ORDER BY date, time 
    LIMIT %s OFFSET %s
    """
    try:
        result = execute_query(query, (limit, skip))
    except Exception as e:
        logger.error(f"DB error on get_appointments: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch appointments"
        )
    logger.info(f"Fetched {len(result)} appointments")
    return result


@router.get("/{appointment_id}", response_model=AppointmentResponse)
def get_appointment(appointment_id: int):
    logger.info(f"GET /appointments/{appointment_id}")
    query = """
    SELECT appointmentid, patientid, physicianid, date, time 
    FROM appointment
    WHERE appointmentid = %s
    """
    try:
        result = execute_query_single_row(query, (appointment_id,))
    except Exception as e:
        logger.error(f"DB error on get_appointment: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch appointment"
        )
    if not result:
        logger.warning(f"Appointment ID {appointment_id} not found")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Appointment with ID {appointment_id} not found"
        )
    return result


@router.get("/patient/{patient_id}", response_model=List[AppointmentResponse])
def get_patient_appointments(patient_id: int):
    logger.info(f"GET /appointments/patient/{patient_id}")
    query = """
    SELECT appointmentid, patientid, physicianid, date, time 
    FROM appointment
    WHERE patientid = %s 
    ORDER BY date, time
    """
    try:
        result = execute_query(query, (patient_id,))
    except Exception as e:
        logger.error(f"DB error on get_patient_appointments: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch patient's appointments"
        )
    logger.info(f"Fetched {len(result)} appointments for patient {patient_id}")
    return result


@router.get("/physician/{physician_id}", response_model=List[AppointmentResponse])
def get_physician_appointments(physician_id: int):
    logger.info(f"GET /appointments/physician/{physician_id}")
    query = """
    SELECT appointmentid, patientid, physicianid, date, time 
    FROM appointment
    WHERE physicianid = %s 
    ORDER BY date, time
    """
    try:
        result = execute_query(query, (physician_id,))
    except Exception as e:
        logger.error(f"DB error on get_physician_appointments: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch physician's appointments"
        )
    logger.info(f"Fetched {len(result)} appointments for physician {physician_id}")
    return result


@router.delete("/{appointment_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_appointment(appointment_id: int):
    logger.info(f"DELETE /appointments/{appointment_id}")
    query = "DELETE FROM appointment WHERE appointmentid = %s RETURNING appointmentid"
    try:
        result = execute_query_single_row(query, (appointment_id,))
    except Exception as e:
        logger.error(f"DB error on delete_appointment: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to delete appointment"
        )
    if not result:
        logger.warning(f"Attempted delete failed: Appointment ID {appointment_id} not found")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Appointment with ID {appointment_id} not found"
        )
    logger.info(f"Appointment {appointment_id} deleted.")
