# Created by Ryan Polasky - 5/8/25

import time
import multiprocessing

from frontend import main_gui
from main import run_backend, read_root


def start_backend_server():
    print("Backend process: Starting server...")
    run_backend()


def test_program():
    """
    This is the simplest way to test the program, as it runs both the frontend & backend for you automatically
    """
    print("Starting backend in a separate process...")
    backend_process = multiprocessing.Process(target=start_backend_server)
    backend_process.start()

    print("Giving backend 3 seconds to start...")
    time.sleep(3)  # Wait for the backend process to hopefully initialize

    print("Checking backend status...")
    try:
        # This call should attempt to connect to the backend & database
        results = read_root()
        print(f"Backend status check result: {results}")

        if results and results.get("status") == "success":
            print("Backend/database check successful. Launching frontend GUI...")
            main_gui()
            print("Frontend GUI closed. Exiting test program...")
            backend_process.terminate()
            exit(1)
        else:
            print(
                f"Backend status is not 'success': {results.get('status') if results else 'None'}. Exiting...")
            backend_process.terminate()
            exit(-1)

    except Exception as e:
        print(f"Error during backend status check: {e}")
        print("Could not confirm backend status. Exiting...")
        backend_process.terminate()
        exit(-1)


if __name__ == "__main__":
    test_program()
