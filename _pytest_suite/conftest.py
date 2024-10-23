import logging

# Add this in a conftest.py or your test code for additional error logging
def pytest_configure():
    error_handler = logging.FileHandler('_pytest_suite/error_log.log')
    error_handler.setLevel(logging.ERROR)
    
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    error_handler.setFormatter(formatter)

    # Get the root logger and add the error-specific handler
    logger = logging.getLogger()
    logger.addHandler(error_handler)

    # Optionally, prevent duplicated logs in the console by disabling propagation
    logger.propagate = False
    