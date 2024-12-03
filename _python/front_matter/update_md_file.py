# UPDATES THE FRONT MATTER FOR ONE FILE
# ---------------------------------------------------------------
# Run this script when updating or adding a new documentation file
# For specifics on each import, see their respective file

# BE SURE TO SET THE CONFIG VARIABLES IN `config.py`
# ---------------------------------------------------------------
import os
import sys
import argparse

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import ROOT_FOLDER
from update_filename import process_md_file as process_md_file_filename
from update_headings import process_md_file as process_md_file_headings
from update_image_dir import process_md_file as process_md_file_image_dir
from update_links import process_md_file as process_md_file_links
from update_images import process_md_file as process_md_file_images

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Update front matter for markdown files.")
    parser.add_argument("file", nargs="?", help="Path to the markdown file to update. Overrides default file path.")

    args = parser.parse_args()

    # Default values
    TAB_FOLDER = "\\wTroubleshoot"
    FILE = "Drill-Animations"

    # Build default file path
    file_to_update = ROOT_FOLDER + TAB_FOLDER + "\\" + FILE + ".md"

    # Override with command-line argument if provided
    if args.file:
        file_to_update = ROOT_FOLDER + args.file

    # Process the markdown file
    process_md_file_filename(file_to_update)
    process_md_file_headings(file_to_update)
    process_md_file_links(file_to_update)
    process_md_file_image_dir(file_to_update)
    process_md_file_images(file_to_update)

    print(f"  Updated front matter for file {file_to_update}")

if __name__ == "__main__":
    main()
