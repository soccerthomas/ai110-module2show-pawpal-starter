from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime


@dataclass
class Pet:
    name: str
    species: str
    age: int

    def update_info(self, name: Optional[str] = None, species: Optional[str] = None, age: Optional[int] = None):
        if name:
            self.name = name
        if species:
            self.species = species
        if age:
            self.age = age


@dataclass
class Task:
    title: str
    pet: Pet
    time: datetime
    priority: int
    completed: bool = False

    def mark_complete(self):
        self.completed = True

    def reschedule(self, new_time: datetime):
        self.time = new_time


class Scheduler:
    def __init__(self):
        self.tasks: List[Task] = []

    def add_task(self, task: Task):
        self.tasks.append(task)

    def remove_task(self, task: Task):
        if task in self.tasks:
            self.tasks.remove(task)

    def get_tasks_for_day(self, date: datetime):
        return [task for task in self.tasks if task.time.date() == date.date()]

    def prioritize_tasks(self):
        self.tasks.sort(key=lambda t: (t.time, t.priority))


class User:
    def __init__(self, name: str):
        self.name = name
        self.pets: List[Pet] = []
        self.scheduler = Scheduler()

    def add_pet(self, pet: Pet):
        self.pets.append(pet)

    def remove_pet(self, pet: Pet):
        if pet in self.pets:
            self.pets.remove(pet)

    def add_task(self, task: Task):
        self.scheduler.add_task(task)

    def view_tasks(self, date: datetime):
        return self.scheduler.get_tasks_for_day(date)
