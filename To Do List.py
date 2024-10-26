import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.root.geometry("400x400")

        self.tasks = []
        self.task_vars = []

        # Entry for new task
        self.task_entry = tk.Entry(self.root, width=30)
        self.task_entry.pack(pady=10)

        # Buttons
        self.add_task_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_task_button.pack(pady=5)

        self.update_task_button = tk.Button(self.root, text="Update Task", command=self.update_task)
        self.update_task_button.pack(pady=5)

        self.delete_task_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_task_button.pack(pady=5)

        # Frame for task checkboxes
        self.task_frame = tk.Frame(self.root)
        self.task_frame.pack(pady=20)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            var = tk.BooleanVar()
            self.tasks.append(task)
            self.task_vars.append(var)
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def update_task(self):
        try:
            selected_index = self.get_selected_index()
            if selected_index is not None:
                self.tasks[selected_index] = self.task_entry.get()
                self.update_task_listbox()
                self.task_entry.delete(0, tk.END)
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to update.")

    def delete_task(self):
        try:
            selected_index = self.get_selected_index()
            if selected_index is not None:
                del self.tasks[selected_index]
                del self.task_vars[selected_index]
                self.update_task_listbox()
                self.task_entry.delete(0, tk.END)
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def update_task_listbox(self):
        # Clear the current task frame
        for widget in self.task_frame.winfo_children():
            widget.destroy()

        # Create checkboxes for each task
        for index, task in enumerate(self.tasks):
            var = self.task_vars[index]
            checkbox = tk.Checkbutton(self.task_frame, text=task, variable=var)
            checkbox.pack(anchor='w')

    def get_selected_index(self):
        for index, var in enumerate(self.task_vars):
            if var.get():
                return index
        return None

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()