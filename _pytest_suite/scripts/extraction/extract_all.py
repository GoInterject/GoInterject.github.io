# run_all_scripts.py

# Import each script as a function or module
import extract_front_matter
import extract_keywords_txt
import extract_keywords
import extract_content

def run_all():
    # Run each script in order
    print("Running extract_front_matter.py...")
    extract_front_matter.main()

    print("Running extract_keywords_txt.py...")
    extract_keywords_txt.main()

    print("Running extract_keywords.py...")
    extract_keywords.main()

    print("Running extract_content.py...")
    extract_content.main()

    print("All scripts completed successfully.")

if __name__ == "__main__":
    run_all()
