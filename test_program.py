# Created by Ryan Polasky - 5/8/25

import time
import multiprocessing
import sys
import requests

from main import run_backend, read_root


def start_backend_server():
    print("Backend process: Starting server...")
    run_backend()


def test_program():
    """
    This program asks the user to choose which frontend to launch: staff or patient.
    It runs the backend in a separate process, then launches the appropriate frontend.
    """
    print("Starting backend in a separate process...")
    backend_process = multiprocessing.Process(target=start_backend_server)
    backend_process.start()

    print("Giving backend 3 seconds to start...")
    time.sleep(3)  # Wait for the backend process to hopefully initialize

    print("Checking backend status...")
    try:
        # Use the FastAPI root function directly; if it fails, use requests as a fallback
        try:
            results = read_root()
        except Exception:
            # Try over HTTP (if run_backend uses reload, the code path is different)
            try:
                results = requests.get("http://localhost:8000/").json()
            except Exception as req_err:
                print(f"HTTP backend check also failed: {req_err}")
                results = None

        print(f"Backend status check result: {results}")

        if results and results.get("status") == "success":
            print("\n=== Choose frontend ===")
            print("1. Staff (admin) interface")
            print("2. Patient interface")
            print("q. Quit\n")
            while True:
                choice = input("Select an option (1/2/q): ").strip().lower()
                if choice in ("q", "quit"):
                    print("Quitting...")
                    backend_process.terminate()
                    sys.exit(0)
                elif choice == "1":
                    print("Launching Staff (admin) interface...")
                    from frontend import main_gui
                    main_gui()
                    break
                elif choice == "2":
                    patient_id = None
                    while patient_id is None:
                        pid = input("Enter Patient ID: ").strip()
                        if pid.isdigit():
                            patient_id = pid
                        else:
                            print("Invalid Patient ID (must be numeric). Try again.")
                    print(f"Launching Patient interface for Patient ID {patient_id}...")
                    from patient_frontend import main_gui as patient_main_gui
                    patient_main_gui(patient_id)
                    break
                else:
                    print("Invalid option. Please enter 1, 2, or q.")

            print("Frontend GUI closed. Exiting test program...")
            backend_process.terminate()
            sys.exit(0)
        else:
            print(f"Backend status is not 'success': {results.get('status') if results else 'None'}. Exiting...")
            backend_process.terminate()
            sys.exit(-1)

    except Exception as e:
        print(f"Error during backend status check: {e}")
        print("Could not confirm backend status. Exiting...")
        backend_process.terminate()
        sys.exit(-1)


if __name__ == "__main__":
    test_program()
