# Created by Louis Seelbach - 5/13/25

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog
import requests

BASE_URL = "http://localhost:8000"


def display_info(patient_id):
    response = requests.get(f"{BASE_URL}/patients/{patient_id}")
    if response.status_code == 200:
        p = response.json()
        info = f"ID: {p['patientid']}\nName: {p['name']}\nDOB: {p['dob']}\nAddress: {p['address']}\nPhone: {p['phone']}\nInsurance: {p['insurance']}"
        messagebox.showinfo("Patient Info", info)
    else:
        messagebox.showerror("Error",
                             "Patient not found.")  # This should never be shown, unless something goes wrong with the database


def display_medical(patient_id):
    response = requests.get(f"{BASE_URL}/medical-records/patient/{patient_id}")
    if response.status_code == 200:
        m = response.json()
        info = f"ID: {m['recordid']}\nPatient ID: {m['patientid']}\nDate Created: {m['dateCreated']}\nAllergies: {m['allergies']}\nMedications: {m['medication']}\nDiagnoses: {m['diagnoses']}"
        messagebox.showinfo("Medical Record Info", info)
    else:
        messagebox.showerror("Error", "Patient not found.")


def display_prescriptions(patient_id):
    response = requests.get(f"{BASE_URL}/prescriptions/patient/{patient_id}")
    if response.status_code == 200:
        p = response.json()
        info = f"ID: {p['prescriptionid']}\nPatient ID: {p['patientid']}\nPhysician ID: {p['physicianid']}\nMedication: {p['medication']}\nDosage: {p['dosage']}"
        messagebox.showinfo("Prescription Info", info)
    else:
        messagebox.showerror("Error", "Patient not found.")


def display_appointments(patient_id):
    response = requests.get(f"{BASE_URL}/appointments/patient/{patient_id}")
    if response.status_code == 200:
        a = response.json()
        info = f"ID: {a['appointmentid']}\nPatient ID: {a['patientid']}\nPhysician ID: {a['physicianid']}\nDate: {a['date']}\nTime: {a['time']}"
        messagebox.showinfo("Appointment Info", info)
    else:
        messagebox.showerror("Error", "Patient not found.")


def display_lab_tests(patient_id):
    response = requests.get(f"{BASE_URL}/lab-tests/patient/{patient_id}")
    if response.status_code == 200:
        l = response.json()
        info = f"ID: {l['testid']}\nPatient ID: {l['patientid']}\nTest Type: {l['testType']}\nResults: {l['results']}"
        messagebox.showinfo("Lab Test Info", info)
    else:
        messagebox.showerror("Error", "Patient not found.")


def display_billing(patient_id):
    response = requests.get(f"{BASE_URL}/billing/patient/{patient_id}")
    if response.status_code == 200:
        b = response.json()
        info = f"ID: {b['billingid']}\nPatient ID: {b['patientid']}\nAmount Due: {b['amountDue']}\nDate Issued: {b['dateIssued']}"
        messagebox.showinfo("Billing Info", info)
    else:
        messagebox.showerror("Error", "Patient not found.")


def display_billing_total(patient_id):
    response = requests.get(f"{BASE_URL}/billing/patient/{patient_id}/total")
    if response.status_code == 200:
        b = response.json()
        info = f"Total: {b['total']}"
        messagebox.showinfo("Billing Total", info)
    else:
        messagebox.showerror("Error", "Patient not found.")


# Main GUI                                                                                                                       
def main_gui(patient_id):
    response = requests.get(f"{BASE_URL}/patients/{patient_id}")
    if response.status_code != 200:
        messagebox.showerror("Error", "Patient not found.")
        return

    root = tk.Tk()
    root.title("Medical System Patient Interface")
    root.geometry("400x600")

    ttk.Label(root, text="Medical System Patient Menu", font=("Arial", 18)).pack(pady=20)

    ttk.Button(root, text="Display Information", width=30, command=lambda p=patient_id: display_info(p)).pack(pady=5)
    ttk.Button(root, text="Display Medical Records", width=30, command=lambda p=patient_id: display_medical(p)).pack(
        pady=5)
    ttk.Button(root, text="Display Prescriptions", width=30,
               command=lambda p=patient_id: display_prescriptions(p)).pack(pady=5)
    ttk.Button(root, text="Display Appointments", width=30, command=lambda p=patient_id: display_appointments(p)).pack(
        pady=5)
    ttk.Button(root, text="Display Lab Tests", width=30, command=lambda p=patient_id: display_lab_tests(p)).pack(pady=5)
    ttk.Button(root, text="Display Billing Info", width=30, command=lambda p=patient_id: display_billing(p)).pack(
        pady=5)
    ttk.Button(root, text="Display Billing Total", width=30,
               command=lambda p=patient_id: display_billing_total(p)).pack(pady=5)

    root.mainloop()


if __name__ == "__main__":
    main_gui(simpledialog.askstring("Patient ID", "Enter Patient ID:"))
