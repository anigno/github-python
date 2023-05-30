import os
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk

def select_directory():
    directory = filedialog.askdirectory()
    if directory:
        file_list.delete(0, tk.END)
        file_list.insert(tk.END, *get_files_in_directory(directory))

def select_file(event):
    selected_item = file_list.get(file_list.curselection())
    if selected_item:
        file_path = selected_item.split(" - ")[1]
        show_file_content(file_path)

def get_files_in_directory(directory):
    file_list = []
    try:
        files = os.listdir(directory)
        for file in files:
            file_path = os.path.join(directory, file)
            if os.path.isfile(file_path):
                file_list.append(f"{file} - {file_path}")
    except Exception as e:
        messagebox.showerror("Error", str(e))
    return file_list

def show_file_content(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.readlines()
        content_tree.delete(*content_tree.get_children())
        for line_number, line in enumerate(content, start=1):
            parts = line.strip().split('|')
            data=' '.join(parts[4:])
            content_tree.insert("", tk.END, text=parts[0], values=(parts[1],parts[2],parts[3],data,))
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main window
window = tk.Tk()

# Create a button to select a directory
select_button = tk.Button(window, text="Select Directory", command=select_directory)
select_button.pack()

# Create a listbox to display file names
file_list = tk.Listbox(window)
file_list.pack()

# Bind the select_file function to the listbox
file_list.bind("<<ListboxSelect>>", select_file)

# Create a treeview to display file content in a table-like format
content_tree = ttk.Treeview(window, columns=("thread","severity","class","message"))
content_tree.heading("#0", text="time")
content_tree.heading("thread", text="thread")
content_tree.heading("severity", text="severity")
content_tree.heading("class", text="class")
content_tree.heading("message", text="message")
content_tree.pack()

# Start the Tkinter event loop
window.mainloop()
