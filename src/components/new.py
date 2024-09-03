import os

# Directory to check (you can use os.getcwd() for the current directory)
directory_to_check = os.getcwd()

# Test file name
test_file = os.path.join(directory_to_check, "test_write_permissions.tmp")

try:
    # Try to create a file in the specified directory
    with open(test_file, 'w') as f:
        f.write("Testing write permissions.")
    # If successful, delete the file and print success message
    os.remove(test_file)
    print("Write permissions are available.")
except Exception as e:
    print(f"No write permissions: {e}")
