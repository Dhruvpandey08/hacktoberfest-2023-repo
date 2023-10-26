import tkinter as tk
from tkinter import filedialog, messagebox

def new_file():
    my_text.delete(1.0, tk.END)
    root.title("Untitled - Notepad")

def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, 'r') as file:
            my_text.delete(1.0, tk.END)
            my_text.insert(tk.END, file.read())
            root.title(file_path)

def save_file(event=None):
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(my_text.get(1.0, tk.END))
            root.title(file_path)

def exit_editor():
    if messagebox.askyesno("Quit", "Are you sure you want to quit?"):
        root.destroy()

def undo(event=None):
    my_text.edit_undo()

def redo(event=None):
    my_text.edit_redo()

root = tk.Tk()
root.title("Untitled - Notepad")
root.geometry("800x600")

my_text = tk.Text(root, wrap=tk.WORD, font=("Arial", 14) , undo=True)
my_text.pack(expand=True, fill='both')

menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file, accelerator="Ctrl+S")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_editor)

edit_menu = tk.Menu(menu)
menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Undo", command=undo, accelerator="Ctrl+Z")
edit_menu.add_command(label="Redo", command=redo, accelerator="Ctrl+Y")

root.bind("<Control-s>", save_file)
root.bind("<Control-z>", undo)
root.bind("<Control-y>", redo)

root.mainloop()
