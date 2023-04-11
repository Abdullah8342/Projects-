# NAME: ABDULLAH
# ROLL NO: F22BSEEN1E02123


# Define an enumeration for the days of the week
from enum import Enum

class Day(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

# Define a base class for tasks
class Task:
    def __init__(self, description):
        self.description = description

    def __str__(self):
        return self.description

# Define a derived class for timed tasks
class TimedTask(Task):
    def __init__(self, description, start_time, end_time):
        super().__init__(description)
        self.start_time = start_time
        self.end_time = end_time

    def __str__(self):
        return f"{self.description} ({self.start_time}-{self.end_time})"

# Define a class for the timetable
class Timetable:
    def __init__(self):
        self.timetable = {day: [] for day in Day}

    # Method to add a new task
    def add_task(self, day, task):
        self.timetable[day].append(task)

    # Method to print the timetable for a given day
    def print_timetable(self, day):
        print(f"Timetable for {day.name}:")
        for task in self.timetable[day]:
            print(task)

# Create some tasks
task1 = Task("Read a book")
task2 = TimedTask("Meeting with John", "10:00", "11:30")
task3 = Task("Write a report")
task4 = TimedTask("Lunch with Sarah", "12:00", "13:00")
task5 = TimedTask("Gym workout", "17:00", "18:00")

# Create a timetable
timetable = Timetable()

# Add the tasks to the timetable
timetable.add_task(Day.MONDAY, task1)
timetable.add_task(Day.MONDAY, task2)
timetable.add_task(Day.TUESDAY, task3)
timetable.add_task(Day.WEDNESDAY, task4)
timetable.add_task(Day.THURSDAY, task5)

# Print the timetable for Wednesday
timetable.print_timetable(Day.WEDNESDAY)
