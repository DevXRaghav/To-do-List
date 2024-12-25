#To-Do-List By Raghav Sharma

import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry_task.get()
    if task != "":
        task_frame = tk.Frame(listbox_frame, bg="black", pady=5)
        task_frame.pack(fill=tk.X)

        tick_button = tk.Checkbutton(task_frame, bg="black", activebackground="black", selectcolor="yellow", command=lambda: mark_done(tick_button, task_label))
        tick_button.pack(side=tk.LEFT, padx=10)

        task_label = tk.Label(task_frame, text=task, font=("Helvetica", 12), fg="white", bg="black")
        task_label.pack(side=tk.LEFT, padx=10)

        remove_button = tk.Button(task_frame, text="Remove", font=("Helvetica", 10), fg="white", bg="black", command=lambda: remove_task(task_frame))
        remove_button.pack(side=tk.RIGHT, padx=10)

        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def remove_task(task_frame):
    task_frame.destroy()

def mark_done(tick_button, task_label):
    if tick_button.var.get() == 1:
        task_label.config(fg="gray")
    else:
        task_label.config(fg="white")

root = tk.Tk()
root.title("Aesthetic To-Do List")
root.geometry("400x600")
root.configure(bg="black")

font_style = ("Helvetica", 14, "bold")
button_color = "#FFEB3B"
entry_color = "#333333"
listbox_color = "black"
listbox_fg = "white"

entry_task = tk.Entry(root, font=font_style, bg=entry_color, fg="white", bd=2, relief="solid", justify="center")
entry_task.pack(pady=15, padx=20, fill=tk.X)

button_add = tk.Button(root, text="Add Task", font=font_style, bg=button_color, fg="black", command=add_task, relief="flat")
button_add.pack(pady=10, padx=20, fill=tk.X)

listbox_frame = tk.Frame(root, bg="black")
listbox_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

def on_enter(e):
    e.widget['bg'] = '#fbc02d'

def on_leave(e):
    e.widget['bg'] = button_color

button_add.bind("<Enter>", on_enter)
button_add.bind("<Leave>", on_leave)

root.mainloop()
