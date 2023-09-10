import os
import subprocess

def format_comments(file_path):
    """Format comments in the Python file and return the formatted content."""
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    formatted_lines = []
    was_previous_line_comment = False  # Track if the previous line was a comment

    for index, line in enumerate(lines):
        if line.startswith("#") and not was_previous_line_comment and index != 0:  # Check if not the first line
            formatted_lines.append('\n')  # Add newline before the comment

        # Append current line to the new list
        formatted_lines.append(line)

        was_previous_line_comment = line.startswith("#")

        # If it's a comment and the next line is not a comment or whitespace
        next_line = lines[index + 1] if index + 1 < len(lines) else ""
        if line.startswith("#") and not next_line.lstrip().startswith("#") and next_line.strip():
            formatted_lines.append('\n')  # Add newline after the comment

    # Return the formatted content as a single string
    return ''.join(formatted_lines)

def convert_py_to_ipynb(directory='.'):
    """Converts all .py files in the given directory to .ipynb using jupytext, excluding ipynb_generator.py and assignment_complete.py."""
    
    # State variables to remember user's choice for all files
    yes_all = False
    no_all = False
    
    # List of files to exclude from conversion
    excluded_files = ["ipynb_generator.py", "assignment_complete.py"]
    
    # List all files in the directory
    for filename in os.listdir(directory):
        full_path = os.path.join(directory, filename)
        
        # Ensure that it's a file and not a directory
        if not os.path.isfile(full_path):
            continue
        
        # Check if the file is a Python file and is not in the excluded_files list
        if filename.endswith('.py') and filename not in excluded_files:
            ipynb_filename = filename.replace('.py', '.ipynb')
            
            # If corresponding .ipynb exists and no global choice has been made yet
            if os.path.exists(ipynb_filename) and not yes_all and not no_all:
                refresh = input(f"Do you want to refresh {ipynb_filename}? (y/ya/n/na): ")

                if refresh.lower() == 'ya':
                    yes_all = True
                elif refresh.lower() == 'na':
                    no_all = True
                elif refresh.lower() != 'y':
                    continue  # Skip to the next file if user answers 'n'

                if not no_all:  # Delete the file if not 'no to all'
                    os.remove(ipynb_filename)  # Delete the existing .ipynb file
            
            # If 'no to all' was selected, skip the conversion for all subsequent files
            elif no_all:
                continue
            
            print(f"Processing file: {filename}")
            formatted_content = format_comments(filename)
            
            with open(filename, 'r+') as f:  # Open file in read+write mode
                # Move to the start of the file
                f.seek(0)
                # Write the formatted content to the file
                f.write(formatted_content)
                # Truncate the file to the size of the formatted content (removes any extra content at the end)
                f.truncate()

            command = f'jupytext --to notebook {filename}'
            
            # Execute the command to generate the .ipynb
            subprocess.run(command, shell=True, check=True)
            print(f"Converted {filename} to {ipynb_filename}")

if __name__ == '__main__':
    convert_py_to_ipynb()