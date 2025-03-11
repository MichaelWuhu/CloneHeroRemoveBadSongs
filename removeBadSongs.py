import os
import re
import shutil

# Path to the badsongs.txt file

# Paste Path in the quotes, it should look like this or something similar: C:\Users\mwu25\OneDrive\Documents\Clone Hero\badsongs.txt
BADSONGS_FILE = r""
#################################

def extract_paths(file_path):
    """Extracts file paths from badsongs.txt, ignoring duplicates and trimming spaces."""
    paths = set()  
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            match = re.search(r'([a-zA-Z]:\\[^()\n]+)', line)
            if match:
                paths.add(match.group(1).strip())
    return list(paths)

def remove_files_and_folders(paths):
    """Deletes files and folders from the extracted paths."""
    for path in paths:
        # print(path)

        # Skip missing paths
        if not os.path.exists(path):
            print(f"Skipping: {path} (Not Found)")
            continue  # Skip missing paths

        
        try:
            if os.path.isfile(path):
                os.remove(path)
                print(f"Deleted file: {path}")
            elif os.path.isdir(path):
                shutil.rmtree(path)
                print(f"Deleted folder: {path}")
        except Exception as e:
            print(f"Error deleting {path}: {e}")
        
        # print(f"Path not found: {path}")

if __name__ == "__main__":
    paths = extract_paths(BADSONGS_FILE)
    remove_files_and_folders(paths)
