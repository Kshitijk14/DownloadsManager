# file_organizer_script.py

import os
import shutil

def main_script_function(source_directory, destination_directory, extension_to_folder):
    for filename in os.listdir(source_directory):
        file_path = os.path.join(source_directory, filename)
        if os.path.isfile(file_path):
            move_file(file_path, destination_directory, extension_to_folder)

def move_file(file_path, destination_directory, extension_to_folder):
    _, file_extension = os.path.splitext(file_path)
    destination_folder = extension_to_folder.get(file_extension, 'Other')
    destination_path = os.path.join(destination_directory, destination_folder)

    if not os.path.exists(destination_path):
        os.makedirs(destination_path)

    shutil.move(file_path, os.path.join(destination_path, os.path.basename(file_path)))
