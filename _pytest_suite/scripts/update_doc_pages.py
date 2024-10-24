import subprocess

# Updates all front matter in the doc pages:
# headings, links, filenames, image directory, images

# Also outputs images data

def run_script(script_path):
    try:
        subprocess.run(['python', script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running script {script_path}: {e}")

if __name__ == "__main__":
    scripts = [
        # "_pytest_suite/scripts/filename.py",
        # "_pytest_suite/scripts/image_dir.py",
        # "_pytest_suite/scripts/images.py",
        # "_pytest_suite/scripts/headings.py",
        "_pytest_suite/scripts/links.py",
    ]

    for script_path in scripts:
        run_script(script_path)
