import tkinter as tk
from tkinter import messagebox

# Initialize the main window
root = tk.Tk()
root.title("To-Do List Manager")

# List to store tasks
tasks = []

# Function to update the listbox with current tasks
def update_task_listbox():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)

# Function to add a task
def add_task():
    task = task_entry.get()
    if task != "":
        tasks.append(task)
        update_task_listbox()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

# Function to remove a selected task
def remove_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        del tasks[selected_task_index]
        update_task_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to remove.")

# Function to clear all tasks
def clear_tasks():
    if messagebox.askyesno("Confirm", "Do you really want to clear all tasks?"):
        tasks.clear()
        update_task_listbox()

# GUI Layout
task_entry = tk.Entry(root, width=50)
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", width=48, command=add_task)
add_button.pack(pady=5)

remove_button = tk.Button(root, text="Remove Task", width=48, command=remove_task)
remove_button.pack(pady=5)

clear_button = tk.Button(root, text="Clear All Tasks", width=48, command=clear_tasks)
clear_button.pack(pady=5)

task_listbox = tk.Listbox(root, width=50, height=10)
task_listbox.pack(pady=10)

# Start the main loop
root.mainloop()
