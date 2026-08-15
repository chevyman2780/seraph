import os

def replace_in_file(file_path):
    target_str = "G-7FN7LEVWXD"
    replacement_str = "G-NNF7NQT0Q0"
    
    try:
        # Read the file contents with UTF-8 encoding (falls back safely where possible)
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            content = file.read()
            
        # Check if the target string exists in the file
        if target_str in content:
            new_content = content.replace(target_str, replacement_str)
            
            # Write the updated content back to the file
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(new_content)
                
            print(f"Updated: {file_path}")
            
    except Exception as e:
        print(f"Could not process file {file_path}: {e}")

def traverse_and_replace():
    # os.walk automatically goes through every single directory and subdirectory
    current_directory = os.getcwd()
    
    print(f"Starting search in: {current_directory}")
    
    for root, dirs, files in os.walk(current_directory):
        # Skip this script file itself so it doesn't modify its own code
        script_name = os.path.basename(__file__)
        if script_name in files:
            files.remove(script_name)
            
        for file in files:
            file_path = os.path.join(root, file)
            replace_in_file(file_path)
            
    print("Replacement process completed.")

if __name__ == "__main__":
    traverse_and_replace()