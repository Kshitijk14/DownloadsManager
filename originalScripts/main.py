import tkinter as tk
from tkinter import filedialog
import os
import shutil
import time

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Organizer")

        # Create widgets
        self.label_source = tk.Label(root, text="Source Directory:")
        self.entry_source = tk.Entry(root)
        self.button_browse_source = tk.Button(root, text="Browse", command=self.browse_source)

        self.label_destination = tk.Label(root, text="Destination Directory:")
        self.entry_destination = tk.Entry(root)
        self.button_browse_destination = tk.Button(root, text="Browse", command=self.browse_destination)

        self.button_sort = tk.Button(root, text="Sort Files", command=self.sort_files)

        # Grid layout
        self.label_source.grid(row=0, column=0)
        self.entry_source.grid(row=0, column=1)
        self.button_browse_source.grid(row=0, column=2)

        self.label_destination.grid(row=1, column=0)
        self.entry_destination.grid(row=1, column=1)
        self.button_browse_destination.grid(row=1, column=2)

        self.button_sort.grid(row=2, column=1)
        
        # Dictionary mapping file extensions to folder names
        self.extension_to_folder = {
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
            
            '.dll': 'Plugins',
            '.vst': 'Plugins',
            '.vst2': 'Plugins',
            '.vst3': 'Plugins',
            '.aax': 'Plugins',
            '.au': 'Plugins',
            '.rtas': 'Plugins',
            '.tdm': 'Plugins',
            '.clap': 'Plugins',
        }

    def browse_source(self):
        source_path = filedialog.askdirectory()
        self.entry_source.delete(0, tk.END)
        self.entry_source.insert(0, source_path)

    def browse_destination(self):
        destination_path = filedialog.askdirectory()
        self.entry_destination.delete(0, tk.END)
        self.entry_destination.insert(0, destination_path)

    def sort_files(self):
        source_directory = self.entry_source.get()
        destination_directory = self.entry_destination.get()

        # Your existing sorting logic here
        for filename in os.listdir(source_directory):
            file_path = os.path.join(source_directory, filename)
            if os.path.isfile(file_path):
                self.move_file(file_path, destination_directory)

    def move_file(self, file_path, destination_directory):
        # Your existing move_file function here
        _, file_extension = os.path.splitext(file_path)
        destination_folder = self.extension_to_folder.get(file_extension, 'Other')
        destination_path = os.path.join(destination_directory, destination_folder)

        if not os.path.exists(destination_path):
            os.makedirs(destination_path)

        shutil.move(file_path, os.path.join(destination_path, os.path.basename(file_path)))

if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()
