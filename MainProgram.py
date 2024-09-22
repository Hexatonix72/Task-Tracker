from enum import Enum
from datetime import datetime
import json

def get_object_attributes(obj):
    return {attr: getattr(obj, attr) for attr in dir(obj) 
            if not attr.startswith('__') and not callable(getattr(obj, attr))}

class Task:
    def __init__(self, id, description, status, createdAt, updatedAt):
        self.id = id
        self.description = description
        self.status = status
        self.createdAt = createdAt
        self.updatedAt = updatedAt

task_list = []

def addTask():
    number_of_tasks = len(task_list)
    taskNumber = number_of_tasks + 1
    name = input("Please enter the name of your task: ")
    status = "todo"
    createdTime = datetime.now()
    updatedTime = datetime.now()

    task_list.append(Task(taskNumber, name, status, createdTime, updatedTime))

def print_objects_with_attributes(object_list):
    for i, obj in enumerate(object_list):
        print(f"Object {i+1}")
        attributes = get_object_attributes(obj)
        for attr, value in attributes.items():
            print(f"  {attr}: {value}")
        print()  # Empty line for readability


addTask()
addTask()
print_objects_with_attributes(task_list)

with open('listOfTasks.json', 'w') as f:
    json.dump(task_list, f, indent=4)