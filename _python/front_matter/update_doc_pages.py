# UPDATES ALL FRONT MATTER IN ALL DOC PAGES
# ---------------------------------------------------------------
# Updates headings, links, filenames, image directory, images front matter in all doc pages

# BE SURE TO SET THE CONFIG VARIABLES IN `config.py`
# ---------------------------------------------------------------

import subprocess

def run_script(script_path):
    try:
        subprocess.run(['python', script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running script {script_path}: {e}")

if __name__ == "__main__":
    scripts = [
        "_pytest_suite/scripts/filename.py",
        "_pytest_suite/scripts/image_dir.py",
        "_pytest_suite/scripts/images.py",
        "_pytest_suite/scripts/headings.py",
        "_pytest_suite/scripts/links.py",
    ]

    for script_path in scripts:
        run_script(script_path)
