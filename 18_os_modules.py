#Getting the Current working directory
import os 
cwd = os.getcwd() 
print("Current working directory:", cwd) 

#os.mkdir()  By using os.mkdir() method in Python is used to create a directory named path with the specified numeric mode.
# Define the directory name
folder_name = "skiee"

# Check if it already exists to avoid error
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(f"Folder '{folder_name}' created successfully.")
else:
    print(f"Folder '{folder_name}' already exists.")

#To delete a folder in Python, you can use the os.rmdir() function — but only if the folder is empty.

folder_name = "skiee"

if os.path.exists(folder_name):
    os.rmdir(folder_name)
    print(f"Folder '{folder_name}' deleted successfully.")
else:
    print(f"Folder '{folder_name}' does not exist.")

