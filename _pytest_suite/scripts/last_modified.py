import os
import subprocess

def get_last_modified_date(file_path):
    try:
        # Run the git log command to get the last modified date
        result = subprocess.run(
            ['git', 'log', '-1', '--pretty=format:%ci', file_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        # Handle errors if the git log command fails
        return "Error: Unable to get last modified date"

def process_md_files(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            if file_name.endswith('.md'):
                file_path = os.path.join(root, file_name)
                last_modified_date = get_last_modified_date(file_path)
                print(f"{file_name}: {last_modified_date}")

if __name__ == "__main__":
    # Replace 'your_folder_path' with the path to the folder containing .md files
    folder_path = r"D:\Users\samuelr\Documents\GitHub\GoInterject.github.io"
    # Change the current working directory to the folder containing .md files
    os.chdir(folder_path)
    # process_md_files(folder_path)

    root_file = r"D:\Users\samuelr\Documents\GitHub\GoInterject.github.io\index.md"
    result = get_last_modified_date(root_file)
    print(result)

