# PYTEST TO VALIDATE ALL LINKS IN THE DOC FOLDERS
# ---------------------------------------------------------------
# Uses the front matter in `front_matter.yaml` as a base
# If this file is not found, it will extract the front matter using `extract_front_matter()`
# Iterates through the front matter and validate links:
# Headings: Checks if the heading exists in the doc page
# Doc Page: Checks if the doc page exists
# Images: Checks if the image exists in the correct location
# Links: Checks if the link exists:
#   Doc page link: Checks if the doc page exists
#   Heading link: Check if the heading exists for the doc page
#   URL: Check if the URL is valid

# BE SURE TO SET THE CONFIG VARIABLES IN `config.py`
# ---------------------------------------------------------------

import os
import logging
import requests
import yaml
import re
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import ROOT_FOLDER
from utils.doc_page_folder_list import PageDirectories
from utils.utilities import convert_filepath_to_url
from extraction.extract_front_matter import extract_front_matter_from_all_pages

# ---------------------------------------------------------------
# GLOBALS
# ---------------------------------------------------------------
logger = logging.getLogger(__name__)
global_headings_dict = {}
global_front_matter = {}

num_files_checked = 0
num_file_errors = 0
num_errors_url = 0
num_errors_images = 0
num_errors_files = 0
num_errors_headings = 0

CHECK_IMAGES = True
CHECK_FILES = True
CHECK_HEADINGS = True # Headings will not be check if CHECK_FILES = False
CHECK_FILES_IN_LINKS = True
CHECK_HEADINGS_IN_LINKS = True # Headings in links will not be check if CHECK_FILES_IN_LINKS = False
CHECK_URL_LINKS = True

DOMAINS_TO_SKIP = ["github.com"] # domains to skip in the URL verification process

# ---------------------------------------------------------------
# METHODS
# ---------------------------------------------------------------
def convert_heading_to_anchor(heading: str) -> str:
    """
    Convert a heading string into a Jekyll-style anchor link.

    Args:
        heading (str): The heading text to convert.

    Returns:
        str: The anchor link formatted for Jekyll.
    """
    anchor = heading.lower() # Convert to lowercase
    anchor = anchor.replace(" ", "-") # Replace spaces with hyphens
    anchor = re.sub(r'[^\w\-]', '', anchor)  # Remove non-alphanumeric characters except for hyphens
    
    return anchor

# ---------------------------------------------------------------
def get_yaml_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return yaml.safe_load(file)

# ---------------------------------------------------------------
def verify_links(root_folder):
    global num_files_checked
    global num_file_errors
    test_results = True

    for file_path, front_matter in global_front_matter.items():
        results_images_test = True
        results_links_test = True
        num_files_checked = num_files_checked + 1
        logger.info(f" Checking Links in: {file_path}")
        links = front_matter.get("links", [])
        image_dir = front_matter.get("image_dir", "error")
        images = front_matter.get("images", [])
        headings = front_matter.get("headings", [])

        if CHECK_IMAGES:
            results_images_test = verify_images_in_file(root_folder, file_path, image_dir, images)
            if results_images_test is False:
                test_results = False
                num_file_errors = num_file_errors + 1
        results_links_test = verify_links_in_file(root_folder, file_path, links, headings)
        if results_links_test is False:
            test_results = False
            if results_images_test:
                num_file_errors = num_file_errors + 1

    return test_results

# ---------------------------------------------------------------
def verify_images_in_file(root_folder, file_path, image_dir, images) -> bool:
    global num_errors_images
    file_test_results = True

    if not image_dir:
        pass
    elif image_dir == "error":
        logger.error(f"FRONT_MATTER: 'image_dir' key is missing from {file_path}")
        num_errors_images = num_errors_images + 1
    else:
        for image in images:
            file_name = image.get("file")
            image_type = image.get("type")
            image_link = os.path.join(root_folder, "images", image_dir, f"{file_name}.{image_type}")
            if os.path.exists(image_link):
                pass
            else:
                logger.error(f"IMAGE NOT FOUND: {image_link} does not exist in: {file_path}")
                num_errors_images = num_errors_images + 1
                file_test_results = False
    return file_test_results

# ---------------------------------------------------------------
def log_error(message):
    logger.error(message)
    return False

# ---------------------------------------------------------------
def check_file_exists(linked_file_path, file_path):
    if not os.path.exists(linked_file_path):
        return log_error(f"FILE NOT FOUND: {linked_file_path} in file: {file_path}")
    return True

# ---------------------------------------------------------------
def check_heading_exists(linked_file_path, link_heading, file_path):
    url = convert_filepath_to_url(linked_file_path)
    file_front_matter = global_front_matter.get(url, {})
    file_headings = file_front_matter.get("headings", [])
    converted_file_headings = [convert_heading_to_anchor(h) for h in file_headings]

    if link_heading and link_heading not in converted_file_headings:
        return log_error(f"HEADING LINK NOT FOUND: {linked_file_path}#{link_heading} in file: {file_path}")
    return True

# ---------------------------------------------------------------
def verify_links_in_file(root_folder, file_path, links, headings) -> bool:
    file_test_results = True
    global num_errors_url, num_errors_files, num_errors_headings

    # Create a list of converted headings
    converted_headings = [convert_heading_to_anchor(h) for h in headings]

    for link in links:
        # Internal Heading link - check if heading exists
        if link.startswith("#") and CHECK_HEADINGS:
            anchor_link = link[1:]  # Remove the '#' character
            if anchor_link not in converted_headings:
                file_test_results = log_error(f"HEADING NOT FOUND: {link} in file: {file_path}")
                num_errors_headings += 1

        # Internal Link - check if file exists
        elif link.startswith("/") and CHECK_FILES:
            base_link, separator, link_heading = link.partition("#")
            base_file_path = base_link[1:].replace(".html", ".md")
            linked_file_path = os.path.normpath(os.path.join(root_folder, base_file_path))

            if not check_file_exists(linked_file_path, file_path):
                num_errors_files += 1
                file_test_results = False
            elif link_heading and CHECK_HEADINGS:
                file_test_results = check_heading_exists(linked_file_path, link_heading, file_path)
                if not file_test_results:
                    num_errors_headings += 1

        # External URL starts with http
        elif link.startswith("http"):
            base_url = "https://docs.gointerject.com"
            if link.startswith(base_url) and CHECK_FILES_IN_LINKS:
                page_link = link[len(base_url):]
                base_link, separator, link_heading = page_link.partition("#")
                base_file_path = base_link[1:].replace(".html", ".md")
                linked_file_path = os.path.normpath(os.path.join(root_folder, base_file_path))

                if not check_file_exists(linked_file_path, file_path):
                    num_errors_files += 1
                    file_test_results = False
                elif link_heading and CHECK_HEADINGS_IN_LINKS:
                    file_test_results = check_heading_exists(linked_file_path, link_heading, file_path)
                    if not file_test_results:
                        num_errors_headings += 1

            # External URL - check HTTP response
            elif not link.startswith(base_url) and CHECK_URL_LINKS:
                if any(substring in link for substring in DOMAINS_TO_SKIP):
                    logger.info(f"URL FOUND BUT IS SKIPPED: {link} in file: {file_path}")
                else:
                    try:
                        response = requests.get(link, allow_redirects=True)
                        if response.status_code in {401, 403}:
                            logger.info(f"URL FOUND BUT NOT AUTHORIZED: {link} in file: {file_path}")
                        elif response.status_code != 200:
                            file_test_results = log_error(f"URL NOT FOUND (Status Code: {response.status_code}): {link} in file: {file_path}")
                            num_errors_url += 1
                    except requests.RequestException as e:
                        file_test_results = log_error(f"URL Error while accessing URL: {link} in file: {file_path} - {str(e)}")
                        num_errors_url += 1

    return file_test_results

# ---------------------------------------------------------------
def test_links():
    global global_front_matter

    yaml_filepath = os.path.join(ROOT_FOLDER, "_metadata", "front_matter.yaml")

    # Looks for the front_matter.yaml file in the _metadata folder first
    if os.path.exists(yaml_filepath):
        global_front_matter = get_yaml_from_file(yaml_filepath)
    # Will build the front matter if the yaml file is not found
    else:
        global_front_matter = extract_front_matter_from_all_pages()

    ret_val = verify_links(ROOT_FOLDER)
    num_errors = num_errors_images+num_errors_headings+num_errors_files+num_errors_url
    logger.info(f"\n\nTEST RESULTS: \n\nBroken Images:    {num_errors_images}\nBroken Files:     {num_errors_files}\nBroken Headings:  {num_errors_headings}\nBroken URLs:      {num_errors_url}\nNUM BROKEN LINKS: {num_errors}\n\nTotal Files checked: {num_files_checked}\nTotal Files Errored: {num_file_errors}\nTotal Files Passed:  {num_files_checked-num_file_errors}\n\nTest Log in 'test_log.log'. Errors in 'error_log.log'")
    assert ret_val == True, "Link verification failed. See log for details."
