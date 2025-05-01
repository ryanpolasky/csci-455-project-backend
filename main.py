# Created by Ryan Polasky - 5/1/25
import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from routers import (
    staff, patient, physician, nurse, medical_record,
    prescription, appointment, lab_test, billing
)
from database import get_db_connection

# Initialize the FastAPI app
app = FastAPI(
    title="CSCI 455 Final Project",
    description="API for managing a healthcare system with patients, physicians, appointments, etc.",
    version="1.0.0",
)

# Add CORS middleware
# noinspection PyTypeChecker
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include all routers
app.include_router(staff.router)
app.include_router(patient.router)
app.include_router(physician.router)
app.include_router(nurse.router)
app.include_router(medical_record.router)
app.include_router(prescription.router)
app.include_router(appointment.router)
app.include_router(lab_test.router)
app.include_router(billing.router)


@app.get("/")
def read_root():
    try:
        # Test the database connection
        with get_db_connection() as conn:
            if conn.closed == 0:  # Connection is good
                return {
                    "status": "success",
                    "message": "API up & running! :)",
                    "database": "connected successfully"
                }
            else:
                return {
                    "status": "warning",
                    "message": "API is running but database connection failed",
                    "database": "disconnected"
                }
    except Exception as e:
        return {
            "status": "error",
            "message": "API is running but database connection failed",
            "database": "error",
            "error": str(e)
        }


@app.get("/repo", include_in_schema=False)
def custom_repo_redirect():
    # Redirect to GitHub repo
    return RedirectResponse(url="https://github.com/ryanpolasky/csci-455-project-backend")


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
