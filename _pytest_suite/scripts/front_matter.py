# This script will iterate through all the pages and extract the front matter into an external file

import os
import yaml  # for parsing YAML front matter and saving the result
from enum import Enum

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

def get_par_dir(n, file):
    """ returns n parent directory of file """
    file_path = os.path.abspath(file)
    for i in range(n):
        file_path = os.path.dirname(file_path)
    return file_path

def get_root_dir():
    root = get_par_dir(3, __file__)
    return root

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
                print(f"Error parsing YAML front matter in {file_path}:\n{str(e)}")
    return {}

def save_front_matter_to_file(output_file, front_matter_dict):
    """Save front matter dictionary to an external YAML file."""
    try:
        with open(output_file, "w", encoding="utf-8") as yaml_file:
            yaml.dump(front_matter_dict, yaml_file, allow_unicode=True)
        print(f"Front matter saved to {output_file}")
    except IOError as e:
        print(f"Error saving front matter to file: {str(e)}")

def convert_to_url(file_path, root_folder):
    """Convert a local file path to a www.gointerject.com URL with .html extension."""
    relative_path = os.path.relpath(file_path, root_folder)  # Get relative path from root_folder
    web_url = os.path.join("www.docs.gointerject.com", relative_path)  # Prepend the base URL
    web_url = web_url.replace("\\", "/")  # Convert backslashes to forward slashes for URLs
    web_url = web_url.replace(".md", ".html")  # Change .md extension to .html
    return web_url

# Main script logic
global_front_matter = {}
root_folder = get_root_dir()

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
            web_url = convert_to_url(file_path, root_folder)
            global_front_matter[web_url] = front_matter

# Define the output file path for saving the front matter
output_file = os.path.join(root_folder, "front_matter_output.yaml")

# Save the global front matter dictionary to an external YAML file
save_front_matter_to_file(output_file, global_front_matter)
