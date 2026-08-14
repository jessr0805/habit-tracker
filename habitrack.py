import json
import os
if os.path.exists("habits.json"):
    with open("habits.json", "r") as file:
        current_habits = json.load(file)
        print(f"Welcome back! You are currently tracking the following habits: {current_habits}")
else:
    print("Welcome to the habit tracker!")
    habit_name = input("What is the name of the habit you want to track: ").lower()
    habit_frequency = input("How often do you want to perform this habit (e.g., daily, weekly, monthly): ").lower()
    print(f"Awesome! You plan to track the habit '{habit_name}' {habit_frequency}. Let's get started!")
    current_habits = {f"{habit_name}, {habit_frequency}"}

with open("habits.json", "w") as file:
    json.dump(current_habits, file, indent = 4)