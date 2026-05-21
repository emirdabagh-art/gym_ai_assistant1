def calculate_bmi(weight, height):
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    return round(bmi, 2)


def calculate_daily_calories(weight, height, age, goal):
    bmr = 10 * weight + 6.25 * height - 5 * age + 5

    if goal == "fat loss":
        return int(bmr - 500)

    elif goal == "muscle gain":
        return int(bmr + 300)

    else:
        return int(bmr)


def recommend_workout_plan(goal):

    if goal == "fat loss":
        return "Cardio + Full Body Workout"

    elif goal == "muscle gain":
        return "Push Pull Legs Split"

    else:
        return "Balanced Maintenance Training"


print("AI Gym & Nutrition Assistant")
print("--------------------------------")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in cm: "))
goal = input("Enter your goal (fat loss / muscle gain / maintenance): ").lower()

bmi = calculate_bmi(weight, height)
calories = calculate_daily_calories(weight, height, age, goal)
workout = recommend_workout_plan(goal)

print("\nRESULT")
print("--------------------------------")
print(f"Name: {name}")
print(f"BMI: {bmi}")
print(f"Daily Calories: {calories}")
print(f"Workout Plan: {workout}")
