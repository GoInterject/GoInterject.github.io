# PYTEST TO VALIDATE ALL LINKS IN THE TOC FILES
# ---------------------------------------------------------------
# Iterates through the DATA_FOLDER and all subfolders finding yaml files
# Extracts all paths from the file
# Excludes paths with no extension (e.g. folders and not files)
# Verifies if path is valid

# BE SURE TO SET THE CONFIG VARIABLES IN `config.py`
# ---------------------------------------------------------------

import logging
import yaml
import os
import glob
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import ROOT_FOLDER, DATA_FOLDER

# ---------------------------------------------------------------
# GLOBALS
# ---------------------------------------------------------------
logger = logging.getLogger(__name__)
num_broken_paths = 0
num_skipped_paths = 0
num_paths = 0

# ---------------------------------------------------------------
# METHODS
# ---------------------------------------------------------------
def extract_paths_from_yaml(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)

    def find_paths(node, paths):
        if isinstance(node, dict):
            for key, value in node.items():
                if key == 'path' and isinstance(value, str):
                    paths.append(value)
                else:
                    find_paths(value, paths)
        elif isinstance(node, list):
            for item in node:
                find_paths(item, paths)

    paths = []
    find_paths(data, paths)
    return paths

# ---------------------------------------------------------------
def verify_paths(paths, toc_filepath):
    global num_paths, num_broken_paths, num_skipped_paths

    verified_paths = []
    for path in paths:
        num_paths += 1
        if path.endswith('.html'):
            # Remove leading slash from path and replace .html with .md
            relative_path = path.lstrip('/')
            md_path = os.path.join(ROOT_FOLDER, relative_path.replace('.html', '.md'))
            # Verify if the file exists
            if os.path.exists(md_path):
                verified_paths.append(md_path)
            else:
                num_broken_paths += 1
                logger.error(f"TOC PATH NOT FOUND: {md_path} in file: {toc_filepath}")
        else:
            num_skipped_paths += 1
            # logger.info(f"Skipping non-HTML path: {path} in file: {toc_filepath}")
    return verified_paths

# ---------------------------------------------------------------
def traverse_and_verify_yaml_files(directory_path):
    for yaml_file in glob.glob(f"{directory_path}/**/*.yaml", recursive=True):
        logger.info(f"Processing toc file: {yaml_file}")
        paths = extract_paths_from_yaml(yaml_file)
        verify_paths(paths, yaml_file)

# ---------------------------------------------------------------
def test_toc():
    data_folder = os.path.join(ROOT_FOLDER, DATA_FOLDER)
    traverse_and_verify_yaml_files(data_folder)
    logger.info(f"f:\n\nTEST RESULTS TOC FILES: \n\nBroken paths:  {num_broken_paths}\nSkipped paths:  {num_skipped_paths}\nTotal paths:  {num_paths}")
    assert num_broken_paths == 0, "TOC verification failed. See log fore details."
