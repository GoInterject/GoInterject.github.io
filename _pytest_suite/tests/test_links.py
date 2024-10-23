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
def verify_front_matter(root_folder):
    results = True

    for file_path, front_matter in global_front_matter.items():
        logger.info(f" Checking: {file_path}")
        links = front_matter.get("links", [])
        image_dir = front_matter.get("image_dir", "error")
        images = front_matter.get("images", [])
        headings = front_matter.get("headings", [])

        results1 = verify_images(root_folder, file_path, image_dir, images)
        if results1 is False:
            results = False
        results2 = verify_links(root_folder, file_path, links, headings)
        if results2 is False:
            results = False

    return results

# ----------------------------------------------------------------------------------
def verify_images(root_folder, file_path, image_dir, images) -> bool:
    results = True

    if not image_dir:
        pass
    elif image_dir == "error":
        logger.error(f"FRONT_MATTER: 'image_dir' key is missing from {file_path}")
    else:
        for image in images:
            file_name = image.get("file")
            image_type = image.get("type")
            image_link = os.path.join(root_folder, "images", image_dir, f"{file_name}.{image_type}")
            if os.path.exists(image_link):
                pass
            else:
                logger.error(f"IMAGE:\nThe image: {image_link} does not exist.\nThe image link is located in: {file_path}")
                results = False
    return results

# ----------------------------------------------------------------------------------
def verify_links(root_folder, file_path, links, headings) -> bool:
    results = True

    for link in links:
        # Internal Heading link - check if heading exists
        if link.startswith("#"):
            anchor_link = link[1:]  # Remove the '#' character
            
            # Create a list of converted headings
            converted_headings = [convert_heading_to_anchor(h) for h in headings]
            
            # Check if the anchor link exists in the converted headings
            if anchor_link not in converted_headings:
                logger.error(f"HEADING: Heading not found for link: {link} in file: {file_path}")
                results = False        
        # Internal Link - check if file exists
        elif link.startswith("/"):
            # Split the link on "#" to get the file path and heading separately
            base_link, separator, heading = link.partition("#")

            # Construct the full path to the markdown file
            linked_file_path = os.path.join(root_folder, base_link[1:].replace(".html", ".md"))
            
            # Debug log for the constructed file path
            # logger.debug(f" Checking file path: {linked_file_path}")
            
            # Check if the file exists
            if not os.path.exists(linked_file_path):
                results = False
                logger.error(f"FILE:\nFile does not exist for link: {link} in file: {file_path}")

        # External URL - check HTTP response
        elif link.startswith("http"):
            try:
                response = requests.get(link)
                if response.status_code != 200:
                    results = False
                    logger.error(f"URL:\nBroken URL link: {link} in file: {file_path}")
            except requests.RequestException as e:
                results = False
                logger.error(f"URL\nError while accessing URL: {link} in file: {file_path} - {str(e)}")

    return results

# ----------------------------------------------------------------------------------

def test_front_matter():
    root = get_root_dir()
    extract_front_matter_from_files(root)
    ret_val = verify_front_matter(root)
    assert ret_val == True, "Some internal links are invalid!"

# test_front_matter()