# UPDATES THE FRONT MATTER FOR ONE FILE
# ---------------------------------------------------------------
# Run this script when updating or adding a new documentation file
# For specifics on each import, see their respective file

# BE SURE TO SET THE CONFIG VARIABLES IN `config.py`
# ---------------------------------------------------------------

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import ROOT_FOLDER
from update_filename import process_md_file as process_md_file_filename
from update_headings import process_md_file as process_md_file_headings
from update_image_dir import process_md_file as process_md_file_image_dir
from update_links import process_md_file as process_md_file_links
from update_images import process_md_file as process_md_file_images

# ---------------------------------------------------------------
if __name__ == "__main__":
    # TAB_FOLDER = "\wIndex"
    # TAB_FOLDER = "\wReleaseNotes"
    # TAB_FOLDER = "\wDeveloper"
    TAB_FOLDER = "\wPortal"
    # TAB_FOLDER = "\wGetStarted"
    # TAB_FOLDER = "\wTroubleshoot"
    # TAB_FOLDER = "\wAbout"
    # TAB_FOLDER = "\wLabs"
    # TAB_FOLDER = ""
    # TAB_FOLDER = r"\bApps\bFinancials"
    FILE = "DataPortals"

    NEW_DOC_PAGE = True # Set to true will generate images entry from all images referenced in the file
    # NEW_DOC_PAGE = False # Set to false will not update images if image front matter entry count is different than images referenced in file count

    file_to_update = ROOT_FOLDER + TAB_FOLDER + "\\" + FILE + ".md"

    process_md_file_filename(file_to_update)
    process_md_file_headings(file_to_update)
    process_md_file_links(file_to_update)
    process_md_file_image_dir(file_to_update)
    process_md_file_images(file_to_update)

    print(f"  Updated front matter for file {file_to_update}")
