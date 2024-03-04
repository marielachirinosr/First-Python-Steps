# Section 1: User Information
user_name = input("What is your name? ")
favorite_color = input("What is your favorite color? ")
print(f"{user_name} likes {favorite_color}")


# Section 2: Age Calculation
from datetime import datetime

birth_year = input("Enter your birth year: ")
birth_month = input("Enter your birth month (1-12): ")

current_date = datetime.now()
current_year = current_date.year
current_month = current_date.month

user_age = current_year - int(birth_year) - (1 if current_month < int(birth_month) else 0)
print(f"You are {user_age} years old.")


# Section 3: Weight Conversion
weight_lbs = input("Enter your weight in pounds: ")
weight_kg = int(weight_lbs) * 0.45
print(f"Your weight in kilograms is {weight_kg:.2f} kg.")