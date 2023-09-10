import os
import zipfile

def create_zip():
    """
    Creates a zip file with a naming convention 'Hicks_Ben_Weeki.zip' n
    where i iterates from 2 upwards based on the name's validity.
    """
    week_number = 2  # Starting from week 2
    
    # Determine the name for the zip file
    while True:
        zip_name = f"Hicks_Ben_Week{week_number}.zip"
        if not os.path.exists(zip_name):
            break
        week_number += 1

    # List to store names of files that are being zipped
    files_to_zip = []

    # Create a new zip file and add all .py and .ipynb files, excluding ipynb_generator.py and itself
    with zipfile.ZipFile(zip_name, 'w') as myzip:
        for filename in os.listdir('.'):
            if (filename.endswith('.py') or filename.endswith('.ipynb')) and filename not in ["ipynb_generator.py", "assignment_complete.py"]:
                myzip.write(filename)
                files_to_zip.append(filename)
    
    print(f"Files have been zipped into {zip_name}.")
    
    # Prompt the user if they'd like to remove the original files that were just zipped
    remove = input(f"Do you want to remove the files that were just zipped from the current directory? (y/n): ")
    if remove.lower() == 'y':
        for file in files_to_zip:
            os.remove(file)
            print(f"Removed {file} from the directory.")

if __name__ == '__main__':
    create_zip()