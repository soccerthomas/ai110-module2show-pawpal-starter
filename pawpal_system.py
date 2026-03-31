from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime, timedelta


@dataclass
class Pet:
    name: str
    species: str
    age: int


@dataclass
class Task:
    title: str
    pet: Pet
    time: datetime
    priority: int
    frequency: Optional[str] = None  # "daily", "weekly", or None
    completed: bool = False

    def mark_complete(self):
        self.completed = True


class Scheduler:
    def __init__(self):
        self.tasks: List[Task] = []

    def add_task(self, task: Task):
        self.tasks.append(task)

    def sort_by_time(self):
        return sorted(self.tasks, key=lambda t: t.time)

    def filter_tasks(self, pet_name: Optional[str] = None, completed: Optional[bool] = None):
        result = self.tasks

        if pet_name is not None:
            result = [t for t in result if t.pet.name == pet_name]

        if completed is not None:
            result = [t for t in result if t.completed == completed]

        return result

    def mark_task_complete(self, task: Task):
        task.mark_complete()

        # handle recurring tasks
        if task.frequency == "daily":
            new_task = Task(
                title=task.title,
                pet=task.pet,
                time=task.time + timedelta(days=1),
                priority=task.priority,
                frequency=task.frequency
            )
            self.add_task(new_task)

        elif task.frequency == "weekly":
            new_task = Task(
                title=task.title,
                pet=task.pet,
                time=task.time + timedelta(weeks=1),
                priority=task.priority,
                frequency=task.frequency
            )
            self.add_task(new_task)

    def detect_conflicts(self):
        warnings = []

        for i in range(len(self.tasks)):
            for j in range(i + 1, len(self.tasks)):
                t1 = self.tasks[i]
                t2 = self.tasks[j]

                if t1.time == t2.time:
                    warnings.append(
                        f"Conflict: '{t1.title}' and '{t2.title}' are scheduled at the same time ({t1.time.strftime('%I:%M %p')})"
                    )

        return warnings


class User:
    def __init__(self, name: str):
        self.name = name
        self.pets: List[Pet] = []
        self.scheduler = Scheduler()

    def add_pet(self, pet: Pet):
        self.pets.append(pet)

    def add_task(self, task: Task):
        self.scheduler.add_task(task)
