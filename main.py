from datetime import datetime
from pawpal_system import Pet, Task, User

owner = User("Alex")

# pets
dog = Pet("Buddy", "Dog", 3)
cat = Pet("Whiskers", "Cat", 2)

owner.add_pet(dog)
owner.add_pet(cat)

# tasks (intentionally out of order + conflict)
t1 = Task("Vet Visit", dog, datetime.now().replace(hour=14, minute=0), 1)
t2 = Task("Feed Cat", cat, datetime.now().replace(hour=8, minute=30), 2, frequency="daily")
t3 = Task("Morning Walk", dog, datetime.now().replace(hour=9, minute=0), 1)
t4 = Task("Grooming", dog, datetime.now().replace(hour=9, minute=0), 2)  # conflict

owner.add_task(t1)
owner.add_task(t2)
owner.add_task(t3)
owner.add_task(t4)

print("Sorted Schedule:\n")
sorted_tasks = owner.scheduler.sort_by_time()

for task in sorted_tasks:
    print(f"{task.time.strftime('%I:%M %p')} - {task.title} ({task.pet.name})")

# filtering example
print("\nOnly Buddy's tasks:\n")
filtered = owner.scheduler.filter_tasks(pet_name="Buddy")

for task in filtered:
    print(f"{task.time.strftime('%I:%M %p')} - {task.title}")

# mark complete (triggers recurring)
print("\nMarking 'Feed Cat' complete (daily task)...\n")
owner.scheduler.mark_task_complete(t2)

print("All tasks after recurrence:\n")
for task in owner.scheduler.sort_by_time():
    print(f"{task.time.strftime('%m/%d %I:%M %p')} - {task.title}")

# conflict detection
print("\nConflict Check:\n")
conflicts = owner.scheduler.detect_conflicts()

if conflicts:
    for c in conflicts:
        print(c)
else:
    print("No conflicts found.")
