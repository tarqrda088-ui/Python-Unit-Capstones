name = input("What is your name: ")

birth_year = int(input("What is your birth year: "))
age = 2026 - birth_year

if age < 12:
    print("This app is for adults")
else:
    print("Welcome to the app")

weight = int(input("What is your weight (kg): "))
height = float(input("What is your height (m): "))

bmi = weight / (height ** 2)

if 60 < weight < 80:
    print("Continue to practice sports")
elif weight < 60:
    print("You should eat more")
else:
    print("You need a dietary program and reduce sugar intake")

daily_tasks = []

task = input("Enter a task for today: ")
daily_tasks.append(task)

print("Your tasks for today:", daily_tasks)

first_task = input("Did you finish the first task? (yes/no): ")

if first_task.lower() == "yes":
    daily_tasks.remove(task)
    print("Good job! You finished your task.")
else:
    print("Try to finish it later.")

print(
    "Finally your data summary is:",
    "Name:", name.upper(),
    "Age:", age,
    "BMI:", bmi,
    "Your remaining tasks:", daily_tasks
)
