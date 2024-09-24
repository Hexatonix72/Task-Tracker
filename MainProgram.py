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

    def to_dict(self):
        return {
            'id': self.id,
            'description': self.description,
            'status': self.status,
            'createdAt': self.createdAt,
            'updatedAt': self.updatedAt
        }
    def list_to_json(task_list, file_path):
        with open(file_path, 'w') as json_file:
            json.dump([task.to_dict() for task in task_list], json_file, indent=4)


task_list = []

def addTask():
    number_of_tasks = len(task_list)
    taskNumber = number_of_tasks + 1
    name = input("Please enter the name of your task: ")
    status = "todo"
    createdTime = (datetime.now()).strftime("%Y-%m-%d %H:%M:%S")
    updatedTime = (datetime.now()).strftime("%Y-%m-%d %H:%M:%S")
    task = Task(taskNumber, name, status, createdTime, updatedTime)

    task_list.append(task)

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
Task.list_to_json(task_list, "task_list.json")
print(task_list)