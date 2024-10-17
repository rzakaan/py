import os
import tkinter as tk
from tkinter import filedialog

class FileExplorer:
    def __init__(self, root):
        self.root = root
        self.root.title("File Explorer")
        self.current_directory = tk.StringVar()
        
        # Entry to display the current directory
        self.directory_entry = tk.Entry(root, textvariable=self.current_directory, width=50)
        self.directory_entry.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Button to open the file dialog
        self.browse_button = tk.Button(root, text="Browse", command=self.browse_directory)
        self.browse_button.grid(row=0, column=2, padx=10, pady=10)

        # Listbox to display files in the current directory
        self.file_listbox = tk.Listbox(root, width=60, height=15)
        self.file_listbox.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        # Scrollbar for the file listbox
        self.scrollbar = tk.Scrollbar(root, command=self.file_listbox.yview)
        self.scrollbar.grid(row=1, column=3, sticky="ns")

        self.file_listbox.config(yscrollcommand=self.scrollbar.set)

        # Bind double click event to open the selected file or directory
        self.file_listbox.bind('<Double-Button-1>', self.open_selected_item)

    def browse_directory(self):
        # Open a file dialog to select a directory
        selected_directory = filedialog.askdirectory()

        if selected_directory:
            self.current_directory.set(selected_directory)
            self.update_file_list(selected_directory)

    def update_file_list(self, directory):
        # Clear the file listbox
        self.file_listbox.delete(0, tk.END)

        # Get the list of files in the current directory
        files = os.listdir(directory)

        # Insert files into the listbox
        for file in files:
            self.file_listbox.insert(tk.END, file)

    def open_selected_item(self, event):
        # Get the selected item from the listbox
        selected_item = self.file_listbox.get(self.file_listbox.curselection())

        # Combine the selected item with the current directory to get the full path
        full_path = os.path.join(self.current_directory.get(), selected_item)

        # Open the selected item if it is a directory, else print the file path
        if os.path.isdir(full_path):
            self.current_directory.set(full_path)
            self.update_file_list(full_path)
        else:
            print(f"Selected File: {full_path}")

if __name__ == "__main__":
    root = tk.Tk()
    file_explorer = FileExplorer(root)
    root.mainloop()
