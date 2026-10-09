# To-Do List Manager - Internship Project
# Author: Gayathri Supraja

tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Task Added: {task}")

def view_tasks():
    print("\n--- My To-Do List ---")
    if not tasks:
        print("No tasks yet!")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def complete_task(index):
    if 0 < index <= len(tasks):
        removed = tasks.pop(index-1)
        print(f"Completed: {removed}")
    else:
        print("Invalid task number!")

# Main execution
print("Welcome to To-Do List Manager")
add_task("Learn Python")
add_task("Complete GitHub Project")
add_task("Submit Internship Task")

view_tasks()
complete_task(1)
view_tasks()

print(f"\nTotal pending tasks: {len(tasks)}")
print("Project by Gayathri - Completed!")
