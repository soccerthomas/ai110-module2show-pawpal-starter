from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime


# Represents a pet in the system
@dataclass
class Pet:
    name: str
    species: str
    age: int

    def update_info(self, name: Optional[str] = None, species: Optional[str] = None, age: Optional[int] = None):
        pass


# Represents a task (feeding, walking, vet visit, etc.)
@dataclass
class Task:
    title: str
    pet: Pet
    time: datetime
    priority: int
    completed: bool = False

    def mark_complete(self):
        pass

    def reschedule(self, new_time: datetime):
        pass


# Handles scheduling logic
class Scheduler:
    def __init__(self):
        self.tasks: List[Task] = []

    def add_task(self, task: Task):
        pass

    def remove_task(self, task: Task):
        pass

    def get_tasks_for_day(self, date: datetime):
        pass

    def prioritize_tasks(self):
        pass


# Represents the user of the app
class User:
    def __init__(self, name: str):
        self.name = name
        self.pets: List[Pet] = []
        self.scheduler = Scheduler()

    def add_pet(self, pet: Pet):
        pass

    def remove_pet(self, pet: Pet):
        pass

    def add_task(self, task: Task):
        pass

    def view_tasks(self, date: datetime):
        pass
