import json
import os

FILENAME = "tasks.json"

def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(FILENAME, "w") as f:
        json.dump(tasks, f, indent=2)

def show_tasks(tasks):
    print("\n========================================")
    print("            YOUR TO-DO LIST             ")
    print("========================================")
    if not tasks:
        print("  No tasks yet! Add some tasks.")
    else:
        for i, task in enumerate(tasks, 1):
            status = "✔" if task["done"] else "○"
            print(f"  {i}. [{status}] {task['title']}")
    print("========================================")

def add_task(tasks):
    title = input("Enter task: ").strip()
    if title:
        tasks.append({"title": title, "done": False})
        save_tasks(tasks)
        print(f"✔ Task added: '{title}'")
    else:
        print("Task cannot be empty!")

def complete_task(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Enter task number to mark complete: "))
        if 1 <= num <= len(tasks):
            tasks[num-1]["done"] = True
            save_tasks(tasks)
            print(f"✔ Task '{tasks[num-1]['title']}' marked as done!")
        else:
            print("Invalid number!")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num-1)
            save_tasks(tasks)
            print(f"✔ Task '{removed['title']}' deleted!")
        else:
            print("Invalid number!")
    except ValueError:
        print("Please enter a valid number.")

def update_task(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Enter task number to update: "))
        if 1 <= num <= len(tasks):
            new_title = input(f"New title (current: '{tasks[num-1]['title']}'): ").strip()
            if new_title:
                tasks[num-1]["title"] = new_title
                save_tasks(tasks)
                print("✔ Task updated!")
        else:
            print("Invalid number!")
    except ValueError:
        print("Please enter a valid number.")

def main():
    print("========================================")
    print("       WELCOME TO TO-DO LIST APP        ")
    print("========================================")
    tasks = load_tasks()

    while True:
        print("\n  1. View Tasks")
        print("  2. Add Task")
        print("  3. Mark Task as Complete")
        print("  4. Update Task")
        print("  5. Delete Task")
        print("  6. Exit")
        choice = input("\nEnter choice (1-6): ").strip()

        if   choice == "1": show_tasks(tasks)
        elif choice == "2": add_task(tasks)
        elif choice == "3": complete_task(tasks)
        elif choice == "4": update_task(tasks)
        elif choice == "5": delete_task(tasks)
        elif choice == "6":
            print("Goodbye!"); break
        else:
            print("Invalid choice! Enter 1-6.")

if __name__ == "__main__":
    main()
