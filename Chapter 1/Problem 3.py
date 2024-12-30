import os

# Specify the directory path
dir_path = "/New folder"

# Get a list of files and directories in the specified path
entries = os.listdir(dir_path)

# Print the entries with indentation for visual hierarchy
for entry in entries:
    # Check if it's a directory
    if os.path.isdir(os.path.join(dir_path, entry)):
        print(f"|-- {entry}")  # Add extra indentation for directories
    else:
        print(entry)
