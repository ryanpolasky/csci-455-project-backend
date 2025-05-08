# Created by Louis Seelbach - 5/3/25

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import requests

BASE_URL = "http://localhost:8000"  # Adjust this to your API base URL


# Replace these with actual DB function calls
def add_record(schema):
    if schema == "Patients":
        add_win = tk.Toplevel()
        add_win.title("Add Patient")

        # Removed "Patient ID" from labels
        labels = ["Name", "Date of Birth (YYYY-MM-DD)", "Address", "Phone", "Insurance"]
        entries = []

        for label in labels:
            ttk.Label(add_win, text=label).pack()
            entry = ttk.Entry(add_win)
            entry.pack()
            entries.append(entry)

        def submit():
            data = {
                # Removed "patientID" from data, as the backend expects the DB to generate it
                "name": entries[0].get(),  # Index adjusted
                "dob": entries[1].get(),  # Index adjusted
                "address": entries[2].get(),  # Index adjusted
                "phone": entries[3].get(),  # Index adjusted
                "insurance": entries[4].get()  # Index adjusted
            }
            response = requests.post(f"{BASE_URL}/patients/", json=data)
            if response.status_code == 201:
                messagebox.showinfo("Success", "Patient added successfully.")
                add_win.destroy()
            else:
                # Added print for backend error details for easier debugging
                print(f"Error adding patient: {response.status_code} - {response.text}")
                messagebox.showerror("Error", f"Failed to add patient. Status: {response.status_code}")

        ttk.Button(add_win, text="Submit", command=submit).pack(pady=10)

    elif schema == "Physicians":
        add_win = tk.Toplevel()
        add_win.title("Add Physician")

        # Removed "Physician ID" from labels
        labels = ["Name", "Specialty"]
        entries = []

        for label in labels:
            ttk.Label(add_win, text=label).pack()
            entry = ttk.Entry(add_win)
            entry.pack()
            entries.append(entry)

        def submit():
            data = {
                # Removed "physicianID" from data
                "name": entries[0].get(),  # Index adjusted
                "specialty": entries[1].get()
                # Index adjusted, Changed "role" to "specialty" to match likely backend model/README
            }
            response = requests.post(f"{BASE_URL}/physicians/", json=data)
            if response.status_code == 201:
                messagebox.showinfo("Success", "Physician added successfully.")
                add_win.destroy()
            else:
                print(f"Error adding physician: {response.status_code} - {response.text}")
                messagebox.showerror("Error", f"Failed to add physician. Status: {response.status_code}")

        ttk.Button(add_win, text="Submit", command=submit).pack(pady=10)

    elif schema == "Appointments":
        add_win = tk.Toplevel()
        add_win.title("Add Appointment")

        # Removed "Appointment ID" from labels
        labels = ["Patient ID", "Physician ID", "Date (YYYY-MM-DD)", "Time (HH:MM)"]
        entries = []

        for label in labels:
            ttk.Label(add_win, text=label).pack()
            entry = ttk.Entry(add_win)
            entry.pack()
            entries.append(entry)

        def submit():
            data = {
                # Removed "appointmentID" from data
                "patientID": entries[0].get(),  # Index adjusted
                "physicianID": entries[1].get(),  # Index adjusted
                "date": entries[2].get(),  # Index adjusted
                "time": entries[3].get()  # Index adjusted
            }
            response = requests.post(f"{BASE_URL}/appointments/", json=data)
            if response.status_code == 201:
                messagebox.showinfo("Success", "Appointment added successfully.")
                add_win.destroy()
            else:
                print(f"Error adding appointment: {response.status_code} - {response.text}")
                messagebox.showerror("Error", f"Failed to add appointment. Status: {response.status_code}")

        ttk.Button(add_win, text="Submit", command=submit).pack(pady=10)

    elif schema == "MedicalRecords":
        add_win = tk.Toplevel()
        add_win.title("Add Medical Record")

        # Removed "Record ID" from labels
        labels = ["Patient ID", "Date Created (YYYY-MM-DD)", "Allergies", "Medications", "Diagnoses"]
        entries = []

        for label in labels:
            ttk.Label(add_win, text=label).pack()
            entry = ttk.Entry(add_win)
            entry.pack()
            entries.append(entry)

        def submit():
            data = {
                # Removed "recordID" from data
                "patientID": entries[0].get(),  # Index adjusted
                "dateCreated": entries[1].get(),  # Index adjusted
                "allergies": entries[2].get(),  # Index adjusted
                "medications": entries[3].get(),  # Index adjusted, Fixed typo "medicaion" to "medications"
                "diagnoses": entries[4].get()  # Index adjusted
            }
            response = requests.post(f"{BASE_URL}/medical-records/", json=data)
            if response.status_code == 201:
                messagebox.showinfo("Success", "Medical record added successfully.")
                add_win.destroy()
            else:
                print(f"Error adding medical record: {response.status_code} - {response.text}")
                messagebox.showerror("Error", f"Failed to add medical record. Status: {response.status_code}")

        ttk.Button(add_win, text="Submit", command=submit).pack(pady=10)

    elif schema == "Prescriptions":
        add_win = tk.Toplevel()
        add_win.title("Add Prescription")

        # Removed "Prescription ID" from labels
        labels = ["Patient ID", "Physician ID", "Medication", "Dosage"]
        entries = []

        for label in labels:
            ttk.Label(add_win, text=label).pack()
            entry = ttk.Entry(add_win)
            entry.pack()
            entries.append(entry)

        def submit():
            data = {
                # Removed "prescriptionID" from data
                "patientID": entries[0].get(),  # Index adjusted
                "physicianID": entries[1].get(),  # Index adjusted
                "medication": entries[2].get(),  # Index adjusted
                "dosage": entries[3].get()  # Index adjusted
            }
            response = requests.post(f"{BASE_URL}/prescriptions/", json=data)
            if response.status_code == 201:
                messagebox.showinfo("Success", "Prescription added successfully.")
                add_win.destroy()
            else:
                print(f"Error adding prescription: {response.status_code} - {response.text}")
                messagebox.showerror("Error", f"Failed to add prescription. Status: {response.status_code}")

        ttk.Button(add_win, text="Submit", command=submit).pack(pady=10)

    elif schema == "LabTests":
        add_win = tk.Toplevel()
        add_win.title("Add Lab Test")

        # Removed "Test ID" from labels
        labels = ["Patient ID", "Test Type", "Results"]
        entries = []

        for label in labels:
            ttk.Label(add_win, text=label).pack()
            entry = ttk.Entry(add_win)
            entry.pack()
            entries.append(entry)

        def submit():
            data = {
                # Removed "testID" from data
                "patientID": entries[0].get(),  # Index adjusted
                "testType": entries[1].get(),  # Index adjusted
                "results": entries[2].get()  # Index adjusted
            }
            response = requests.post(f"{BASE_URL}/lab-tests/", json=data)
            if response.status_code == 201:
                messagebox.showinfo("Success", "Lab test added successfully.")
                add_win.destroy()
            else:
                print(f"Error adding lab test: {response.status_code} - {response.text}")
                messagebox.showerror("Error", f"Failed to add lab test. Status: {response.status_code}")

        ttk.Button(add_win, text="Submit", command=submit).pack(pady=10)

    elif schema == "Billing":
        add_win = tk.Toplevel()
        add_win.title("Add Billing")

        # Removed "Billing ID" from labels
        labels = ["Patient ID", "Amount Due", "Date Issued (YYYY-MM-DD)"]
        entries = []

        for label in labels:
            ttk.Label(add_win, text=label).pack()
            entry = ttk.Entry(add_win)
            entry.pack()
            entries.append(entry)

        def submit():
            data = {
                # Removed "billingID" from data
                "patientID": entries[0].get(),  # Index adjusted
                "amountDue": entries[1].get(),  # Index adjusted
                "dateIssued": entries[2].get()  # Index adjusted
            }
            response = requests.post(f"{BASE_URL}/billing/", json=data)
            if response.status_code == 201:
                messagebox.showinfo("Success", "Billing record added successfully.")
                add_win.destroy()
            else:
                print(f"Error adding billing: {response.status_code} - {response.text}")
                messagebox.showerror("Error", f"Failed to add billing record. Status: {response.status_code}")

        ttk.Button(add_win, text="Submit", command=submit).pack(pady=10)

    elif schema == "Nurses":
        add_win = tk.Toplevel()
        add_win.title("Add Nurse")

        # Removed "Nurse ID" from labels
        labels = ["Name"]
        entries = []

        for label in labels:
            ttk.Label(add_win, text=label).pack()
            entry = ttk.Entry(add_win)
            entry.pack()
            entries.append(entry)

        def submit():
            data = {
                # Removed "nurseID" from data
                "name": entries[0].get(),  # Index adjusted
            }
            response = requests.post(f"{BASE_URL}/nurses/", json=data)
            if response.status_code == 201:
                messagebox.showinfo("Success", "Nurse added successfully.")
                add_win.destroy()
            else:
                print(f"Error adding nurse: {response.status_code} - {response.text}")
                messagebox.showerror("Error", f"Failed to add nurse. Status: {response.status_code}")

        ttk.Button(add_win, text="Submit", command=submit).pack(pady=10)

    elif schema == "Staff":
        add_win = tk.Toplevel()
        add_win.title("Add Staff")

        # Removed "Staff ID" from labels
        labels = ["Name", "Role"]
        entries = []

        for label in labels:
            ttk.Label(add_win, text=label).pack()
            entry = ttk.Entry(add_win)
            entry.pack()
            entries.append(entry)

        def submit():
            data = {
                # Removed "staffID" from data
                "name": entries[0].get(),  # Index adjusted
                "role": entries[1].get()  # Index adjusted
            }
            response = requests.post(f"{BASE_URL}/staff/", json=data)
            if response.status_code == 201:
                messagebox.showinfo("Success", "Staff added successfully.")
                add_win.destroy()
            else:
                print(f"Error adding staff: {response.status_code} - {response.text}")
                messagebox.showerror("Error", f"Failed to add staff. Status: {response.status_code}")

        ttk.Button(add_win, text="Submit", command=submit).pack(pady=10)


# The rest of the functions (remove_record, search, show_all, update, etc.) remain the same
# as they correctly use IDs to interact with existing records.

def remove_record(schema):
    if schema == "Patients":
        rm_win = tk.Toplevel()
        rm_win.title("Remove Patient")

        ttk.Label(rm_win, text="Enter Patient ID to remove:").pack()
        id_entry = ttk.Entry(rm_win)
        id_entry.pack()

        def submit():
            patient_id = id_entry.get()
            # Check if ID is provided and is an integer
            if not patient_id.isdigit():
                messagebox.showerror("Error", "Please enter a valid numeric ID.")
                return
            response = requests.delete(f"{BASE_URL}/patients/{patient_id}")
            if response.status_code == 204:  # Changed from 200 to 204 based on backend spec
                messagebox.showinfo("Success", "Patient removed.")
                rm_win.destroy()
            elif response.status_code == 404:
                messagebox.showerror("Error", f"Patient with ID {patient_id} not found.")
            else:
                print(f"Error removing patient: {response.status_code} - {response.text}")
                messagebox.showerror("Error", f"Failed to remove patient. Status: {response.status_code}")

        ttk.Button(rm_win, text="Submit", command=submit).pack(pady=10)

    elif schema == "Physicians":
        rm_win = tk.Toplevel()
        rm_win.title("Remove Physician")

        ttk.Label(rm_win, text="Enter Physician ID to remove:").pack()
        id_entry = ttk.Entry(rm_win)
        id_entry.pack()

        def submit():
            physician_id = id_entry.get()
            if not physician_id.isdigit():
                messagebox.showerror("Error", "Please enter a valid numeric ID.")
                return
            response = requests.delete(f"{BASE_URL}/physicians/{physician_id}")
            if response.status_code == 204:
                messagebox.showinfo("Success", "Physician removed.")
                rm_win.destroy()
            elif response.status_code == 404:
                messagebox.showerror("Error", f"Physician with ID {physician_id} not found.")
            else:
                print(f"Error removing physician: {response.status_code} - {response.text}")
                messagebox.showerror("Error", f"Failed to remove physician. Status: {response.status_code}")

        ttk.Button(rm_win, text="Submit", command=submit).pack(pady=10)

    elif schema == "Appointments":
        rm_win = tk.Toplevel()
        rm_win.title("Remove Appointment")

        ttk.Label(rm_win, text="Enter Appointment ID to remove:").pack()
        id_entry = ttk.Entry(rm_win)
        id_entry.pack()

        def submit():
            appointment_id = id_entry.get()
            if not appointment_id.isdigit():
                messagebox.showerror("Error", "Please enter a valid numeric ID.")
                return
            response = requests.delete(f"{BASE_URL}/appointments/{appointment_id}")
            if response.status_code == 204:
                messagebox.showinfo("Success", "Appointment removed.")
                rm_win.destroy()
            elif response.status_code == 404:
                messagebox.showerror("Error", f"Appointment with ID {appointment_id} not found.")
            else:
                print(f"Error removing appointment: {response.status_code} - {response.text}")
                messagebox.showerror("Error", f"Failed to remove appointment. Status: {response.status_code}")

        ttk.Button(rm_win, text="Submit", command=submit).pack(pady=10)

    elif schema == "MedicalRecords":
        rm_win = tk.Toplevel()
        rm_win.title("Remove Medical Record")

        ttk.Label(rm_win, text="Enter Record ID to remove:").pack()
        id_entry = ttk.Entry(rm_win)
        id_entry.pack()

        def submit():
            record_id = id_entry.get()
            if not record_id.isdigit():
                messagebox.showerror("Error", "Please enter a valid numeric ID.")
                return
            response = requests.delete(f"{BASE_URL}/medical-records/{record_id}")
            if response.status_code == 204:
                messagebox.showinfo("Success", "Medical record removed.")
                rm_win.destroy()
            elif response.status_code == 404:
                messagebox.showerror("Error", f"Medical record with ID {record_id} not found.")
            else:
                print(f"Error removing medical record: {response.status_code} - {response.text}")
                messagebox.showerror("Error", f"Failed to remove medical record. Status: {response.status_code}")

        ttk.Button(rm_win, text="Submit", command=submit).pack(pady=10)

    elif schema == "Prescriptions":
        rm_win = tk.Toplevel()
        rm_win.title("Remove Prescription")

        ttk.Label(rm_win, text="Enter Prescription ID to remove:").pack()
        id_entry = ttk.Entry(rm_win)
        id_entry.pack()

        def submit():
            prescription_id = id_entry.get()
            if not prescription_id.isdigit():
                messagebox.showerror("Error", "Please enter a valid numeric ID.")
                return
            response = requests.delete(f"{BASE_URL}/prescriptions/{prescription_id}")
            if response.status_code == 204:
                messagebox.showinfo("Success", "Prescription removed.")
                rm_win.destroy()
            elif response.status_code == 404:
                messagebox.showerror("Error", f"Prescription with ID {prescription_id} not found.")
            else:
                print(f"Error removing prescription: {response.status_code} - {response.text}")
                messagebox.showerror("Error", f"Failed to remove prescription. Status: {response.status_code}")

        ttk.Button(rm_win, text="Submit", command=submit).pack(pady=10)

    elif schema == "LabTests":
        rm_win = tk.Toplevel()
        rm_win.title("Remove Lab Test")

        ttk.Label(rm_win, text="Enter Test ID to remove:").pack()
        id_entry = ttk.Entry(rm_win)
        id_entry.pack()

        def submit():
            test_id = id_entry.get()
            if not test_id.isdigit():
                messagebox.showerror("Error", "Please enter a valid numeric ID.")
                return
            response = requests.delete(f"{BASE_URL}/lab-tests/{test_id}")
            if response.status_code == 204:
                messagebox.showinfo("Success", "Lab test removed.")
                rm_win.destroy()
            elif response.status_code == 404:
                messagebox.showerror("Error", f"Lab test with ID {test_id} not found.")
            else:
                print(f"Error removing lab test: {response.status_code} - {response.text}")
                messagebox.showerror("Error", f"Failed to remove lab test. Status: {response.status_code}")

        ttk.Button(rm_win, text="Submit", command=submit).pack(pady=10)

    elif schema == "Billing":
        rm_win = tk.Toplevel()
        rm_win.title("Remove Billing")

        ttk.Label(rm_win, text="Enter Billing ID to remove:").pack()
        id_entry = ttk.Entry(rm_win)
        id_entry.pack()

        def submit():
            billing_id = id_entry.get()
            if not billing_id.isdigit():
                messagebox.showerror("Error", "Please enter a valid numeric ID.")
                return
            response = requests.delete(f"{BASE_URL}/billing/{billing_id}")
            if response.status_code == 204:
                messagebox.showinfo("Success", "Billing record removed.")
                rm_win.destroy()
            elif response.status_code == 404:
                messagebox.showerror("Error", f"Billing record with ID {billing_id} not found.")
            else:
                print(f"Error removing billing: {response.status_code} - {response.text}")
                messagebox.showerror("Error", f"Failed to remove billing record. Status: {response.status_code}")

        ttk.Button(rm_win, text="Submit", command=submit).pack(pady=10)

    elif schema == "Nurses":
        rm_win = tk.Toplevel()
        rm_win.title("Remove Nurse")

        ttk.Label(rm_win, text="Enter Nurse ID to remove:").pack()
        id_entry = ttk.Entry(rm_win)
        id_entry.pack()

        def submit():
            nurse_id = id_entry.get()
            if not nurse_id.isdigit():
                messagebox.showerror("Error", "Please enter a valid numeric ID.")
                return
            response = requests.delete(f"{BASE_URL}/nurses/{nurse_id}")
            if response.status_code == 204:
                messagebox.showinfo("Success", "Nurse removed.")
                rm_win.destroy()
            elif response.status_code == 404:
                messagebox.showerror("Error", f"Nurse with ID {nurse_id} not found.")
            else:
                print(f"Error removing nurse: {response.status_code} - {response.text}")
                messagebox.showerror("Error", f"Failed to remove nurse. Status: {response.status_code}")

        ttk.Button(rm_win, text="Submit", command=submit).pack(pady=10)

    elif schema == "Staff":
        rm_win = tk.Toplevel()
        rm_win.title("Remove Staff")

        ttk.Label(rm_win, text="Enter Staff ID to remove:").pack()
        id_entry = ttk.Entry(rm_win)
        id_entry.pack()

        def submit():
            staff_id = id_entry.get()
            if not staff_id.isdigit():
                messagebox.showerror("Error", "Please enter a valid numeric ID.")
                return
            response = requests.delete(f"{BASE_URL}/staff/{staff_id}")
            if response.status_code == 204:
                messagebox.showinfo("Success", "Staff removed.")
                rm_win.destroy()
            elif response.status_code == 404:
                messagebox.showerror("Error", f"Staff with ID {staff_id} not found.")
            else:
                print(f"Error removing staff: {response.status_code} - {response.text}")
                messagebox.showerror("Error", f"Failed to remove staff. Status: {response.status_code}")

        ttk.Button(rm_win, text="Submit", command=submit).pack(pady=10)


def search(schema):
    if schema == "Patients":
        search_win = tk.Toplevel()
        search_win.title("Search Patient")

        ttk.Label(search_win, text="Enter Patient ID:").pack()
        id_entry = ttk.Entry(search_win)
        id_entry.pack()

        def submit():
            patient_id = id_entry.get()
            if not patient_id.isdigit():
                messagebox.showerror("Error", "Please enter a valid numeric ID.")
                return
            response = requests.get(f"{BASE_URL}/patients/{patient_id}")
            if response.status_code == 200:
                p = response.json()
                info = f"ID: {p['patientID']}\nName: {p['name']}\nDOB: {p['dob']}\nAddress: {p['address']}\nPhone: {p['phone']}\nInsurance: {p['insurance']}"
                messagebox.showinfo("Patient Info", info)
            elif response.status_code == 404:
                messagebox.showerror("Error", f"Patient with ID {patient_id} not found.")
            else:
                print(f"Error searching patient: {response.status_code} - {response.text}")
                messagebox.showerror("Error", f"Failed to search patient. Status: {response.status_code}")

        ttk.Button(search_win, text="Search", command=submit).pack(pady=10)

    elif schema == "Physicians":
        search_win = tk.Toplevel()
        search_win.title("Search Physician")

        ttk.Label(search_win, text="Enter Physician ID:").pack()
        id_entry = ttk.Entry(search_win)
        id_entry.pack()

        def submit():
            physician_id = id_entry.get()
            if not physician_id.isdigit():
                messagebox.showerror("Error", "Please enter a valid numeric ID.")
                return
            response = requests.get(f"{BASE_URL}/physicians/{physician_id}")
            if response.status_code == 200:
                p = response.json()
                # Corrected 'role' to 'specialty' to match the backend model and README
                info = f"ID: {p['physicianID']}\nName: {p['name']}\nSpecialty: {p['specialty']}"
                messagebox.showinfo("Physician Info", info)
            elif response.status_code == 404:
                messagebox.showerror("Error", f"Physician with ID {physician_id} not found.")
            else:
                print(f"Error searching physician: {response.status_code} - {response.text}")
                messagebox.showerror("Error", f"Failed to search physician. Status: {response.status_code}")

        ttk.Button(search_win, text="Search", command=submit).pack(pady=10)

    elif schema == "Appointments":
        search_win = tk.Toplevel()
        search_win.title("Search Appointment")

        ttk.Label(search_win, text="Enter Appointment ID:").pack()
        id_entry = ttk.Entry(search_win)
        id_entry.pack()

        def submit():
            appointment_id = id_entry.get()
            if not appointment_id.isdigit():
                messagebox.showerror("Error", "Please enter a valid numeric ID.")
                return
            response = requests.get(f"{BASE_URL}/appointments/{appointment_id}")
            if response.status_code == 200:
                a = response.json()
                info = f"ID: {a['appointmentID']}\nPatient ID: {a['patientID']}\nPhysician ID: {a['physicianID']}\nDate: {a['date']}\nTime: {a['time']}"
                messagebox.showinfo("Appointment Info", info)
            elif response.status_code == 404:
                messagebox.showerror("Error", f"Appointment with ID {appointment_id} not found.")
            else:
                print(f"Error searching appointment: {response.status_code} - {response.text}")
                messagebox.showerror("Error", f"Failed to search appointment. Status: {response.status_code}")

        ttk.Button(search_win, text="Search", command=submit).pack(pady=10)

    elif schema == "MedicalRecords":
        search_win = tk.Toplevel()
        search_win.title("Search Medical Record")

        ttk.Label(search_win, text="Enter Record ID:").pack()
        id_entry = ttk.Entry(search_win)
        id_entry.pack()

        def submit():
            record_id = id_entry.get()
            if not record_id.isdigit():
                messagebox.showerror("Error", "Please enter a valid numeric ID.")
                return
            response = requests.get(f"{BASE_URL}/medical-records/{record_id}")
            if response.status_code == 200:
                m = response.json()
                # Corrected 'medication' key name if needed (assuming backend uses 'medications')
                medications_val = m.get('medications',
                                        m.get('medication', 'N/A'))  # Handle potential backend key name variations
                info = f"ID: {m['recordID']}\nPatient ID: {m['patientID']}\nDate Created: {m['dateCreated']}\nAllergies: {m['allergies']}\nMedications: {medications_val}\nDiagnoses: {m['diagnoses']}"
                messagebox.showinfo("Medical Record Info", info)
            elif response.status_code == 404:
                messagebox.showerror("Error", f"Medical record with ID {record_id} not found.")
            else:
                print(f"Error searching medical record: {response.status_code} - {response.text}")
                messagebox.showerror("Error", f"Failed to search medical record. Status: {response.status_code}")

        ttk.Button(search_win, text="Search", command=submit).pack(pady=10)

    elif schema == "Prescriptions":
        search_win = tk.Toplevel()
        search_win.title("Search Prescription")

        ttk.Label(search_win, text="Enter Prescription ID:").pack()
        id_entry = ttk.Entry(search_win)
        id_entry.pack()

        def submit():
            prescription_id = id_entry.get()
            if not prescription_id.isdigit():
                messagebox.showerror("Error", "Please enter a valid numeric ID.")
                return
            response = requests.get(f"{BASE_URL}/prescriptions/{prescription_id}")
            if response.status_code == 200:
                p = response.json()
                info = f"ID: {p['prescriptionID']}\nPatient ID: {p['patientID']}\nPhysician ID: {p['physicianID']}\nMedication: {p['medication']}\nDosage: {p['dosage']}"
                messagebox.showinfo("Prescription Info", info)
            elif response.status_code == 404:
                messagebox.showerror("Error", f"Prescription with ID {prescription_id} not found.")
            else:
                print(f"Error searching prescription: {response.status_code} - {response.text}")
                messagebox.showerror("Error", f"Failed to search prescription. Status: {response.status_code}")

        ttk.Button(search_win, text="Search", command=submit).pack(pady=10)

    elif schema == "LabTests":
        search_win = tk.Toplevel()
        search_win.title("Search Lab Test")

        ttk.Label(search_win, text="Enter Test ID:").pack()
        id_entry = ttk.Entry(search_win)
        id_entry.pack()

        def submit():
            test_id = id_entry.get()
            if not test_id.isdigit():
                messagebox.showerror("Error", "Please enter a valid numeric ID.")
                return
            response = requests.get(f"{BASE_URL}/lab-tests/{test_id}")
            if response.status_code == 200:
                l = response.json()
                info = f"ID: {l['testID']}\nPatient ID: {l['patientID']}\nTest Type: {l['testType']}\nResults: {l['results']}"
                messagebox.showinfo("Lab Test Info", info)
            elif response.status_code == 404:
                messagebox.showerror("Error", f"Lab test with ID {test_id} not found.")
            else:
                print(f"Error searching lab test: {response.status_code} - {response.text}")
                messagebox.showerror("Error", f"Failed to search lab test. Status: {response.status_code}")

        ttk.Button(search_win, text="Search", command=submit).pack(pady=10)

    elif schema == "Billing":
        search_win = tk.Toplevel()
        search_win.title("Search Billing")

        ttk.Label(search_win, text="Enter Billing ID:").pack()
        id_entry = ttk.Entry(search_win)
        id_entry.pack()

        def submit():
            billing_id = id_entry.get()
            if not billing_id.isdigit():
                messagebox.showerror("Error", "Please enter a valid numeric ID.")
                return
            response = requests.get(f"{BASE_URL}/billing/{billing_id}")
            if response.status_code == 200:
                b = response.json()
                info = f"ID: {b['billID']}\nPatient ID: {b['patientID']}\nAmount Due: {b['amountDue']}\nDate Issued: {b['dateIssued']}"  # Corrected ID key from billingID to billID based on README/backend likely
                messagebox.showinfo("Billing Info", info)
            elif response.status_code == 404:
                messagebox.showerror("Error", f"Billing record with ID {billing_id} not found.")
            else:
                print(f"Error searching billing: {response.status_code} - {response.text}")
                messagebox.showerror("Error", f"Failed to search billing record. Status: {response.status_code}")

        ttk.Button(search_win, text="Search", command=submit).pack(pady=10)

    elif schema == "Nurses":
        search_win = tk.Toplevel()
        search_win.title("Search Nurse")

        ttk.Label(search_win, text="Enter Nurse ID:").pack()
        id_entry = ttk.Entry(search_win)
        id_entry.pack()

        def submit():
            nurse_id = id_entry.get()
            if not nurse_id.isdigit():
                messagebox.showerror("Error", "Please enter a valid numeric ID.")
                return
            response = requests.get(f"{BASE_URL}/nurses/{nurse_id}")
            if response.status_code == 200:
                n = response.json()
                info = f"ID: {n['nurseID']}\nName: {n['name']}"
                messagebox.showinfo("Nurse Info", info)
            elif response.status_code == 404:
                messagebox.showerror("Error", f"Nurse with ID {nurse_id} not found.")
            else:
                print(f"Error searching nurse: {response.status_code} - {response.text}")
                messagebox.showerror("Error", f"Failed to search nurse. Status: {response.status_code}")

        ttk.Button(search_win, text="Search", command=submit).pack(pady=10)

    elif schema == "Staff":
        search_win = tk.Toplevel()
        search_win.title("Search Staff")

        ttk.Label(search_win, text="Enter Staff ID:").pack()
        id_entry = ttk.Entry(search_win)
        id_entry.pack()

        def submit():
            staff_id = id_entry.get()
            if not staff_id.isdigit():
                messagebox.showerror("Error", "Please enter a valid numeric ID.")
                return
            response = requests.get(f"{BASE_URL}/staff/{staff_id}")
            if response.status_code == 200:
                s = response.json()
                info = f"ID: {s['staffID']}\nName: {s['name']}\nRole: {s['role']}"
                messagebox.showinfo("Staff Info", info)
            elif response.status_code == 404:
                messagebox.showerror("Error", f"Staff with ID {staff_id} not found.")
            else:
                print(f"Error searching staff: {response.status_code} - {response.text}")
                messagebox.showerror("Error", f"Failed to search staff. Status: {response.status_code}")

        ttk.Button(search_win, text="Search", command=submit).pack(pady=10)


def show_all(schema):
    if schema == "Patients":
        response = requests.get(f"{BASE_URL}/patients/")
        if response.status_code == 200:
            patients = response.json()
            if not patients:
                messagebox.showinfo("All Patients", "No patients found.")
                return
            output = "\n\n".join([
                f"ID: {p['patientID']}\nName: {p['name']}\nDOB: {p['dob']}\nAddress: {p['address']}\nPhone: {p['phone']}\nInsurance: {p['insurance']}"
                # Added Address and Insurance for completeness
                for p in patients
            ])
            messagebox.showinfo("All Patients", output)
        else:
            print(f"Error showing all patients: {response.status_code} - {response.text}")
            messagebox.showerror("Error", "Could not retrieve patients.")

    elif schema == "Physicians":
        response = requests.get(f"{BASE_URL}/physicians/")
        if response.status_code == 200:
            physicians = response.json()
            if not physicians:
                messagebox.showinfo("All Physicians", "No physicians found.")
                return
            output = "\n\n".join([
                # Corrected 'role' to 'specialty'
                f"ID: {p['physicianID']}\nName: {p['name']}\nSpecialty: {p['specialty']}"
                for p in physicians
            ])
            messagebox.showinfo("All Physicians", output)
        else:
            print(f"Error showing all physicians: {response.status_code} - {response.text}")
            messagebox.showerror("Error", "Could not retrieve physicians.")

    elif schema == "Appointments":
        response = requests.get(f"{BASE_URL}/appointments/")
        if response.status_code == 200:
            appointments = response.json()
            if not appointments:
                messagebox.showinfo("All Appointments", "No appointments found.")
                return
            output = "\n\n".join([
                f"ID: {a['appointmentID']}\nPatient ID: {a['patientID']}\nPhysician ID: {a['physicianID']}\nDate: {a['date']}\nTime: {a['time']}"
                for a in appointments
            ])
            messagebox.showinfo("All Appointments", output)
        else:
            print(f"Error showing all appointments: {response.status_code} - {response.text}")
            messagebox.showerror("Error", "Could not retrieve appointments.")

    elif schema == "MedicalRecords":
        response = requests.get(f"{BASE_URL}/medical-records/")
        if response.status_code == 200:
            records = response.json()
            if not records:
                messagebox.showinfo("All Medical Records", "No medical records found.")
                return
            output = "\n\n".join([
                # Corrected 'medication' key name if needed
                f"ID: {m['recordID']}\nPatient ID: {m['patientID']}\nDate Created: {m['dateCreated']}\nAllergies: {m['allergies']}\nMedications: {m.get('medications', m.get('medication', 'N/A'))}\nDiagnoses: {m['diagnoses']}"
                for m in records
            ])
            messagebox.showinfo("All Medical Records", output)
        else:
            print(f"Error showing all medical records: {response.status_code} - {response.text}")
            messagebox.showerror("Error", "Could not retrieve medical records.")

    elif schema == "Prescriptions":
        response = requests.get(f"{BASE_URL}/prescriptions/")
        if response.status_code == 200:
            prescriptions = response.json()
            if not prescriptions:
                messagebox.showinfo("All Prescriptions", "No prescriptions found.")
                return
            output = "\n\n".join([
                f"ID: {p['prescriptionID']}\nPatient ID: {p['patientID']}\nPhysician ID: {p['physicianID']}\nMedication: {p['medication']}\nDosage: {p['dosage']}"
                for p in prescriptions
            ])
            messagebox.showinfo("All Prescriptions", output)
        else:
            print(f"Error showing all prescriptions: {response.status_code} - {response.text}")
            messagebox.showerror("Error", "Could not retrieve prescriptions.")

    elif schema == "LabTests":
        response = requests.get(f"{BASE_URL}/lab-tests/")
        if response.status_code == 200:
            lab_tests = response.json()
            if not lab_tests:
                messagebox.showinfo("All Lab Tests", "No lab tests found.")
                return
            output = "\n\n".join([
                f"ID: {l['testID']}\nPatient ID: {l['patientID']}\nTest Type: {l['testType']}\nResults: {l['results']}"
                for l in lab_tests
            ])
            messagebox.showinfo("All Lab Tests", output)
        else:
            print(f"Error showing all lab tests: {response.status_code} - {response.text}")
            messagebox.showerror("Error", "Could not retrieve lab tests.")

    elif schema == "Billing":
        response = requests.get(f"{BASE_URL}/billing/")
        if response.status_code == 200:
            billing = response.json()
            if not billing:
                messagebox.showinfo("All Billing Records", "No billing records found.")
                return
            output = "\n\n".join([
                # Corrected ID key from billingID to billID
                f"ID: {b['billID']}\nPatient ID: {b['patientID']}\nAmount Due: {b['amountDue']}\nDate Issued: {b['dateIssued']}"
                for b in billing
            ])
            messagebox.showinfo("All Billing Records", output)
        else:
            print(f"Error showing all billing: {response.status_code} - {response.text}")
            messagebox.showerror("Error", "Could not retrieve billing records.")

    elif schema == "Nurses":
        response = requests.get(f"{BASE_URL}/nurses/")
        if response.status_code == 200:
            nurses = response.json()
            if not nurses:
                messagebox.showinfo("All Nurses", "No nurses found.")
                return
            output = "\n\n".join([
                f"ID: {n['nurseID']}\nName: {n['name']}"
                for n in nurses
            ])
            messagebox.showinfo("All Nurses", output)
        else:
            print(f"Error showing all nurses: {response.status_code} - {response.text}")
            messagebox.showerror("Error", "Could not retrieve nurses.")

    elif schema == "Staff":
        response = requests.get(f"{BASE_URL}/staff/")
        if response.status_code == 200:
            staff = response.json()
            if not staff:
                messagebox.showinfo("All Staff", "No staff found.")
                return
            output = "\n\n".join([
                f"ID: {s['staffID']}\nName: {s['name']}\nRole: {s['role']}"
                for s in staff
            ])
            messagebox.showinfo("All Staff", output)
        else:
            print(f"Error showing all staff: {response.status_code} - {response.text}")
            messagebox.showerror("Error", "Could not retrieve staff.")


def update(schema):
    # Added input validation for ID field in update functions
    def validate_and_update(id_entry, data, url):
        record_id = id_entry.get()
        if not record_id.isdigit():
            messagebox.showerror("Error", "Please enter a valid numeric ID for the record to update.")
            return
        try:
            response = requests.put(f"{url}/{record_id}", json=data)
            if response.status_code == 200:
                messagebox.showinfo("Success", f"{schema} updated.")
                return True  # Indicate success
            elif response.status_code == 404:
                messagebox.showerror("Error", f"{schema} with ID {record_id} not found.")
            else:
                print(f"Error updating {schema}: {response.status_code} - {response.text}")
                messagebox.showerror("Error", f"Failed to update {schema}. Status: {response.status_code}")
            return False  # Indicate failure
        except Exception as e:
            print(f"Exception during update: {e}")
            messagebox.showerror("Error", f"An error occurred during update: {e}")
            return False

    if schema == "Patients":
        upd_win = tk.Toplevel()
        upd_win.title("Update Patient Info")

        ttk.Label(upd_win, text="Patient ID to update:").pack()
        id_entry = ttk.Entry(upd_win)
        id_entry.pack()

        labels = ["Name", "Date of Birth (YYYY-MM-DD)", "Address", "Phone", "Insurance"]
        entries = []

        for label in labels:
            ttk.Label(upd_win, text=label).pack()
            entry = ttk.Entry(upd_win)
            entry.pack()
            entries.append(entry)

        def submit():
            data = {
                "name": entries[0].get(),
                "dob": entries[1].get(),
                "address": entries[2].get(),
                "phone": entries[3].get(),
                "insurance": entries[4].get()
            }
            if validate_and_update(id_entry, data, f"{BASE_URL}/patients"):
                upd_win.destroy()

        ttk.Button(upd_win, text="Update", command=submit).pack(pady=10)

    elif schema == "Physicians":
        upd_win = tk.Toplevel()
        upd_win.title("Update Physician Info")

        ttk.Label(upd_win, text="Physician ID to update:").pack()
        id_entry = ttk.Entry(upd_win)
        id_entry.pack()

        labels = ["Name", "Specialty"]
        entries = []

        for label in labels:
            ttk.Label(upd_win, text=label).pack()
            entry = ttk.Entry(upd_win)
            entry.pack()
            entries.append(entry)

        def submit():
            data = {
                "name": entries[0].get(),
                "specialty": entries[1].get()  # Corrected 'role' to 'specialty'
            }
            if validate_and_update(id_entry, data, f"{BASE_URL}/physicians"):
                upd_win.destroy()

        ttk.Button(upd_win, text="Update", command=submit).pack(pady=10)

    elif schema == "Appointments":
        upd_win = tk.Toplevel()
        upd_win.title("Update Appointment Info")

        ttk.Label(upd_win, text="Appointment ID to update:").pack()
        id_entry = ttk.Entry(upd_win)
        id_entry.pack()

        labels = ["Patient ID", "Physician ID", "Date (YYYY-MM-DD)", "Time (HH:MM)"]
        entries = []

        for label in labels:
            ttk.Label(upd_win, text=label).pack()
            entry = ttk.Entry(upd_win)
            entry.pack()
            entries.append(entry)

        def submit():
            data = {
                "patientID": entries[0].get(),
                "physicianID": entries[1].get(),
                "date": entries[2].get(),
                "time": entries[3].get()
            }
            if validate_and_update(id_entry, data, f"{BASE_URL}/appointments"):
                upd_win.destroy()

        ttk.Button(upd_win, text="Update", command=submit).pack(pady=10)

    elif schema == "MedicalRecords":
        upd_win = tk.Toplevel()
        upd_win.title("Update Medical Record Info")

        ttk.Label(upd_win, text="Record ID to update:").pack()
        id_entry = ttk.Entry(upd_win)
        id_entry.pack()

        labels = ["Patient ID", "Date Created (YYYY-MM-DD)", "Allergies", "Medications", "Diagnoses"]
        entries = []

        for label in labels:
            ttk.Label(upd_win, text=label).pack()
            entry = ttk.Entry(upd_win)
            entry.pack()
            entries.append(entry)

        def submit():
            data = {
                "patientID": entries[0].get(),
                "dateCreated": entries[1].get(),
                "allergies": entries[2].get(),
                "medications": entries[3].get(),  # Corrected 'medication' to 'medications'
                "diagnoses": entries[4].get()
            }
            if validate_and_update(id_entry, data, f"{BASE_URL}/medical-records"):
                upd_win.destroy()

        ttk.Button(upd_win, text="Update", command=submit).pack(pady=10)

    elif schema == "Prescriptions":
        upd_win = tk.Toplevel()
        upd_win.title("Update Prescription Info")

        ttk.Label(upd_win, text="Prescription ID to update:").pack()
        id_entry = ttk.Entry(upd_win)
        id_entry.pack()

        labels = ["Patient ID", "Physician ID", "Medication", "Dosage"]
        entries = []

        for label in labels:
            ttk.Label(upd_win, text=label).pack()
            entry = ttk.Entry(upd_win)
            entry.pack()
            entries.append(entry)

        def submit():
            data = {
                "patientID": entries[0].get(),
                "physicianID": entries[1].get(),
                "medication": entries[2].get(),
                "dosage": entries[3].get()
            }
            if validate_and_update(id_entry, data, f"{BASE_URL}/prescriptions"):
                upd_win.destroy()

        ttk.Button(upd_win, text="Update", command=submit).pack(pady=10)

    elif schema == "LabTests":
        upd_win = tk.Toplevel()
        upd_win.title("Update Lab Test Info")

        ttk.Label(upd_win, text="Test ID to update:").pack()
        id_entry = ttk.Entry(upd_win)
        id_entry.pack()

        labels = ["Patient ID", "Test Type", "Results"]
        entries = []

        for label in labels:
            ttk.Label(upd_win, text=label).pack()
            entry = ttk.Entry(upd_win)
            entry.pack()
            entries.append(entry)

        def submit():
            data = {
                "patientID": entries[0].get(),
                "testType": entries[1].get(),
                "results": entries[2].get()
            }
            if validate_and_update(id_entry, data, f"{BASE_URL}/lab-tests"):
                upd_win.destroy()

        ttk.Button(upd_win, text="Update", command=submit).pack(pady=10)

    elif schema == "Billing":
        upd_win = tk.Toplevel()
        upd_win.title("Update Billing Info")

        ttk.Label(upd_win, text="Billing ID to update:").pack()
        id_entry = ttk.Entry(upd_win)
        id_entry.pack()

        labels = ["Patient ID", "Amount Due", "Date Issued (YYYY-MM-DD)"]
        entries = []

        for label in labels:
            ttk.Label(upd_win, text=label).pack()
            entry = ttk.Entry(upd_win)
            entry.pack()
            entries.append(entry)

        def submit():
            data = {
                "patientID": entries[0].get(),
                "amountDue": entries[1].get(),
                "dateIssued": entries[2].get()
            }
            # Corrected URL to match backend spec using bill_id
            if validate_and_update(id_entry, data, f"{BASE_URL}/billing"):
                upd_win.destroy()

        ttk.Button(upd_win, text="Update", command=submit).pack(pady=10)

    elif schema == "Nurses":
        upd_win = tk.Toplevel()
        upd_win.title("Update Nurse Info")

        ttk.Label(upd_win, text="Nurse ID to update:").pack()
        id_entry = ttk.Entry(upd_win)
        id_entry.pack()

        labels = ["Name"]
        entries = []

        for label in labels:
            ttk.Label(upd_win, text=label).pack()
            entry = ttk.Entry(upd_win)
            entry.pack()
            entries.append(entry)

        def submit():
            data = {
                "name": entries[0].get()
            }
            if validate_and_update(id_entry, data, f"{BASE_URL}/nurses"):
                upd_win.destroy()

        ttk.Button(upd_win, text="Update", command=submit).pack(pady=10)

    elif schema == "Staff":
        upd_win = tk.Toplevel()
        upd_win.title("Update Staff Info")

        ttk.Label(upd_win, text="Staff ID to update:").pack()
        id_entry = ttk.Entry(upd_win)
        id_entry.pack()

        labels = ["Name", "Role"]
        entries = []

        for label in labels:
            ttk.Label(upd_win, text=label).pack()
            entry = ttk.Entry(upd_win)
            entry.pack()
            entries.append(entry)

        def submit():
            data = {
                "name": entries[0].get(),
                "role": entries[1].get()
            }
            if validate_and_update(id_entry, data, f"{BASE_URL}/staff"):
                upd_win.destroy()

        ttk.Button(upd_win, text="Update", command=submit).pack(pady=10)


def search_by_specialty():
    search_win = tk.Toplevel()
    search_win.title("Search Physician by Specialty")

    ttk.Label(search_win, text="Enter Specialty:").pack()
    id_entry = ttk.Entry(search_win)  # This is specialty, not ID
    id_entry.pack()

    def submit():
        specialty = id_entry.get()
        # Changed endpoint from /staff/{specialty} to /physicians/specialty/{specialty} based on README/backend spec
        response = requests.get(f"{BASE_URL}/physicians/specialty/{specialty}")
        if response.status_code == 200:
            physicians = response.json()
            if not physicians:
                messagebox.showinfo(f"Physicians in {specialty}", f"No physicians found with specialty: {specialty}")
                return
            output = "\n\n".join([
                # Corrected 'role' to 'specialty'
                f"ID: {p['physicianID']}\nName: {p['name']}\nSpecialty: {p['specialty']}"
                for p in physicians
            ])
            messagebox.showinfo(f"Physicians in {specialty}", output)
        elif response.status_code == 404:  # Backend might return 404 if no physicians found
            messagebox.showinfo(f"Physicians in {specialty}", f"No physicians found with specialty: {specialty}")
        else:
            print(f"Error searching physicians by specialty: {response.status_code} - {response.text}")
            messagebox.showerror("Error", f"Failed to search physicians by specialty. Status: {response.status_code}")

    ttk.Button(search_win, text="Search", command=submit).pack(pady=10)


def show_all_w_patient_info(schema):
    if schema == "MedicalRecords":
        response = requests.get(f"{BASE_URL}/medical-records/with-patient-info/")
        if response.status_code == 200:
            records = response.json()
            if not records:
                messagebox.showinfo("All Medical Records With Patient Info",
                                    "No medical records with patient info found.")
                return
            output = "\n\n".join([
                # Corrected 'medication' key name if needed, ensured patient info keys match
                f"Record ID: {m['recordID']}\nPatient ID: {m['patientID']}\nPatient Name: {m['name']}\nDOB: {m['dob']}\nPhone: {m['phone']}\nDate Created: {m['dateCreated']}\nAllergies: {m['allergies']}\nMedications: {m.get('medications', m.get('medication', 'N/A'))}\nDiagnoses: {m['diagnoses']}"
                for m in records
            ])
            messagebox.showinfo("All Medical Records With Patient Info", output)
        else:
            print(f"Error showing medical records with patient info: {response.status_code} - {response.text}")
            messagebox.showerror("Error", "Could not retrieve medical records with patient info.")

    elif schema == "LabTests":
        response = requests.get(f"{BASE_URL}/lab-tests/with-patient/")
        if response.status_code == 200:
            lab_tests = response.json()
            if not lab_tests:
                messagebox.showinfo("All Lab Tests With Patient Info", "No lab tests with patient info found.")
                return
            output = "\n\n".join([
                # Ensured patient info keys match
                f"Test ID: {l['testID']}\nPatient ID: {l['patientID']}\nPatient Name: {l['name']}\nDOB: {l['dob']}\nPhone: {l['phone']}\nTest Type: {l['testType']}\nResults: {l['results']}"
                for l in lab_tests
            ])
            messagebox.showinfo("All Lab Tests With Patient Info", output)
        else:
            print(f"Error showing lab tests with patient info: {response.status_code} - {response.text}")
            messagebox.showerror("Error", "Could not retrieve lab tests with patient info.")

    elif schema == "Billing":
        response = requests.get(f"{BASE_URL}/billing/with-patient/")
        if response.status_code == 200:
            billing = response.json()
            if not billing:
                messagebox.showinfo("All Billing Records With Patient Info",
                                    "No billing records with patient info found.")
                return
            output = "\n\n".join([
                # Corrected ID key, ensured patient info keys match
                f"Bill ID: {b['billID']}\nPatient ID: {b['patientID']}\nPatient Name: {b['name']}\nDOB: {b['dob']}\nPhone: {b['phone']}\nAmount Due: {b['amountDue']}\nDate Issued: {b['dateIssued']}"
                for b in billing
            ])
            messagebox.showinfo("All Billing Records With Patient Info", output)
        else:
            print(f"Error showing billing records with patient info: {response.status_code} - {response.text}")
            messagebox.showerror("Error", "Could not retrieve billing records with patient info.")


def search_by_other(schema, other_schema):
    # Added input validation for ID field in search_by_other functions
    def validate_and_search(id_entry, url_template, info_title, error_msg_suffix):
        entity_id = id_entry.get()
        if not entity_id.isdigit():
            messagebox.showerror("Error", f"Please enter a valid numeric {other_schema} ID.")
            return

        try:
            response = requests.get(url_template.format(entity_id=entity_id))
            if response.status_code == 200:
                results = response.json()
                if isinstance(results, list):  # Handle endpoints returning lists (e.g., records by patient)
                    if not results:
                        messagebox.showinfo(info_title, f"No {schema} found for {other_schema} ID {entity_id}.")
                        return
                    output = "\n\n".join([str(item) for item in results])  # Simple string conversion
                    messagebox.showinfo(info_title, output)
                else:  # Handle endpoints returning single objects
                    messagebox.showinfo(info_title, str(results))  # Simple string conversion
            elif response.status_code == 404:
                messagebox.showinfo(info_title,
                                    f"No {schema} found for {other_schema} ID {entity_id}.")  # 404 often means no records found
            else:
                print(f"Error searching {schema} by {other_schema}: {response.status_code} - {response.text}")
                messagebox.showerror("Error", f"Failed to search {error_msg_suffix}. Status: {response.status_code}")
        except Exception as e:
            print(f"Exception during search_by_other: {e}")
            messagebox.showerror("Error", f"An error occurred during search: {e}")

    if schema == "MedicalRecords":
        search_win = tk.Toplevel()
        search_win.title(f"Search Medical Record By {other_schema}")  # Dynamically set title

        ttk.Label(search_win, text=f"Enter {other_schema} ID:").pack()
        id_entry = ttk.Entry(search_win)
        id_entry.pack()

        def submit():
            # Assuming the backend endpoint is /medical-records/patient/{patient_id}
            validate_and_search(id_entry, f"{BASE_URL}/medical-records/patient/{{entity_id}}",
                                f"Medical Records for {other_schema} ID {id_entry.get()}",
                                f"medical records by {other_schema.lower()}")

        ttk.Button(search_win, text="Search", command=submit).pack(pady=10)


    elif schema == "Appointments":
        search_win = tk.Toplevel()
        search_win.title(f"Search Appointment By {other_schema}")  # Dynamically set title

        ttk.Label(search_win, text=f"Enter {other_schema} ID:").pack()
        id_entry = ttk.Entry(search_win)
        id_entry.pack()

        def submit():
            if other_schema == "Patients":
                # Assuming the backend endpoint is /appointments/patient/{patient_id}
                validate_and_search(id_entry, f"{BASE_URL}/appointments/patient/{{entity_id}}",
                                    f"Appointments for {other_schema} ID {id_entry.get()}",
                                    f"appointments by {other_schema.lower()}")

            elif other_schema == "Physicians":
                # Assuming the backend endpoint is /appointments/physician/{physician_id}
                validate_and_search(id_entry, f"{BASE_URL}/appointments/physician/{{entity_id}}",
                                    f"Appointments for {other_schema} ID {id_entry.get()}",
                                    f"appointments by {other_schema.lower()}")

        ttk.Button(search_win, text="Search", command=submit).pack(pady=10)

    elif schema == "Prescriptions":
        search_win = tk.Toplevel()
        search_win.title(f"Search Prescription By {other_schema}")  # Dynamically set title

        ttk.Label(search_win, text=f"Enter {other_schema} ID:").pack()
        id_entry = ttk.Entry(search_win)
        id_entry.pack()

        def submit():
            if other_schema == "Patients":
                # Assuming the backend endpoint is /prescriptions/patient/{patient_id}
                validate_and_search(id_entry, f"{BASE_URL}/prescriptions/patient/{{entity_id}}",
                                    f"Prescriptions for {other_schema} ID {id_entry.get()}",
                                    f"prescriptions by {other_schema.lower()}")

            elif other_schema == "Physicians":
                # Assuming the backend endpoint is /prescriptions/physician/{physician_id}
                validate_and_search(id_entry, f"{BASE_URL}/prescriptions/physician/{{entity_id}}",
                                    f"Prescriptions for {other_schema} ID {id_entry.get()}",
                                    f"prescriptions by {other_schema.lower()}")

        ttk.Button(search_win, text="Search", command=submit).pack(pady=10)

    elif schema == "LabTests":
        search_win = tk.Toplevel()
        search_win.title(f"Search Lab Test By {other_schema}")  # Dynamically set title

        ttk.Label(search_win, text=f"Enter {other_schema} ID:").pack()
        id_entry = ttk.Entry(search_win)
        id_entry.pack()

        def submit():
            # Assuming the backend endpoint is /lab-tests/patient/{patient_id}
            validate_and_search(id_entry, f"{BASE_URL}/lab-tests/patient/{{entity_id}}",
                                f"Lab Tests for {other_schema} ID {id_entry.get()}",
                                f"lab tests by {other_schema.lower()}")

        ttk.Button(search_win, text="Search", command=submit).pack(pady=10)

    elif schema == "Billing":
        search_win = tk.Toplevel()
        search_win.title(f"Search Billing By {other_schema}")  # Dynamically set title

        ttk.Label(search_win, text=f"Enter {other_schema} ID:").pack()
        id_entry = ttk.Entry(search_win)
        id_entry.pack()

        def submit():
            # Assuming the backend endpoint is /billing/patient/{patient_id}
            validate_and_search(id_entry, f"{BASE_URL}/billing/patient/{{entity_id}}",
                                f"Billing Records for {other_schema} ID {id_entry.get()}",
                                f"billing records by {other_schema.lower()}")

        ttk.Button(search_win, text="Search", command=submit).pack(pady=10)


def add_diagnosis():
    diag_win = tk.Toplevel()
    diag_win.title("Add Diagnosis")

    ttk.Label(diag_win, text="Medical Record ID:").pack()
    id_entry = ttk.Entry(diag_win)
    id_entry.pack()

    ttk.Label(diag_win, text="Diagnosis:").pack()
    diag_entry = ttk.Entry(diag_win, width=40)
    diag_entry.pack()

    def submit():
        record_id = id_entry.get()
        diagnosis = diag_entry.get()

        if not record_id.isdigit():
            messagebox.showerror("Error", "Please enter a valid numeric Medical Record ID.")
            return

        response = requests.patch(
            f"{BASE_URL}/medical-records/{record_id}/add-diagnosis",
            json={"diagnosis": diagnosis}
        )

        if response.status_code == 200:
            messagebox.showinfo("Success", "Diagnosis added successfully.")
            diag_win.destroy()
        elif response.status_code == 404:
            messagebox.showerror("Error", f"Medical record with ID {record_id} not found.")
        else:
            print(f"Error adding diagnosis: {response.status_code} - {response.text}")
            messagebox.showerror("Error", f"Failed to add diagnosis. Status: {response.status_code}")

    ttk.Button(diag_win, text="Submit", command=submit).pack(pady=10)


def show_all_w_details():
    response = requests.get(f"{BASE_URL}/prescriptions/with-details/")
    if response.status_code == 200:
        prescriptions = response.json()
        if not prescriptions:
            messagebox.showinfo("All Prescriptions With Details", "No prescriptions with details found.")
            return
        output = "\n\n".join([
            # Ensured keys match expected backend output
            f"ID: {p.get('prescriptionID', 'N/A')}\nPatient ID: {p.get('patientID', 'N/A')}\nPhysician ID: {p.get('physicianID', 'N/A')}\nMedication: {p.get('medication', 'N/A')}\nDosage: {p.get('dosage', 'N/A')}\nPatient Name: {p.get('patient_name', 'N/A')}\nDOB: {p.get('dob', 'N/A')}\nPhone: {p.get('phone', 'N/A')}\nPhysician Name: {p.get('physician_name', 'N/A')}\nSpecialty: {p.get('specialty', p.get('role', 'N/A'))}"
            # Handle physician role/specialty key
            for p in prescriptions
        ])
        messagebox.showinfo("All Prescriptions With Details", output)
    else:
        print(f"Error showing all prescriptions with details: {response.status_code} - {response.text}")
        messagebox.showerror("Error", "Could not retrieve prescriptions.")


def update_results():
    update_win = tk.Toplevel()
    update_win.title("Update Lab Test Results")

    ttk.Label(update_win, text="Lab Test ID:").pack()
    id_entry = ttk.Entry(update_win)
    id_entry.pack()

    ttk.Label(update_win, text="Results:").pack()
    result_entry = ttk.Entry(update_win, width=40)
    result_entry.pack()

    def submit():
        test_id = id_entry.get()
        results = result_entry.get()

        if not test_id or not results:
            messagebox.showerror("Error", "Both fields are required.")
            return
        if not test_id.isdigit():
            messagebox.showerror("Error", "Please enter a valid numeric Lab Test ID.")
            return

        response = requests.patch(
            f"{BASE_URL}/lab-tests/{test_id}/update-results",
            json={"results": results}
        )

        if response.status_code == 200:
            messagebox.showinfo("Success", "Lab results updated.")
            update_win.destroy()
        elif response.status_code == 404:
            messagebox.showerror("Error", f"Lab test with ID {test_id} not found.")
        else:
            print(f"Error updating lab test results: {response.status_code} - {response.text}")
            messagebox.showerror("Error", f"Failed to update results. Status: {response.status_code}")

    ttk.Button(update_win, text="Submit", command=submit).pack(pady=10)


def calculate_billing_total():
    search_win = tk.Toplevel()
    search_win.title("Calculate Total Amount Due for Patient")

    ttk.Label(search_win, text="Enter Patient ID:").pack()
    id_entry = ttk.Entry(search_win)
    id_entry.pack()

    def submit():
        patient_id = id_entry.get()
        if not patient_id.isdigit():
            messagebox.showerror("Error", "Please enter a valid numeric Patient ID.")
            return

        response = requests.get(f"{BASE_URL}/billing/patient/{patient_id}/total")
        if response.status_code == 200:
            b = response.json()
            # Assuming the backend returns {'total': value}
            if 'total' in b:
                info = f"Total Amount Due: ${b['total']:.2f}"  # Format as currency
                messagebox.showinfo("Billing Info", info)
            else:
                # Handle unexpected response structure
                print(f"Unexpected response for total billing: {b}")
                messagebox.showerror("Error", "Received unexpected data from the backend.")
        elif response.status_code == 404:
            # Backend might return 404 if patient not found or no billing records
            messagebox.showinfo("Billing Info", f"No billing records found for patient ID {patient_id}.")
        else:
            print(f"Error calculating billing total: {response.status_code} - {response.text}")
            messagebox.showerror("Error", f"Failed to calculate total. Status: {response.status_code}")

    ttk.Button(search_win, text="Search", command=submit).pack(pady=10)


# Submenu Window
def open_schema_menu(schema):
    sub_window = tk.Toplevel()
    sub_window.title(f"{schema} Management")

    ttk.Label(sub_window, text=f"{schema} Menu", font=("Arial", 16)).pack(pady=10)

    ttk.Button(sub_window, text=f"Add {schema}", command=lambda: add_record(schema)).pack(pady=5)
    ttk.Button(sub_window, text=f"Remove {schema}", command=lambda: remove_record(schema)).pack(pady=5)
    ttk.Button(sub_window, text=f"Search", command=lambda: search(schema)).pack(pady=5)
    ttk.Button(sub_window, text=f"Show all {schema}", command=lambda: show_all(schema)).pack(pady=5)
    ttk.Button(sub_window, text=f"Update {schema}", command=lambda: update(schema)).pack(pady=5)

    if schema == "Physicians":
        # Corrected label text to reflect action and schema
        ttk.Button(sub_window, text="Search Physicians By Specialty", command=lambda: search_by_specialty()).pack(
            pady=5)

    elif schema == "MedicalRecords":
        ttk.Button(sub_window, text="Show all with Patient Info", command=lambda: show_all_w_patient_info(schema)).pack(
            pady=5)
        ttk.Button(sub_window, text="Search by Patient ID", command=lambda: search_by_other(schema, "Patient")).pack(
            pady=5)  # Changed "Patients" to "Patient" for clarity in label/message
        ttk.Button(sub_window, text="Add Diagnosis", command=lambda: add_diagnosis()).pack(pady=5)

    elif schema == "Appointments":
        ttk.Button(sub_window, text="Search by Patient ID", command=lambda: search_by_other(schema, "Patient")).pack(
            pady=5)  # Changed "Patients" to "Patient"
        ttk.Button(sub_window, text="Search by Physician ID",
                   command=lambda: search_by_other(schema, "Physician")).pack(
            pady=5)  # Changed "Physicians" to "Physician"

    elif schema == "Prescriptions":
        ttk.Button(sub_window, text="Show All With Details", command=lambda: show_all_w_details()).pack(pady=5)
        ttk.Button(sub_window, text="Search by Patient ID", command=lambda: search_by_other(schema, "Patient")).pack(
            pady=5)  # Changed "Patients" to "Patient"
        ttk.Button(sub_window, text="Search by Physician ID",
                   command=lambda: search_by_other(schema, "Physician")).pack(
            pady=5)  # Changed "Physicians" to "Physician"

    elif schema == "LabTests":
        ttk.Button(sub_window, text="Show all with Patient Info", command=lambda: show_all_w_patient_info(schema)).pack(
            pady=5)
        ttk.Button(sub_window, text="Search by Patient ID", command=lambda: search_by_other(schema, "Patient")).pack(
            pady=5)  # Changed "Patients" to "Patient"
        ttk.Button(sub_window, text="Update Lab Test Results", command=lambda: update_results()).pack(pady=5)

    elif schema == "Billing":
        ttk.Button(sub_window, text="Show all with Patient Info", command=lambda: show_all_w_patient_info(schema)).pack(
            pady=5)
        ttk.Button(sub_window, text="Search by Patient ID", command=lambda: search_by_other(schema, "Patient")).pack(
            pady=5)  # Changed "Patients" to "Patient"
        ttk.Button(sub_window, text="Calculate Total Due", command=lambda: calculate_billing_total()).pack(pady=5)

    ttk.Button(sub_window, text="Back", command=sub_window.destroy).pack(pady=5)


# Main GUI
def main_gui():
    root = tk.Tk()
    root.title("Medical System Staff Interface")
    root.geometry("400x600")

    ttk.Label(root, text="Medical System Staff Menu", font=("Arial", 18)).pack(pady=20)

    schemas = [
        "Appointments", "Billing", "LabTests", "MedicalRecords",
        "Nurses", "Patients", "Physicians", "Prescriptions", "Staff"
    ]

    for schema in schemas:
        ttk.Button(root, text=schema, width=30, command=lambda s=schema: open_schema_menu(s)).pack(pady=5)

    root.mainloop()


if __name__ == "__main__":
    main_gui()
