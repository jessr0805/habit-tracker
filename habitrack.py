import json
import os
if os.path.exists("habits.json"):
    with open("habits.json", "r") as file:
        current_habits = json.load(file)
        print(f"Welcome back! You are currently tracking the following habit: {current_habits['habit_name']} with a frequency of {current_habits['habit_frequency']}. Your current streak is {current_habits['streak_count']}.")
        habit_name = current_habits["habit_name"]
        habit_frequency = current_habits["habit_frequency"]
        streak_count = current_habits["streak_count"]
else:
    streak_count = 0
    print("Welcome to the habit tracker!")
    habit_name = input("What is the name of the habit you want to track: ").lower()
    habit_frequency = input("How often do you want to perform this habit (e.g., daily, weekly, monthly): ").lower()
    current_habits = {"habit_name": habit_name, "habit_frequency": habit_frequency, "streak_count": streak_count}
    print(f"Awesome! You plan to track the habit '{habit_name}' {habit_frequency}. Let's get started!")
print("Did you complete your habit today? (yes/no): ")
completed = input("Enter your response here: ").lower()
if completed == "yes":
    print("Great job! Keep up the good work!")
    streak_count += 1
    current_habits["streak_count"] = streak_count 
    print(f"Your current streak for '{habit_name}' is now {streak_count}")
else:
    print("No worries! You can try again tomorrow.")
with open("habits.json", "w") as file:
    json.dump(current_habits, file, indent = 4)