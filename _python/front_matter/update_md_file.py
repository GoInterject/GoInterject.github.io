# UPDATES THE FRONT MATTER FOR ONE FILE
# ---------------------------------------------------------------
# Run this script when updating or adding a new documentation file
# You can run this script with a CLA, e.g.:
# python _python/front_matter/update_md_file.py "/wAbout/Resizing-Form-Windows.md"
# For specifics on each import, see their respective file

# BE SURE TO SET THE CONFIG VARIABLES IN `config.py`
# ---------------------------------------------------------------
import typer
from pathlib import Path
import sys

current_dir = Path(__file__).resolve().parent
parent_dir = current_dir.parent
sys.path.append(str(parent_dir))

from config import ROOT_FOLDER
from front_matter.update_filename import process_md_file as process_md_file_filename
from front_matter.update_headings import process_md_file as process_md_file_headings
from front_matter.update_image_dir import process_md_file as process_md_file_image_dir
from front_matter.update_links import process_md_file as process_md_file_links
from front_matter.update_images import process_md_file as process_md_file_images

def main(file: str = typer.Argument(None, help="Path to the markdown file to update. Overrides default file path.")):
    # Default values
    TAB_FOLDER = "\\wTroubleshoot"
    FILE = "Drill-Animations"

    # Build default file path
    file_to_update = ROOT_FOLDER + TAB_FOLDER + "\\" + FILE + ".md"

    # Override with command-line argument if provided
    if file:
        file_to_update = Path(ROOT_FOLDER) / file.lstrip("/")

    # Process the markdown file
    process_md_file_filename(file_to_update)
    process_md_file_headings(file_to_update)
    process_md_file_links(file_to_update)
    process_md_file_image_dir(file_to_update)
    process_md_file_images(file_to_update)

    print(f"  Updated front matter for file {file_to_update}")

if __name__ == "__main__":
    typer.run(main)

