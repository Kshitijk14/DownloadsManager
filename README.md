# DownloadsManager
Python automation script that helps in categorizing and sorting downloaded files into appropriate folders based on file type or source.

## Run Project
- py download-manager.py

## Function of the libraries used
### 1. os (Operating System Interface):
  - The os module provides a way of interacting with the operating system, including file and directory operations.
  - In this script, os.path.join() is used to create platform-independent file paths by joining directory and file names with the appropriate path separator.
  - os.listdir() is used to list the files and directories in a given directory.
  - os.path.isfile() checks if a given path points to a file.

### 2. shutil (File Operations):
  - The shutil module provides a higher-level interface for file operations, including file copying, moving, and removal.
  -  In this script, shutil.move() is used to move files from the source directory to their respective destination folders based on their extensions.

### 3. time (Time-related Functions):
  - The time module provides various time-related functions.
  - time.sleep() is used to pause the execution of the script for a specified number of seconds. In the script, it's used to introduce a delay between scans of the source directory to avoid continuous scanning and reduce system resource usage.
