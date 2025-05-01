# CSCI 455 Final Project - Backend

A comprehensive RESTful API for healthcare management built with FastAPI and PostgreSQL. This API provides functionality for managing patients, physicians, appointments, medical records, prescriptions, lab tests, and billing in a healthcare setting.

## 🏥 Overview

This REST API enables medical facilities to digitally manage their entire operation from patient intake to billing. The system provides clean, performant endpoints for all aspects of healthcare management using direct PostgreSQL queries with proper SQL injection protection.

## 🚀 Features

- **Complete Healthcare Entity Management**: Manage patients, staff, physicians, nurses, medical records, appointments, prescriptions, lab tests, and billing
- **RESTful API Design**: Follow REST best practices with appropriate HTTP methods and status codes
- **Data Validation**: Request/response validation using Pydantic models
- **SQL Injection Protection**: Secure database queries using parameterized statements
- **Comprehensive Documentation**: Auto-generated API documentation via Swagger UI
- **Relationship Support**: Handles all relationships between healthcare entities

## ⚙️ Technology Stack

- **FastAPI**: Modern, high-performance web framework for building APIs
- **PostgreSQL**: Advanced open-source relational database
- **psycopg2**: PostgreSQL adapter for Python
- **Pydantic**: Data validation and settings management
- **Uvicorn**: ASGI server for serving the FastAPI application

## 📋 API Endpoints

### Patient Management

| Endpoint                 | Method   | Description                |
|--------------------------|----------|----------------------------|
| `/patients/`             | `GET`    | Retrieve all patients      |
| `/patients/{patient_id}` | `GET`    | Get patient by ID          |
| `/patients/`             | `POST`   | Register a new patient     |
| `/patients/{patient_id}` | `PUT`    | Update patient information |
| `/patients/{patient_id}` | `DELETE` | Remove patient from system |

### Staff Management

| Endpoint            | Method   | Description                |
|---------------------|----------|----------------------------|
| `/staff/`           | `GET`    | Retrieve all staff members |
| `/staff/{staff_id}` | `GET`    | Get staff member by ID     |
| `/staff/`           | `POST`   | Add new staff member       |
| `/staff/{staff_id}` | `PUT`    | Update staff information   |
| `/staff/{staff_id}` | `DELETE` | Remove staff member        |

### Physician Management

| Endpoint                            | Method   | Description                  |
|-------------------------------------|----------|------------------------------|
| `/physicians/`                      | `GET`    | Retrieve all physicians      |
| `/physicians/{physician_id}`        | `GET`    | Get physician by ID          |
| `/physicians/specialty/{specialty}` | `GET`    | Get physicians by specialty  |
| `/physicians/`                      | `POST`   | Add new physician            |
| `/physicians/{physician_id}`        | `PUT`    | Update physician information |
| `/physicians/{physician_id}`        | `DELETE` | Remove physician             |

### Nurse Management

| Endpoint             | Method   | Description              |
|----------------------|----------|--------------------------|
| `/nurses/`           | `GET`    | Retrieve all nurses      |
| `/nurses/{nurse_id}` | `GET`    | Get nurse by ID          |
| `/nurses/`           | `POST`   | Add new nurse            |
| `/nurses/{nurse_id}` | `PUT`    | Update nurse information |
| `/nurses/{nurse_id}` | `DELETE` | Remove nurse             |

### Medical Records Management

| Endpoint                                     | Method  | Description                          |
|----------------------------------------------|---------|--------------------------------------|
| `/medical-records/`                          | `GET`   | Retrieve all medical records         |
| `/medical-records/with-patient-info`         | `GET`   | Get records with patient information |
| `/medical-records/{record_id}`               | `GET`   | Get medical record by ID             |
| `/medical-records/patient/{patient_id}`      | `GET`   | Get medical records for a patient    |
| `/medical-records/`                          | `POST`  | Create new medical record            |
| `/medical-records/{record_id}`               | `PUT`   | Update medical record                |
| `/medical-records/{record_id}/add-diagnosis` | `PATCH` | Add diagnosis to medical record      |

### Appointment Management

| Endpoint                                 | Method   | Description                      |
|------------------------------------------|----------|----------------------------------|
| `/appointments/`                         | `GET`    | Retrieve all appointments        |
| `/appointments/{appointment_id}`         | `GET`    | Get appointment by ID            |
| `/appointments/patient/{patient_id}`     | `GET`    | Get appointments for a patient   |
| `/appointments/physician/{physician_id}` | `GET`    | Get appointments for a physician |
| `/appointments/`                         | `POST`   | Create new appointment           |
| `/appointments/{appointment_id}`         | `DELETE` | Cancel appointment               |

### Prescription Management

| Endpoint                                  | Method   | Description                                          |
|-------------------------------------------|----------|------------------------------------------------------|
| `/prescriptions/`                         | `GET`    | Retrieve all prescriptions                           |
| `/prescriptions/with-details`             | `GET`    | Get prescriptions with patient and physician details |
| `/prescriptions/{prescription_id}`        | `GET`    | Get prescription by ID                               |
| `/prescriptions/patient/{patient_id}`     | `GET`    | Get prescriptions for a patient                      |
| `/prescriptions/physician/{physician_id}` | `GET`    | Get prescriptions by physician                       |
| `/prescriptions/`                         | `POST`   | Create new prescription                              |
| `/prescriptions/{prescription_id}`        | `PUT`    | Update prescription                                  |
| `/prescriptions/{prescription_id}`        | `DELETE` | Remove prescription                                  |

### Lab Test Management

| Endpoint                              | Method   | Description                        |
|---------------------------------------|----------|------------------------------------|
| `/lab-tests/`                         | `GET`    | Retrieve all lab tests             |
| `/lab-tests/with-patient`             | `GET`    | Get tests with patient information |
| `/lab-tests/{test_id}`                | `GET`    | Get lab test by ID                 |
| `/lab-tests/patient/{patient_id}`     | `GET`    | Get lab tests for a patient        |
| `/lab-tests/`                         | `POST`   | Order new lab test                 |
| `/lab-tests/{test_id}`                | `PUT`    | Update lab test information        |
| `/lab-tests/{test_id}/update-results` | `PATCH`  | Update test results                |
| `/lab-tests/{test_id}`                | `DELETE` | Remove lab test                    |

### Billing Management

| Endpoint                              | Method   | Description                            |
|---------------------------------------|----------|----------------------------------------|
| `/billing/`                           | `GET`    | Retrieve all billing records           |
| `/billing/with-patient`               | `GET`    | Get billing with patient information   |
| `/billing/{bill_id}`                  | `GET`    | Get billing record by ID               |
| `/billing/patient/{patient_id}`       | `GET`    | Get billing records for a patient      |
| `/billing/patient/{patient_id}/total` | `GET`    | Calculate total amount due for patient |
| `/billing/`                           | `POST`   | Create new billing record              |
| `/billing/{bill_id}`                  | `PUT`    | Update billing information             |
| `/billing/{bill_id}`                  | `DELETE` | Remove billing record                  |

## 📝 Data Models

### Patient

```
patientID: int - Primary key
name: string - Patient name
dob: date - Date of birth
address: string - Patient address
phone: string - Contact phone number
insurance: string - Insurance information
```

### Staff
```
staffID: int - Primary key
name: string - Staff name
role: string - Staff role
```

### Physician
```
physicianID: int - Primary key
name: string - Physician name
specialty: string - Medical specialty
```

### Nurse
```
nurseID: int - Primary key
name: string - Nurse name
```

### Medical Record
```
recordID: int - Primary key
patientID: int - Foreign key referencing Patient
dateCreated: date - Record creation date
allergies: string - Patient allergies
medications: string - Current medications
diagnoses: string - Medical diagnoses
```

### Prescription
```
prescriptionID: int - Primary key
patientID: int - Foreign key referencing Patient
physicianID: int - Foreign key referencing Physician
medication: string - Prescribed medication
dosage: string - Dosage instructions
```

### Appointment
```
appointmentID: int - Primary key
patientID: int - Foreign key referencing Patient
physicianID: int - Foreign key referencing Physician
date: date - Appointment date
time: time - Appointment time
```

### Lab Test
```
testID: int - Primary key
patientID: int - Foreign key referencing Patient
testType: string - Type of lab test
results: string - Test results
```

### Billing
```
billID: int - Primary key
patientID: int - Foreign key referencing Patient
amountDue: float - Amount to be paid
dateIssued: date - Date bill was issued
```

## 🛠️ Installation and Setup

1. Clone the repo:
    ```shell
    git clone https://github.com/ryanpolasky/csci-455-project-backend.git
    cd csci-455-project-backend
    ```

2. Set up a virtual environment (on Windows): 
    ```shell 
    python -m venv venv
    source venv\Scripts\activate
    ```
   
3. Install dependencies:
   ```shell
    pip install -r requirements.txt
    ```

4. Configure database connection:
    ```text
    DB_HOST={your database host}
    DB_PORT={your database port, typically 5432}
    DB_NAME={name of the database}
    DB_USER={username}
    DB_PASSWORD={password}
    ```
   
5. Run the API:
    ```shell
    uvicorn main:app --reload
    ```
   
6. Either use this README file for API routes, or open your browser & navigate to http://localhost:8000/docs
   
## 📚 Best Practices Followed

- **Separation of concerns**: Database connectivity is separate from API routes
- **Parameterized queries**: All SQL queries use parameters to prevent SQL injection
- **Error handling**: Comprehensive error responses with appropriate status codes
- **Input validation**: Request data validation using Pydantic models
- **Consistent API design**: Consistent endpoint naming and response formats
- **Database connection management**: Proper connection pooling and resource cleanup
