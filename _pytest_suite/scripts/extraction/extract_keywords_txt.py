# Extracts all keywords from the front_matter.yaml file
# Eliminates duplicates
# Saves all keywords to OUTPUT_FOLDER/OUTPUT_FILENAME

# ---------------------------------------------------------------
import yaml
import os

# ---------------------------------------------------------------
# GLOBALS
# ---------------------------------------------------------------
# All folders are relative to gointerject.github.io folder
OUTPUT_FOLDER = "_metadata"
OUTPUT_FILENAME = 'keywords.txt'
FRONT_MATTER_FILEPATH = './_metadata/front_matter.yaml'

# ---------------------------------------------------------------
# METHODS
# ---------------------------------------------------------------
def get_par_dir(n, file):
    """ returns n parent directory of file """
    file_path = os.path.abspath(file)
    for i in range(n):
        file_path = os.path.dirname(file_path)
    return file_path

# ---------------------------------------------------------------
def get_root_dir():
    root = get_par_dir(4, __file__)
    return root

# ---------------------------------------------------------------
def extract_keywords(yaml_file, output_file):
    # Load the YAML file
    with open(yaml_file, 'r') as file:
        data = yaml.safe_load(file)

    # Set to store unique keywords
    unique_keywords = set()

    # Extract keywords from each entry
    for item in data.values():
        keywords = item.get('keywords', [])
        unique_keywords.update(keywords)

    # Write unique keywords to output file
    with open(output_file, 'w') as file:
        for keyword in sorted(unique_keywords):
            file.write(f"{keyword}\n")

# ---------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------
def main():
    root_folder = get_root_dir()
    output_file = os.path.join(root_folder, OUTPUT_FOLDER, OUTPUT_FILENAME)
    output_filepath = "./" + OUTPUT_FOLDER + "/" + OUTPUT_FILENAME
    extract_keywords(FRONT_MATTER_FILEPATH, output_filepath)
    print(f"  Keywords extracted and saved to {output_file}")

if __name__ == "__main__":
    main()
