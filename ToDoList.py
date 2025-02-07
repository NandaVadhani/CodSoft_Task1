import tkinter as tk
from tkinter import messagebox

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        messagebox.showinfo("Task Added", f"Task '{task}' added.")

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            messagebox.showinfo("Task Removed", f"Task '{task}' removed.")
        else:
            messagebox.showwarning("Task Not Found", f"Task '{task}' not found.")

    def view_tasks(self):
        if not self.tasks:
            messagebox.showinfo("To-Do List", "No tasks in the list.")
        else:
            tasks_str = "\n".join(f"{idx + 1}. {task}" for idx, task in enumerate(self.tasks))
            messagebox.showinfo("To-Do List", tasks_str)

class ToDoApp:
    def __init__(self, root):
        self.todo_list = ToDoList()
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("300x300")  
        
        self.tasks_listbox = tk.Listbox(root, width=45, height=10)
        self.tasks_listbox.pack(pady=10)

        self.task_entry = tk.Entry(root, width=30)
        self.task_entry.pack(pady=5)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        self.remove_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.todo_list.add_task(task)
            self.tasks_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)

    def remove_task(self):
        task = self.task_entry.get()
        if task:
            self.todo_list.remove_task(task)
            self.tasks_listbox.delete(tk.ACTIVE)
            self.task_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
