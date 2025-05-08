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

        labels = ["Patient ID", "Name", "Date of Birth (YYYY-MM-DD)", "Address", "Phone", "Insurance"]
        entries = []

        for label in labels:
            ttk.Label(add_win, text=label).pack()
            entry = ttk.Entry(add_win)
            entry.pack()
            entries.append(entry)

        def submit():
            data = {
                "patientID": entries[0].get(),
                "name": entries[1].get(),
                "dob": entries[2].get(),
                "address": entries[3].get(),
                "phone": entries[4].get(),
                "insurance": entries[5].get()
            }
            response = requests.post(f"{BASE_URL}/patients/", json=data)
            if response.status_code == 201:
                messagebox.showinfo("Success", "Patient added successfully.")
                add_win.destroy()
            else:
                messagebox.showerror("Error", "Failed to add patient.")

        ttk.Button(add_win, text="Submit", command=submit).pack(pady=10)

    elif schema == "Physicians":
        add_win = tk.Toplevel()
        add_win.title("Add Physician")

        labels = ["Physician ID", "Name", "Specialty"]
        entries = []

        for label in labels:
            ttk.Label(add_win, text=label).pack()
            entry = ttk.Entry(add_win)
            entry.pack()
            entries.append(entry)

        def submit():
            data = {
                "physicianID": entries[0].get(),
                "name": entries[1].get(),
                "role": entries[2].get()
            }
            response = requests.post(f"{BASE_URL}/physicians/", json=data)
            if response.status_code == 201:
                messagebox.showinfo("Success", "Physician added successfully.")
                add_win.destroy()
            else:
                messagebox.showerror("Error", "Failed to add physician.")

        ttk.Button(add_win, text="Submit", command=submit).pack(pady=10)

    elif schema == "Appointments":
        add_win = tk.Toplevel()
        add_win.title("Add Appointment")

        labels = ["Appointment ID", "Patient ID", "Physician ID", "Date (YYYY-MM-DD)", "Time (HH:MM)"]
        entries = []

        for label in labels:
            ttk.Label(add_win, text=label).pack()
            entry = ttk.Entry(add_win)
            entry.pack()
            entries.append(entry)

        def submit():
            data = {
                "appointmentID": entries[0].get(),
                "patientID": entries[1].get(),
                "physicianID": entries[2].get(),
                "date": entries[3].get(),
                "time": entries[4].get()
            }
            response = requests.post(f"{BASE_URL}/appointments/", json=data)
            if response.status_code == 201:
                messagebox.showinfo("Success", "Appointment added successfully.")
                add_win.destroy()
            else:
                messagebox.showerror("Error", "Failed to add appointment.")

        ttk.Button(add_win, text="Submit", command=submit).pack(pady=10)

    elif schema == "MedicalRecords":
        add_win = tk.Toplevel()
        add_win.title("Add Medical Record")

        labels = ["Record ID", "Patient ID", "Date Created (YYYY-MM-DD)", "Allergies", "Medications", "Diagnoses"]
        entries = []

        for label in labels:
            ttk.Label(add_win, text=label).pack()
            entry = ttk.Entry(add_win)
            entry.pack()
            entries.append(entry)

        def submit():
            data = {
                "recordID": entries[0].get(),
                "patientID": entries[1].get(),
                "dateCreated": entries[2].get(),
                "allergies": entries[3].get(),
                "medicaion": entries[4].get(),
                "diagnoses": entries[5].get()
            }
            response = requests.post(f"{BASE_URL}/medical-records/", json=data)
            if response.status_code == 201:
                messagebox.showinfo("Success", "Medical record added successfully.")
                add_win.destroy()
            else:
                messagebox.showerror("Error", "Failed to add medical record.")

        ttk.Button(add_win, text="Submit", command=submit).pack(pady=10)

    elif schema == "Prescriptions":
        add_win = tk.Toplevel()
        add_win.title("Add Prescription")

        labels = ["Prescription ID", "Patient ID", "Physician ID", "Medication", "Dosage"]
        entries = []

        for label in labels:
            ttk.Label(add_win, text=label).pack()
            entry = ttk.Entry(add_win)
            entry.pack()
            entries.append(entry)

        def submit():
            data = {
                "prescriptionID": entries[0].get(),
                "patientID": entries[1].get(),
                "physicianID": entries[2].get(),
                "medication": entries[3].get(),
                "dosage": entries[4].get()
            }
            response = requests.post(f"{BASE_URL}/prescriptions/", json=data)
            if response.status_code == 201:
                messagebox.showinfo("Success", "Prescription added successfully.")
                add_win.destroy()
            else:
                messagebox.showerror("Error", "Failed to add prescription.")

        ttk.Button(add_win, text="Submit", command=submit).pack(pady=10)

    elif schema == "LabTests":
        add_win = tk.Toplevel()
        add_win.title("Add Lab Test")

        labels = ["Test ID", "Patient ID", "Test Type", "Results"]
        entries = []

        for label in labels:
            ttk.Label(add_win, text=label).pack()
            entry = ttk.Entry(add_win)
            entry.pack()
            entries.append(entry)

        def submit():
            data = {
                "testID": entries[0].get(),
                "patientID": entries[1].get(),
                "testType": entries[2].get(),
                "results": entries[3].get()
            }
            response = requests.post(f"{BASE_URL}/lab-tests/", json=data)
            if response.status_code == 201:
                messagebox.showinfo("Success", "Lab test added successfully.")
                add_win.destroy()
            else:
                messagebox.showerror("Error", "Failed to add lab test.")

        ttk.Button(add_win, text="Submit", command=submit).pack(pady=10)

    elif schema == "Billing":
        add_win = tk.Toplevel()
        add_win.title("Add Billing")

        labels = ["Billing ID", "Patient ID", "Amount Due", "Date Issued (YYYY-MM-DD)"]
        entries = []

        for label in labels:
            ttk.Label(add_win, text=label).pack()
            entry = ttk.Entry(add_win)
            entry.pack()
            entries.append(entry)

        def submit():
            data = {
                "billingID": entries[0].get(),
                "patientID": entries[1].get(),
                "amountDue": entries[2].get(),
                "dateIssued": entries[3].get()
            }
            response = requests.post(f"{BASE_URL}/billing/", json=data)
            if response.status_code == 201:
                messagebox.showinfo("Success", "Billing record added successfully.")
                add_win.destroy()
            else:
                messagebox.showerror("Error", "Failed to add billing record.")

        ttk.Button(add_win, text="Submit", command=submit).pack(pady=10)

    elif schema == "Nurses":
        add_win = tk.Toplevel()
        add_win.title("Add Nurse")

        labels = ["Nurse ID", "Name"]
        entries = []

        for label in labels:
            ttk.Label(add_win, text=label).pack()
            entry = ttk.Entry(add_win)
            entry.pack()
            entries.append(entry)

        def submit():
            data = {
                "nurseID": entries[0].get(),
                "name": entries[1].get(),
            }
            response = requests.post(f"{BASE_URL}/nurses/", json=data)
            if response.status_code == 201:
                messagebox.showinfo("Success", "Nurse added successfully.")
                add_win.destroy()
            else:
                messagebox.showerror("Error", "Failed to add nurse.")

        ttk.Button(add_win, text="Submit", command=submit).pack(pady=10)

    elif schema == "Staff":
        add_win = tk.Toplevel()
        add_win.title("Add Staff")

        labels = ["Staff ID", "Name", "Role"]
        entries = []

        for label in labels:
            ttk.Label(add_win, text=label).pack()
            entry = ttk.Entry(add_win)
            entry.pack()
            entries.append(entry)

        def submit():
            data = {
                "staffID": entries[0].get(),
                "name": entries[1].get(),
                "role": entries[2].get()
            }
            response = requests.post(f"{BASE_URL}/staff/", json=data)
            if response.status_code == 201:
                messagebox.showinfo("Success", "Staff added successfully.")
                add_win.destroy()
            else:
                messagebox.showerror("Error", "Failed to add staff.")

        ttk.Button(add_win, text="Submit", command=submit).pack(pady=10)


def remove_record(schema):
    if schema == "Patients":
        rm_win = tk.Toplevel()
        rm_win.title("Remove Patient")

        ttk.Label(rm_win, text="Enter Patient ID to remove:").pack()
        id_entry = ttk.Entry(rm_win)
        id_entry.pack()

        def submit():
            patient_id = id_entry.get()
            response = requests.delete(f"{BASE_URL}/patients/{patient_id}")
            if response.status_code == 200:
                messagebox.showinfo("Success", "Patient removed.")
                rm_win.destroy()
            else:
                messagebox.showerror("Error", "Failed to remove patient.")

        ttk.Button(rm_win, text="Submit", command=submit).pack(pady=10)

    elif schema == "Physicians":
        rm_win = tk.Toplevel()
        rm_win.title("Remove Physician")

        ttk.Label(rm_win, text="Enter Physician ID to remove:").pack()
        id_entry = ttk.Entry(rm_win)
        id_entry.pack()

        def submit():
            physician_id = id_entry.get()
            response = requests.delete(f"{BASE_URL}/physicians/{physician_id}")
            if response.status_code == 200:
                messagebox.showinfo("Success", "Physician removed.")
                rm_win.destroy()
            else:
                messagebox.showerror("Error", "Failed to remove physician.")

        ttk.Button(rm_win, text="Submit", command=submit).pack(pady=10)

    elif schema == "Appointments":
        rm_win = tk.Toplevel()
        rm_win.title("Remove Appointment")

        ttk.Label(rm_win, text="Enter Appointment ID to remove:").pack()
        id_entry = ttk.Entry(rm_win)
        id_entry.pack()

        def submit():
            appointment_id = id_entry.get()
            response = requests.delete(f"{BASE_URL}/appointments/{appointment_id}")
            if response.status_code == 200:
                messagebox.showinfo("Success", "Appointment removed.")
                rm_win.destroy()
            else:
                messagebox.showerror("Error", "Failed to remove appointment.")

        ttk.Button(rm_win, text="Submit", command=submit).pack(pady=10)

    elif schema == "MedicalRecords":
        rm_win = tk.Toplevel()
        rm_win.title("Remove Medical Record")

        ttk.Label(rm_win, text="Enter Record ID to remove:").pack()
        id_entry = ttk.Entry(rm_win)
        id_entry.pack()

        def submit():
            record_id = id_entry.get()
            response = requests.delete(f"{BASE_URL}/medical-records/{record_id}")
            if response.status_code == 200:
                messagebox.showinfo("Success", "Medical record removed.")
                rm_win.destroy()
            else:
                messagebox.showerror("Error", "Failed to remove medical record.")

        ttk.Button(rm_win, text="Submit", command=submit).pack(pady=10)

    elif schema == "Prescriptions":
        rm_win = tk.Toplevel()
        rm_win.title("Remove Prescription")

        ttk.Label(rm_win, text="Enter Prescription ID to remove:").pack()
        id_entry = ttk.Entry(rm_win)
        id_entry.pack()

        def submit():
            prescription_id = id_entry.get()
            response = requests.delete(f"{BASE_URL}/prescriptions/{prescription_id}")
            if response.status_code == 200:
                messagebox.showinfo("Success", "Prescription removed.")
                rm_win.destroy()
            else:
                messagebox.showerror("Error", "Failed to remove prescription.")

        ttk.Button(rm_win, text="Submit", command=submit).pack(pady=10)

    elif schema == "LabTests":
        rm_win = tk.Toplevel()
        rm_win.title("Remove Lab Test")

        ttk.Label(rm_win, text="Enter Test ID to remove:").pack()
        id_entry = ttk.Entry(rm_win)
        id_entry.pack()

        def submit():
            test_id = id_entry.get()
            response = requests.delete(f"{BASE_URL}/lab-tests/{test_id}")
            if response.status_code == 200:
                messagebox.showinfo("Success", "Lab test removed.")
                rm_win.destroy()
            else:
                messagebox.showerror("Error", "Failed to remove lab test.")

        ttk.Button(rm_win, text="Submit", command=submit).pack(pady=10)

    elif schema == "Billing":
        rm_win = tk.Toplevel()
        rm_win.title("Remove Billing")

        ttk.Label(rm_win, text="Enter Billing ID to remove:").pack()
        id_entry = ttk.Entry(rm_win)
        id_entry.pack()

        def submit():
            billing_id = id_entry.get()
            response = requests.delete(f"{BASE_URL}/billing/{billing_id}")
            if response.status_code == 200:
                messagebox.showinfo("Success", "Billing record removed.")
                rm_win.destroy()
            else:
                messagebox.showerror("Error", "Failed to remove billing record.")

        ttk.Button(rm_win, text="Submit", command=submit).pack(pady=10)

    elif schema == "Nurses":
        rm_win = tk.Toplevel()
        rm_win.title("Remove Nurse")

        ttk.Label(rm_win, text="Enter Nurse ID to remove:").pack()
        id_entry = ttk.Entry(rm_win)
        id_entry.pack()

        def submit():
            nurse_id = id_entry.get()
            response = requests.delete(f"{BASE_URL}/nurses/{nurse_id}")
            if response.status_code == 200:
                messagebox.showinfo("Success", "Nurse removed.")
                rm_win.destroy()
            else:
                messagebox.showerror("Error", "Failed to remove nurse.")

        ttk.Button(rm_win, text="Submit", command=submit).pack(pady=10)

    elif schema == "Staff":
        rm_win = tk.Toplevel()
        rm_win.title("Remove Staff")

        ttk.Label(rm_win, text="Enter Staff ID to remove:").pack()
        id_entry = ttk.Entry(rm_win)
        id_entry.pack()

        def submit():
            staff_id = id_entry.get()
            response = requests.delete(f"{BASE_URL}/staff/{staff_id}")
            if response.status_code == 200:
                messagebox.showinfo("Success", "Staff removed.")
                rm_win.destroy()
            else:
                messagebox.showerror("Error", "Failed to remove staff.")

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
            response = requests.get(f"{BASE_URL}/patients/{patient_id}")
            if response.status_code == 200:
                p = response.json()
                info = f"ID: {p['patientID']}\nName: {p['name']}\nDOB: {p['dob']}\nAddress: {p['address']}\nPhone: {p['phone']}\nInsurance: {p['insurance']}"
                messagebox.showinfo("Patient Info", info)
            else:
                messagebox.showerror("Error", "Patient not found.")

        ttk.Button(search_win, text="Search", command=submit).pack(pady=10)

    elif schema == "Physicians":
        search_win = tk.Toplevel()
        search_win.title("Search Physician")

        ttk.Label(search_win, text="Enter Physician ID:").pack()
        id_entry = ttk.Entry(search_win)
        id_entry.pack()

        def submit():
            physician_id = id_entry.get()
            response = requests.get(f"{BASE_URL}/physicians/{physician_id}")
            if response.status_code == 200:
                p = response.json()
                info = f"ID: {p['physicianID']}\nName: {p['name']}\nSpecialty: {p['role']}"
                messagebox.showinfo("Physician Info", info)
            else:
                messagebox.showerror("Error", "Physician not found.")

        ttk.Button(search_win, text="Search", command=submit).pack(pady=10)

    elif schema == "Appointments":
        search_win = tk.Toplevel()
        search_win.title("Search Appointment")

        ttk.Label(search_win, text="Enter Appointment ID:").pack()
        id_entry = ttk.Entry(search_win)
        id_entry.pack()

        def submit():
            appointment_id = id_entry.get()
            response = requests.get(f"{BASE_URL}/appointments/{appointment_id}")
            if response.status_code == 200:
                a = response.json()
                info = f"ID: {a['appointmentID']}\nPatient ID: {a['patientID']}\nPhysician ID: {a['physicianID']}\nDate: {a['date']}\nTime: {a['time']}"
                messagebox.showinfo("Appointment Info", info)
            else:
                messagebox.showerror("Error", "Appointment not found.")

        ttk.Button(search_win, text="Search", command=submit).pack(pady=10)

    elif schema == "MedicalRecords":
        search_win = tk.Toplevel()
        search_win.title("Search Medical Record")

        ttk.Label(search_win, text="Enter Record ID:").pack()
        id_entry = ttk.Entry(search_win)
        id_entry.pack()

        def submit():
            record_id = id_entry.get()
            response = requests.get(f"{BASE_URL}/medical-records/{record_id}")
            if response.status_code == 200:
                m = response.json()
                info = f"ID: {m['recordID']}\nPatient ID: {m['patientID']}\nDate Created: {m['dateCreated']}\nAllergies: {m['allergies']}\nMedications: {m['medication']}\nDiagnoses: {m['diagnoses']}"
                messagebox.showinfo("Medical Record Info", info)
            else:
                messagebox.showerror("Error", "Medical record not found.")

        ttk.Button(search_win, text="Search", command=submit).pack(pady=10)

    elif schema == "Prescriptions":
        search_win = tk.Toplevel()
        search_win.title("Search Prescription")

        ttk.Label(search_win, text="Enter Prescription ID:").pack()
        id_entry = ttk.Entry(search_win)
        id_entry.pack()

        def submit():
            prescription_id = id_entry.get()
            response = requests.get(f"{BASE_URL}/prescriptions/{prescription_id}")
            if response.status_code == 200:
                p = response.json()
                info = f"ID: {p['prescriptionID']}\nPatient ID: {p['patientID']}\nPhysician ID: {p['physicianID']}\nMedication: {p['medication']}\nDosage: {p['dosage']}"
                messagebox.showinfo("Prescription Info", info)
            else:
                messagebox.showerror("Error", "Prescription not found.")

        ttk.Button(search_win, text="Search", command=submit).pack(pady=10)

    elif schema == "LabTests":
        search_win = tk.Toplevel()
        search_win.title("Search Lab Test")

        ttk.Label(search_win, text="Enter Test ID:").pack()
        id_entry = ttk.Entry(search_win)
        id_entry.pack()

        def submit():
            test_id = id_entry.get()
            response = requests.get(f"{BASE_URL}/lab-tests/{test_id}")
            if response.status_code == 200:
                l = response.json()
                info = f"ID: {l['testID']}\nPatient ID: {l['patientID']}\nTest Type: {l['testType']}\nResults: {l['results']}"
                messagebox.showinfo("Lab Test Info", info)
            else:
                messagebox.showerror("Error", "Lab test not found.")

        ttk.Button(search_win, text="Search", command=submit).pack(pady=10)

    elif schema == "Billing":
        search_win = tk.Toplevel()
        search_win.title("Search Billing")

        ttk.Label(search_win, text="Enter Billing ID:").pack()
        id_entry = ttk.Entry(search_win)
        id_entry.pack()

        def submit():
            billing_id = id_entry.get()
            response = requests.get(f"{BASE_URL}/billing/{billing_id}")
            if response.status_code == 200:
                b = response.json()
                info = f"ID: {b['billingID']}\nPatient ID: {b['patientID']}\nAmount Due: {b['amountDue']}\nDate Issued: {b['dateIssued']}"
                messagebox.showinfo("Billing Info", info)
            else:
                messagebox.showerror("Error", "Billing record not found.")

        ttk.Button(search_win, text="Search", command=submit).pack(pady=10)

    elif schema == "Nurses":
        search_win = tk.Toplevel()
        search_win.title("Search Nurse")

        ttk.Label(search_win, text="Enter Nurse ID:").pack()
        id_entry = ttk.Entry(search_win)
        id_entry.pack()

        def submit():
            nurse_id = id_entry.get()
            response = requests.get(f"{BASE_URL}/nurses/{nurse_id}")
            if response.status_code == 200:
                n = response.json()
                info = f"ID: {n['nurseID']}\nName: {n['name']}"
                messagebox.showinfo("Nurse Info", info)
            else:
                messagebox.showerror("Error", "Nurse not found.")

        ttk.Button(search_win, text="Search", command=submit).pack(pady=10)

    elif schema == "Staff":
        search_win = tk.Toplevel()
        search_win.title("Search Staff")

        ttk.Label(search_win, text="Enter Staff ID:").pack()
        id_entry = ttk.Entry(search_win)
        id_entry.pack()

        def submit():
            staff_id = id_entry.get()
            response = requests.get(f"{BASE_URL}/staff/{staff_id}")
            if response.status_code == 200:
                s = response.json()
                info = f"ID: {s['staffID']}\nName: {s['name']}\nRole: {s['role']}"
                messagebox.showinfo("Staff Info", info)
            else:
                messagebox.showerror("Error", "Staff not found.")

        ttk.Button(search_win, text="Search", command=submit).pack(pady=10)


def show_all(schema):
    if schema == "Patients":
        response = requests.get(f"{BASE_URL}/patients/")
        if response.status_code == 200:
            patients = response.json()
            output = "\n\n".join([
                f"ID: {p['patientID']}\nName: {p['name']}\nDOB: {p['dob']}\nPhone: {p['phone']}"
                for p in patients
            ])
            messagebox.showinfo("All Patients", output)
        else:
            messagebox.showerror("Error", "Could not retrieve patients.")

    elif schema == "Physicians":
        response = requests.get(f"{BASE_URL}/physicians/")
        if response.status_code == 200:
            physicians = response.json()
            output = "\n\n".join([
                f"ID: {p['physicianID']}\nName: {p['name']}\nSpecialty: {p['role']}"
                for p in physicians
            ])
            messagebox.showinfo("All Physicians", output)
        else:
            messagebox.showerror("Error", "Could not retrieve physicians.")

    elif schema == "Appointments":
        response = requests.get(f"{BASE_URL}/appointments/")
        if response.status_code == 200:
            appointments = response.json()
            output = "\n\n".join([
                f"ID: {a['appointmentID']}\nPatient ID: {a['patientID']}\nPhysician ID: {a['physicianID']}\nDate: {a['date']}\nTime: {a['time']}"
                for a in appointments
            ])
            messagebox.showinfo("All Appointments", output)
        else:
            messagebox.showerror("Error", "Could not retrieve appointments.")

    elif schema == "MedicalRecords":
        response = requests.get(f"{BASE_URL}/medical-records/")
        if response.status_code == 200:
            records = response.json()
            output = "\n\n".join([
                f"ID: {m['recordID']}\nPatient ID: {m['patientID']}\nDate Created: {m['dateCreated']}\nAllergies: {m['allergies']}\nMedications: {m['medication']}\nDiagnoses: {m['diagnoses']}"
                for m in records
            ])
            messagebox.showinfo("All Medical Records", output)
        else:
            messagebox.showerror("Error", "Could not retrieve medical records.")

    elif schema == "Prescriptions":
        response = requests.get(f"{BASE_URL}/prescriptions/")
        if response.status_code == 200:
            prescriptions = response.json()
            output = "\n\n".join([
                f"ID: {p['prescriptionID']}\nPatient ID: {p['patientID']}\nPhysician ID: {p['physicianID']}\nMedication: {p['medication']}\nDosage: {p['dosage']}"
                for p in prescriptions
            ])
            messagebox.showinfo("All Prescriptions", output)
        else:
            messagebox.showerror("Error", "Could not retrieve prescriptions.")

    elif schema == "LabTests":
        response = requests.get(f"{BASE_URL}/lab-tests/")
        if response.status_code == 200:
            lab_tests = response.json()
            output = "\n\n".join([
                f"ID: {l['testID']}\nPatient ID: {l['patientID']}\nTest Type: {l['testType']}\nResults: {l['results']}"
                for l in lab_tests
            ])
            messagebox.showinfo("All Lab Tests", output)
        else:
            messagebox.showerror("Error", "Could not retrieve lab tests.")

    elif schema == "Billing":
        response = requests.get(f"{BASE_URL}/billing/")
        if response.status_code == 200:
            billing = response.json()
            output = "\n\n".join([
                f"ID: {b['billingID']}\nPatient ID: {b['patientID']}\nAmount Due: {b['amountDue']}\nDate Issued: {b['dateIssued']}"
                for b in billing
            ])
            messagebox.showinfo("All Billing Records", output)
        else:
            messagebox.showerror("Error", "Could not retrieve billing records.")

    elif schema == "Nurses":
        response = requests.get(f"{BASE_URL}/nurses/")
        if response.status_code == 200:
            nurses = response.json()
            output = "\n\n".join([
                f"ID: {n['nurseID']}\nName: {n['name']}"
                for n in nurses
            ])
            messagebox.showinfo("All Nurses", output)
        else:
            messagebox.showerror("Error", "Could not retrieve nurses.")

    elif schema == "Staff":
        response = requests.get(f"{BASE_URL}/staff/")
        if response.status_code == 200:
            staff = response.json()
            output = "\n\n".join([
                f"ID: {s['staffID']}\nName: {s['name']}\nRole: {s['role']}"
                for s in staff
            ])
            messagebox.showinfo("All Staff", output)
        else:
            messagebox.showerror("Error", "Could not retrieve staff.")


def update(schema):
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
            patient_id = id_entry.get()
            data = {
                "name": entries[0].get(),
                "dob": entries[1].get(),
                "address": entries[2].get(),
                "phone": entries[3].get(),
                "insurance": entries[4].get()
            }
            response = requests.put(f"{BASE_URL}/patients/{patient_id}", json=data)
            if response.status_code == 200:
                messagebox.showinfo("Success", "Patient updated.")
                upd_win.destroy()
            else:
                messagebox.showerror("Error", "Failed to update patient.")

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
            physician_id = id_entry.get()
            data = {
                "name": entries[0].get(),
                "role": entries[1].get()
            }
            response = requests.put(f"{BASE_URL}/physicians/{physician_id}", json=data)
            if response.status_code == 200:
                messagebox.showinfo("Success", "Physician updated.")
                upd_win.destroy()
            else:
                messagebox.showerror("Error", "Failed to update physician.")

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
            appointment_id = id_entry.get()
            data = {
                "patientID": entries[0].get(),
                "physicianID": entries[1].get(),
                "date": entries[2].get(),
                "time": entries[3].get()
            }
            response = requests.put(f"{BASE_URL}/appointments/{appointment_id}", json=data)
            if response.status_code == 200:
                messagebox.showinfo("Success", "Appointment updated.")
                upd_win.destroy()
            else:
                messagebox.showerror("Error", "Failed to update appointment.")

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
            record_id = id_entry.get()
            data = {
                "patientID": entries[0].get(),
                "dateCreated": entries[1].get(),
                "allergies": entries[2].get(),
                "medication": entries[3].get(),
                "diagnoses": entries[4].get()
            }
            response = requests.put(f"{BASE_URL}/medical-records/{record_id}", json=data)
            if response.status_code == 200:
                messagebox.showinfo("Success", "Medical record updated.")
                upd_win.destroy()
            else:
                messagebox.showerror("Error", "Failed to update medical record.")

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
            prescription_id = id_entry.get()
            data = {
                "patientID": entries[0].get(),
                "physicianID": entries[1].get(),
                "medication": entries[2].get(),
                "dosage": entries[3].get()
            }
            response = requests.put(f"{BASE_URL}/prescriptions/{prescription_id}", json=data)
            if response.status_code == 200:
                messagebox.showinfo("Success", "Prescription updated.")
                upd_win.destroy()
            else:
                messagebox.showerror("Error", "Failed to update prescription.")

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
            test_id = id_entry.get()
            data = {
                "patientID": entries[0].get(),
                "testType": entries[1].get(),
                "results": entries[2].get()
            }
            response = requests.put(f"{BASE_URL}/lab-tests/{test_id}", json=data)
            if response.status_code == 200:
                messagebox.showinfo("Success", "Lab test updated.")
                upd_win.destroy()
            else:
                messagebox.showerror("Error", "Failed to update lab test.")

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
            billing_id = id_entry.get()
            data = {
                "patientID": entries[0].get(),
                "amountDue": entries[1].get(),
                "dateIssued": entries[2].get()
            }
            response = requests.put(f"{BASE_URL}/billing/{billing_id}", json=data)
            if response.status_code == 200:
                messagebox.showinfo("Success", "Billing record updated.")
                upd_win.destroy()
            else:
                messagebox.showerror("Error", "Failed to update billing record.")

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
            nurse_id = id_entry.get()
            data = {
                "name": entries[0].get()
            }
            response = requests.put(f"{BASE_URL}/nurses/{nurse_id}", json=data)
            if response.status_code == 200:
                messagebox.showinfo("Success", "Nurse updated.")
                upd_win.destroy()
            else:
                messagebox.showerror("Error", "Failed to update nurse.")

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
            staff_id = id_entry.get()
            data = {
                "name": entries[0].get(),
                "role": entries[1].get()
            }
            response = requests.put(f"{BASE_URL}/staff/{staff_id}", json=data)
            if response.status_code == 200:
                messagebox.showinfo("Success", "Staff updated.")
                upd_win.destroy()
            else:
                messagebox.showerror("Error", "Failed to update staff.")

        ttk.Button(upd_win, text="Update", command=submit).pack(pady=10)


def search_by_specialty():
    search_win = tk.Toplevel()
    search_win.title("Search Physician by Specialty")

    ttk.Label(search_win, text="Enter Specialty:").pack()
    id_entry = ttk.Entry(search_win)
    id_entry.pack()

    def submit():
        specialty = id_entry.get()
        response = requests.get(f"{BASE_URL}/staff/{specialty}")
        if response.status_code == 200:
            physicians = response.json()
            output = "\n\n".join([
                f"ID: {p['physicianID']}\nName: {p['name']}\nSpecialty: {p['role']}"
                for p in physicians
            ])
            messagebox.showinfo("All {specialty} Physicians", output)
        else:
            messagebox.showerror("Error", "Staff not found.")

    ttk.Button(search_win, text="Search", command=submit).pack(pady=10)


def show_all_w_patient_info(schema):
    if schema == "MedicalRecords":
        response = requests.get(f"{BASE_URL}/medical-records/with-patient-info/")
        if response.status_code == 200:
            records = response.json()
            output = "\n\n".join([
                f"ID: {m['recordID']}\nPatient ID: {m['patientID']}\nDate Created: {m['dateCreated']}\nAllergies: {m['allergies']}\nMedications: {m['medication']}\nDiagnoses: {m['diagnoses']}\nName: {m['name']}\nDOB: {m['dob']}\nPhone: {m['phone']}"
                for m in records
            ])
            messagebox.showinfo("All Medical Records With Patient Info", output)
        else:
            messagebox.showerror("Error", "Could not retrieve medical records.")

    elif schema == "LabTests":
        response = requests.get(f"{BASE_URL}/lab-tests/with-patient/")
        if response.status_code == 200:
            lab_tests = response.json()
            output = "\n\n".join([
                f"ID: {l['testID']}\nPatient ID: {l['patientID']}\nTest Type: {l['testType']}\nResults: {l['results']}\nName: {l['name']}\nDOB: {l['dob']}\nPhone: {l['phone']}"
                for l in lab_tests
            ])
            messagebox.showinfo("All Lab Tests With Patient Info", output)
        else:
            messagebox.showerror("Error", "Could not retrieve lab tests.")

    elif schema == "Billing":
        response = requests.get(f"{BASE_URL}/billing/with-patient/")
        if response.status_code == 200:
            billing = response.json()
            output = "\n\n".join([
                f"ID: {b['billingID']}\nPatient ID: {b['patientID']}\nAmount Due: {b['amountDue']}\nDate Issued: {b['dateIssued']}\nName: {b['name']}\nDOB: {b['dob']}\nPhone: {b['phone']}"
                for b in billing
            ])
            messagebox.showinfo("All Billing Records With Patient Info", output)
        else:
            messagebox.showerror("Error", "Could not retrieve billing records.")


def search_by_other(schema, other_schema):
    if schema == "MedicalRecords":
        search_win = tk.Toplevel()
        search_win.title("Search Medical Record By Patient")

        ttk.Label(search_win, text="Enter Patient ID:").pack()
        id_entry = ttk.Entry(search_win)
        id_entry.pack()

        def submit():
            patient_id = id_entry.get()
            response = requests.get(f"{BASE_URL}/medical-records/patient/{patient_id}")
            if response.status_code == 200:
                m = response.json()
                info = f"ID: {m['recordID']}\nPatient ID: {m['patientID']}\nDate Created: {m['dateCreated']}\nAllergies: {m['allergies']}\nMedications: {m['medication']}\nDiagnoses: {m['diagnoses']}"
                messagebox.showinfo("Medical Record Info", info)
            else:
                messagebox.showerror("Error", "Patient not found.")

        ttk.Button(search_win, text="Search", command=submit).pack(pady=10)

    elif schema == "Appointments":
        if other_schema == "Patients":
            search_win = tk.Toplevel()
            search_win.title("Search Appointment By Patient")

            ttk.Label(search_win, text="Enter Patient ID:").pack()
            id_entry = ttk.Entry(search_win)
            id_entry.pack()

            def submit():
                patient_id = id_entry.get()
                response = requests.get(f"{BASE_URL}/appointments/patient/{patient_id}")
                if response.status_code == 200:
                    a = response.json()
                    info = f"ID: {a['appointmentID']}\nPatient ID: {a['patientID']}\nPhysician ID: {a['physicianID']}\nDate: {a['date']}\nTime: {a['time']}"
                    messagebox.showinfo("Appointment Info", info)
                else:
                    messagebox.showerror("Error", "Patient not found.")

            ttk.Button(search_win, text="Search", command=submit).pack(pady=10)

        elif other_schema == "Physicians":
            search_win = tk.Toplevel()
            search_win.title("Search Appointment By Physician")

            ttk.Label(search_win, text="Enter Physician ID:").pack()
            id_entry = ttk.Entry(search_win)
            id_entry.pack()

            def submit():
                physician_id = id_entry.get()
                response = requests.get(f"{BASE_URL}/appointments/physician/{physician_id}")
                if response.status_code == 200:
                    a = response.json()
                    info = f"ID: {a['appointmentID']}\nPatient ID: {a['patientID']}\nPhysician ID: {a['physicianID']}\nDate: {a['date']}\nTime: {a['time']}"
                    messagebox.showinfo("Appointment Info", info)
                else:
                    messagebox.showerror("Error", "Physician not found.")

            ttk.Button(search_win, text="Search", command=submit).pack(pady=10)

    elif schema == "Prescriptions":
        if other_schema == "Patients":
            search_win = tk.Toplevel()
            search_win.title("Search Prescription By Patient")

            ttk.Label(search_win, text="Enter Patient ID:").pack()
            id_entry = ttk.Entry(search_win)
            id_entry.pack()

            def submit():
                patient_id = id_entry.get()
                response = requests.get(f"{BASE_URL}/prescriptions/patient/{patient_id}")
                if response.status_code == 200:
                    p = response.json()
                    info = f"ID: {p['prescriptionID']}\nPatient ID: {p['patientID']}\nPhysician ID: {p['physicianID']}\nMedication: {p['medication']}\nDosage: {p['dosage']}"
                    messagebox.showinfo("Prescription Info", info)
                else:
                    messagebox.showerror("Error", "Patient not found.")

            ttk.Button(search_win, text="Search", command=submit).pack(pady=10)

        elif other_schema == "Physicians":
            search_win = tk.Toplevel()
            search_win.title("Search Prescription By Physician")

            ttk.Label(search_win, text="Enter Physician ID:").pack()
            id_entry = ttk.Entry(search_win)
            id_entry.pack()

            def submit():
                physician_id = id_entry.get()
                response = requests.get(f"{BASE_URL}/prescriptions/physician/{physician_id}")
                if response.status_code == 200:
                    p = response.json()
                    info = f"ID: {p['prescriptionID']}\nPatient ID: {p['patientID']}\nPhysician ID: {p['physicianID']}\nMedication: {p['medication']}\nDosage: {p['dosage']}"
                    messagebox.showinfo("Prescription Info", info)
                else:
                    messagebox.showerror("Error", "Physician not found.")

            ttk.Button(search_win, text="Search", command=submit).pack(pady=10)

    elif schema == "LabTests":
        search_win = tk.Toplevel()
        search_win.title("Search Lab Test By Patient")

        ttk.Label(search_win, text="Enter Patient ID:").pack()
        id_entry = ttk.Entry(search_win)
        id_entry.pack()

        def submit():
            patient_id = id_entry.get()
            response = requests.get(f"{BASE_URL}/lab-tests/patient/{patient_id}")
            if response.status_code == 200:
                l = response.json()
                info = f"ID: {l['testID']}\nPatient ID: {l['patientID']}\nTest Type: {l['testType']}\nResults: {l['results']}"
                messagebox.showinfo("Lab Test Info", info)
            else:
                messagebox.showerror("Error", "Patient not found.")

        ttk.Button(search_win, text="Search", command=submit).pack(pady=10)

    elif schema == "Billing":
        search_win = tk.Toplevel()
        search_win.title("Search Billing By Patient")

        ttk.Label(search_win, text="Enter Patient ID:").pack()
        id_entry = ttk.Entry(search_win)
        id_entry.pack()

        def submit():
            patient_id = id_entry.get()
            response = requests.get(f"{BASE_URL}/billing/patient/{patient_id}")
            if response.status_code == 200:
                b = response.json()
                info = f"ID: {b['billingID']}\nPatient ID: {b['patientID']}\nAmount Due: {b['amountDue']}\nDate Issued: {b['dateIssued']}"
                messagebox.showinfo("Billing Info", info)
            else:
                messagebox.showerror("Error", "Patient not found.")

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

        response = requests.patch(
            f"{BASE_URL}/medical-records/{record_id}/add-diagnosis",
            json={"diagnosis": diagnosis}
        )

        if response.status_code == 200:
            messagebox.showinfo("Success", "Diagnosis added successfully.")
            diag_win.destroy()
        else:
            messagebox.showerror("Error", "Failed to add diagnosis.")

    ttk.Button(diag_win, text="Submit", command=submit).pack(pady=10)


def show_all_w_details():
    response = requests.get(f"{BASE_URL}/prescriptions/with-details/")
    if response.status_code == 200:
        prescriptions = response.json()
        output = "\n\n".join([
            f"ID: {p['prescriptionID']}\nPatient ID: {p['patientID']}\nPhysician ID: {p['physicianID']}\nMedication: {p['medication']}\nDosage: {p['dosage']}\nPatient Name: {p['patient_name']}\nDOB: {p['dob']}\nPhone: {p['phone']}\nPhysician Name: {p['physician_name']}\nSpecialty: {p['role']}"
            for p in prescriptions
        ])
        messagebox.showinfo("All Prescriptions With Details", output)
    else:
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

        response = requests.patch(
            f"{BASE_URL}/lab-tests/{test_id}/update-results",
            json={"results": results}
        )

        if response.status_code == 200:
            messagebox.showinfo("Success", "Lab results updated.")
            update_win.destroy()
        else:
            messagebox.showerror("Error", "Failed to update results.")

    ttk.Button(update_win, text="Submit", command=submit).pack(pady=10)


def calculate_billing_total():
    search_win = tk.Toplevel()
    search_win.title("Calculate Total Amount Due for Patient")

    ttk.Label(search_win, text="Enter Patient ID:").pack()
    id_entry = ttk.Entry(search_win)
    id_entry.pack()

    def submit():
        patient_id = id_entry.get()
        response = requests.get(f"{BASE_URL}/billing/patient/{patient_id}/total")
        if response.status_code == 200:
            b = response.json()
            info = f"Total: {b['total']}"
            messagebox.showinfo("Billing Info", info)
        else:
            messagebox.showerror("Error", "Patient not found.")

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
        ttk.Button(sub_window, text="Search By Specialty", command=lambda: search_by_specialty()).pack(pady=5)

    elif schema == "MedicalRecords":
        ttk.Button(sub_window, text="Show all with Patient Info", command=lambda: show_all_w_patient_info(schema)).pack(
            pady=5)
        ttk.Button(sub_window, text="Search by Patient ID", command=lambda: search_by_other(schema, "Patients")).pack(
            pady=5)
        ttk.Button(sub_window, text="Add Diagnosis", command=lambda: add_diagnosis()).pack(pady=5)

    elif schema == "Appointments":
        ttk.Button(sub_window, text="Search by Patient ID", command=lambda: search_by_other(schema, "Patients")).pack(
            pady=5)
        ttk.Button(sub_window, text="Search by Physician ID",
                   command=lambda: search_by_other(schema, "Physicians")).pack(pady=5)

    elif schema == "Prescriptions":
        ttk.Button(sub_window, text="Show All With Details", command=lambda: show_all_w_details()).pack(pady=5)
        ttk.Button(sub_window, text="Search by Patient ID", command=lambda: search_by_other(schema, "Patients")).pack(
            pady=5)
        ttk.Button(sub_window, text="Search by Physician ID",
                   command=lambda: search_by_other(schema, "Physicians")).pack(pady=5)

    elif schema == "LabTests":
        ttk.Button(sub_window, text="Show all with Patient Info", command=lambda: show_all_w_patient_info(schema)).pack(
            pady=5)
        ttk.Button(sub_window, text="Search by Patient ID", command=lambda: search_by_other(schema, "Patients")).pack(
            pady=5)
        ttk.Button(sub_window, text="Update Lab Test Results", command=lambda: update_results()).pack(pady=5)

    elif schema == "Billing":
        ttk.Button(sub_window, text="Show all with Patient Info", command=lambda: show_all_w_patient_info(schema)).pack(
            pady=5)
        ttk.Button(sub_window, text="Search by Patient ID", command=lambda: search_by_other(schema, "Patients")).pack(
            pady=5)
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
