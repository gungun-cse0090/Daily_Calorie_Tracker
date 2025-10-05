#Task 1 — Setup & Welcome

# Name: Gungun
# Date: 05 Oct 2025
# Project: Daily Calorie Tracker CLI
 

#Task 2 — Input & Data Collection

print("Welcome to Daily Calorie Tracker!")
print("Track your meals, calories, and stay within your daily goal.\n")

meals = []
calories = []

n = int(input("How many meals did you have today? "))

for i in range(n):
    meal_name = input(f"Enter meal {i+1} name: ")
    calorie = float(input(f"Enter calories for {meal_name}: "))
    meals.append(meal_name)
    calories.append(calorie)

#Task 3 — Calorie Calculations

total_calories = sum(calories)
average_calories = total_calories / len(calories)
daily_limit = float(input("\nEnter your daily calorie limit: "))


#Task 4 — Limit Check

if total_calories > daily_limit:
    print("\n You have exceeded your daily calorie limit!")
else:
    print("\n Great! You are within your daily calorie goal.")



#Task 5 — Neatly Formatted Output


print("\nMeal Name\tCalories")
print("-" * 30)
for i in range(len(meals)):
    print(f"{meals[i]}\t\t{calories[i]}")
print("-" * 30)
print(f"Total:\t\t{total_calories}")
print(f"Average:\t{average_calories:.2f}")




# Bonus: Save session to file
save = input("Do you want to save this report? (yes/no): ").lower()

if save == "yes":
    f = open("calorie_log.txt", "a") 
    f.write("Your Daily Calorie Report\n")
    for i in range(len(meals)):
        f.write(f"{meals[i]}: {calories[i]} calories\n")
    f.write(f"Total: {total_calories}\n")
    f.write(f"Average: {average_calories:.2f}\n")
    if total_calories > daily_limit:
        f.write("Status: Exceeded limit!\n\n")
    else:
        f.write("Status: Within limit!\n\n")
    f.close()
    print(" Report saved in calorie_log.txt")
else:
    print("Report not saved.")



