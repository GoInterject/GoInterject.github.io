import os
import logging

def pytest_configure():
    # Define paths to log files in the test directory
    base_dir = os.path.dirname(__file__)  # This points to the 'test' directory if conftest.py is there
    error_log_path = os.path.join(base_dir, "logs", "error_log.log")
    test_log_path = os.path.join(base_dir, "logs", "test_log.log")

    # Delete logs at the start of the session to ensure fresh logs
    for log_file in [error_log_path, test_log_path]:
        if os.path.exists(log_file):
            try:
                os.remove(log_file)
                print(f"Cleared log file: {log_file}")
            except OSError as e:
                print(f"Error clearing {log_file}: {e}")

    # Set up logging for error logs
    error_handler = logging.FileHandler(error_log_path)
    error_handler.setLevel(logging.ERROR)
    
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    error_handler.setFormatter(formatter)

    # Attach the error handler to the root logger
    logger = logging.getLogger()
    logger.addHandler(error_handler)
    logger.propagate = False
