import os
import shutil
import time

# Define the source directory and the destination directory
source_directory = r"C:\Users\Hp\Downloads" # default downloads folder
destination_directory = r"E:\New-Downloads" # new downloads sort folder

# Create a dictionary mapping file extensions to folder names
extension_to_folder = {
    '.pdf': 'DOCs',
    '.doc': 'DOCs',
    '.docx': 'DOCs',
    '.txt': 'DOCs',
    '.pptx': 'DOCs',
    '.pptm': 'DOCs',
    '.ppt': 'DOCs',
    '.csv': 'DOCs',
    '.xls': 'DOCs',
    '.xlsx': 'DOCs',
    '.xlsm': 'DOCs',
    
    '.jpg': 'Images',
    '.jpeg': 'Images',
    '.png': 'Images',
    '.heic': 'Images',
    '.heif': 'Images',
    '.ico': 'Images',
    '.webp': 'Images',
    '.svg': 'Images',
    
    '.mp3': 'Music',
    '.wav': 'Music',
    '.m4a': 'Music',
    '.flac': 'Music',
    
    '.mp4': 'Videos',
    '.m4v': 'Videos',
    '.mov': 'Videos',
    
    '.zip': 'Archive',
    '.rar': 'Archive',
    '.7z': 'Archive',
    
    '.exe': 'Installers',
}

# Function to move a file to its corresponding folder based on its extension
def move_file(file_path):
    # Get the file extension
    _, file_extension = os.path.splitext(file_path)
    
    # Get the destination folder based on the extension or use 'Other' if not found
    destination_folder = extension_to_folder.get(file_extension, 'Other')
    
    # Create the full path for the destination folder
    destination_path = os.path.join(destination_directory, destination_folder)
    
    # Check if the destination folder exists, if not, create it
    if not os.path.exists(destination_path):
        os.makedirs(destination_path)
    
    # Move the file to the destination folder
    shutil.move(file_path, os.path.join(destination_path, os.path.basename(file_path)))

# Monitor the source directory for new files and sort them
while True:
    for filename in os.listdir(source_directory):
        file_path = os.path.join(source_directory, filename)
        if os.path.isfile(file_path):
            move_file(file_path)
    
    # Sleep for a while (e.g., 1 hour) before checking again
    time.sleep(3600)  # 3600 seconds = 1 hour
