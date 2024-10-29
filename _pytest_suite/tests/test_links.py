import os
import logging
import requests
import yaml  # for parsing YAML front matter
from enum import Enum
import re

# ----------------------------------------------------------------------------------
logger = logging.getLogger(__name__)
global_headings_dict = {}
global_front_matter = {}
num_files_checked = 0
num_errors_url = 0
num_errors_images = 0
num_errors_files = 0
num_errors_headings = 0
num_file_errors = 0
CHECK_IMAGES = False
CHECK_FILES = False
CHECK_HEADINGS = False # Headings will not be check if CHECK_FILES = False
CHECK_FILES_IN_LINKS = False
CHECK_HEADINGS_IN_LINKS = False # Headings in links will not be check if CHECK_FILES_IN_LINKS = False
CHECK_URL_LINKS = True

# ----------------------------------------------------------------------------------
class PageDirectories(Enum):
    WABOUT = "wAbout"
    WAPI = "wApi"
    WDESIGN = "wDesign"
    WDEVELOPER = "wDeveloper"
    WFUNCTIONS = "wFunctions"
    WGETSTARTED = "wGetStarted"
    WINDEX = "wIndex"
    WLABS = "wLabs"
    WPORTAL = "wPortal"
    WRELEASENOTES = "wReleaseNotes"
    WTROUBLESHOOT = "wTroubleshoot"
    BFINANCIALS = "bApps\\bFinancials"
    InterjectTRAININGBUDGET = "bApps\\InterjectTraining\\Budget"
    InterjectTRAININGCAPITAL = "bApps\\InterjectTraining\\Capital"
    InterjectTRAININGPROJECTIONS = "bApps\\InterjectTraining\\Projections"
    InterjectTRAININGWIP = "bApps\\InterjectTraining\\WIP"

# ----------------------------------------------------------------------------------
def prRed(skk): 
    logger.error(skk)

# ----------------------------------------------------------------------------------
def get_par_dir(n, file):
    """ returns n parent directory of file """
    file_path = os.path.abspath(file)
    for i in range(n):
        file_path = os.path.dirname(file_path)
    return file_path

# ----------------------------------------------------------------------------------
def get_root_dir():
    root = get_par_dir(3, __file__)
    return root

# ----------------------------------------------------------------------------------
def extract_front_matter(file_str):
    """Extract front matter from a file content string."""
    if file_str.startswith("---"):
        end_idx = file_str.find("---", 3)  # Find the second occurrence of '---'
        if end_idx != -1:
            front_matter_str = file_str[3:end_idx]
            # Replace tabs with spaces to prevent YAML parsing errors
            front_matter_str = front_matter_str.replace("\t", "    ")  # Replace with 4 spaces (adjust as needed)
            try:
                return yaml.safe_load(front_matter_str)
            except yaml.YAMLError as e:
                logger.error(f"PARSE: Error parsing YAML front matter: {str(e)}")
    return {}

# ----------------------------------------------------------------------------------
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

# ----------------------------------------------------------------------------------
def extract_front_matter_from_files(root_folder):
    for folder in PageDirectories:
        dir_path = os.path.join(root_folder, folder.value)
        if not os.path.exists(dir_path):
            continue

        for file_name in os.listdir(dir_path):
            file_path = os.path.join(dir_path, file_name)
            if not file_name.endswith(".md"):
                continue

            with open(file_path, "r", encoding="utf-8") as file_handle:
                file_str = file_handle.read()
                front_matter = extract_front_matter(file_str)
                global_front_matter[file_path] = front_matter

# ----------------------------------------------------------------------------------
def verify_links(root_folder):
    global num_files_checked
    global num_file_errors
    test_results = True

    for file_path, front_matter in global_front_matter.items():
        results_images_test = True
        results_links_test = True
        num_files_checked = num_files_checked + 1
        logger.info(f" Checking: {file_path}")
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

# ----------------------------------------------------------------------------------
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
                logger.error(f"IMAGE NOT FOUND: {image_link} does not exist in: {file_path}\n")
                num_errors_images = num_errors_images + 1
                file_test_results = False
    return file_test_results

# ----------------------------------------------------------------------------------
def verify_links_in_file(root_folder, file_path, links, headings) -> bool:
    file_test_results = True
    global num_errors_url
    global num_errors_files
    global num_errors_headings

    # Create a list of converted headings
    converted_headings = [convert_heading_to_anchor(h) for h in headings]

    for link in links:
        # Internal Heading link - check if heading exists
        if link.startswith("#") and CHECK_HEADINGS:
            anchor_link = link[1:]  # Remove the '#' character
            
            # Check if the anchor link exists in the converted headings
            if anchor_link not in converted_headings:
                logger.error(f"HEADING NOT FOUND: {link} in file: {file_path}\n")
                num_errors_headings = num_errors_headings + 1
                file_test_results = False        
        # Internal Link - check if file exists
        elif link.startswith("/") and CHECK_FILES:
            # Split the link on "#" to get the file path and heading separately
            base_link, separator, link_heading = link.partition("#")
            base_file_path = base_link[1:].replace(".html", ".md")

            # Construct the full path to the markdown file
            linked_file_path = os.path.normpath(os.path.join(root_folder, base_file_path))            

            # Check if the file exists
            if not os.path.exists(linked_file_path):
                file_test_results = False
                logger.error(f"FILE NOT FOUND: {linked_file_path} in file: {file_path}\n")
                num_errors_files = num_errors_files + 1
            # Check if the link heading exists
            elif link_heading and CHECK_HEADINGS:
                file_front_matter = global_front_matter.get(linked_file_path.replace('/', '\\'), {})
                file_headings = file_front_matter.get("headings", [])
                converted_file_headings = [convert_heading_to_anchor(h) for h in file_headings]

                # Check if the linked heading exists in the target file's headings
                if link_heading and link_heading not in converted_file_headings:
                    file_test_results = False
                    logger.error(f"HEADING NOT FOUND: {linked_file_path}#{link_heading} in file: {file_path}\n")
                    num_errors_headings = num_errors_headings + 1

        # External URL starts with http
        elif link.startswith("http"):
            # If external url is an actual page in our docs, just check the local file
            base_url = "https://docs.gointerject.com"
            if link.startswith(base_url) and CHECK_FILES_IN_LINKS:
                page_link = link[len(base_url):]
                base_link, separator, link_heading = page_link.partition("#")
                base_file_path = base_link[1:].replace(".html", ".md")

                # Construct the full path to the markdown file
                linked_file_path = os.path.normpath(os.path.join(root_folder, base_file_path))

                if not os.path.exists(linked_file_path):
                    file_test_results = False
                    logger.error(f"FILE IN LINK NOT FOUND: {linked_file_path} in file: {file_path}\n")
                    num_errors_files = num_errors_files + 1

                elif link_heading and CHECK_HEADINGS_IN_LINKS:
                    file_front_matter = global_front_matter.get(linked_file_path.replace('/', '\\'), {})
                    file_headings = file_front_matter.get("headings", [])
                    converted_file_headings = [convert_heading_to_anchor(h) for h in file_headings]

                    # Check if the linked heading exists in the target file's headings
                    if link_heading and link_heading not in converted_file_headings:
                        file_test_results = False
                        logger.error(f"HEADING IN LINK NOT FOUND: {linked_file_path}#{link_heading} in file: {file_path}\n")
                        num_errors_headings = num_errors_headings + 1

            # External URL - check HTTP response
            elif not link.startswith(base_url) and CHECK_URL_LINKS:
                try:
                    response = requests.get(link, allow_redirects=True)
                    if response.status_code == 401 or response.status_code == 403:
                        logger.info(f" URL FOUND BUT NOT AUTHORIZED: {link} in file: {file_path}\n")
                    elif response.status_code != 200:
                        file_test_results = False
                        logger.error(f"URL NOT FOUND (Status Code: {response.status_code}): {link} in file: {file_path}\n")
                        num_errors_url += 1
                except requests.RequestException as e:
                    file_test_results = False
                    logger.error(f"URL Error while accessing URL: {link} in file: {file_path} - {str(e)}\n")
                    num_errors_url += 1

    return file_test_results
# ----------------------------------------------------------------------------------

def test_links():
    root = get_root_dir()
    extract_front_matter_from_files(root)
    ret_val = verify_links(root)
    num_errors = num_errors_images+num_errors_headings+num_errors_files+num_errors_url
    logger.info(f" SUMMARY: \n\nBroken Images:    {num_errors_images}\nBroken Files:     {num_errors_files}\nBroken Headings:  {num_errors_headings}\nBroken URLs:      {num_errors_url}\nNUM BROKEN LINKS: {num_errors}\n\nTotal Files checked: {num_files_checked}\nTotal Files Errored: {num_file_errors}\nTotal Files Passed:  {num_files_checked-num_file_errors}\n\nTest Log in 'test_log.log'. Errors in 'error_log.log'")
    assert ret_val == True, "Failed. See log for details."
