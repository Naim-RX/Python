import os  # Import the os module to interact with the operating system (files, folders, paths)

# Check if a folder named "data" does not exist in the current directory
if not os.path.exists("data"):
    os.mkdir("data")  # Create a folder named "data"

# Create 10 folders inside "data" named day-1 to day-10
for i in range(0, 10):
    os.mkdir(f"data/day-{i+1}")  # f-string used to dynamically name folders

# Rename folders from "day-1, day-2..." to "day_1, day_2..." (replace - with _)
for i in range(0, 10):
    os.rename(f"data/day-{i+1}", f"data/day_{i+1}")

# List all files and folders inside the "data" directory
folders = os.listdir("data")

# Print the list of folder names inside "data"
print(folders)

# Print the current working directory (where the script is running)
print(os.getcwd())
