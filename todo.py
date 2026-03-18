import json
import os
from datetime import datetime

def load_task():
    try:
        with open("tasks.json","r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def save_tasks(tasks):
    with open("tasks.json","w") as f:
        json.dump(tasks,f)

def add_task(tasks):
    try:
        title=input("Enter a title: ").strip()
        if not title:
            raise ValueError("Task title cannot be empty")
        new_task={
        "title":title,
        "done":False,
        "created": datetime.now().strftime("%d-%m-%Y")
    }
        tasks.append(new_task)
        print("Task added successfully")
    except ValueError as e:
        print(f'Error:{e}')

def show_task(tasks):
    if not tasks:
        print("Tasks not found!")
        return
    for index,task in enumerate(tasks,1):
        status_icon="[✅]" if task.get("done") else "[] "
        print(f"{index}.{status_icon}{task.get('title')}(Added:{task.get('created')})")


def mark_done(tasks):
    show_task(tasks)
    if not tasks:
        return
    try:
        task_num=int(input("Enter a task number to toggle:"))
        index=task_num-1
        if index<0:
            raise IndexError("Enter a number 1 or higher!")
        tasks[index]["done"]=not tasks[index]["done"]
        if tasks[index]["done"]==True:
            print("Task marked as done.")
        else:
            print("Task marked as undone!")
    except ValueError:
        print("Error! Please enter a valid integer.")
    except IndexError as e:
        print(f"Error!{e}")

def delete_task(tasks):
    show_task(tasks)
    if not tasks:
        return
    try:
        task_num=int(input("Enter task number to delete:"))
        index=task_num-1
        if index<0:
            raise IndexError("Enter a number 1 or higher!")
        choice=input(f'Are you sure {tasks[index]["title"]} should be deleted(y/n):').lower()
        if choice=="y":
            del tasks[index]
            print("Task deleted!")
        elif choice=="n":
            print("Deletion cancelled!")
        else:
            print("Enter a valid choice!")
    except ValueError:
        print("Error! Enter a valid integer!")
    except IndexError as e:
        print(f'Error! {e}')
    

def main():
    tasks=load_task()
    while True:
        print("\n===TO DO APP===\n1. Add task\n2. View tasks\n3. Mark task done\n4. Delete task\n5. Quit")
        try:    
            choice=input("Enter you'r choice:").strip()
            if choice=="1":
                add_task(tasks)
            elif choice=="2":
                show_task(tasks)
            elif choice=="3":
                mark_done(tasks)
            elif choice=="4":
                delete_task(tasks)
            elif choice=="5":
                save_tasks(tasks)
                print("Tasks saved. Goodbye!")
                break
            else:
                print("Enter a valid choice with help of numbers among 1 to 5!")
        except ValueError:
            print("Please enter a number!")
main()
        
        
