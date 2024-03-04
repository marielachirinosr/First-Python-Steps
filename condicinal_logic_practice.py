# Section 1: Weather Report
def check_weather():
    while True:  # Loop until valid input is received
        weather_input = input("Is it hot or cold today? Please enter 'hot' or 'cold': ").strip().lower()

        if weather_input in ('hot', 'cold'):
            if weather_input == 'hot':
                is_hot = True
                is_cold = False
            else:
                is_hot = False
                is_cold = True
            break  # Exit the loop if valid input is received
        else:
            print("Invalid input. Please enter 'hot' or 'cold'.")

    return is_hot, is_cold

is_hot, is_cold = check_weather()

if is_hot:
    print("It's a hot day.")
    print("Make sure to stay hydrated!")
elif is_cold:
    print("It's a cool day.")
    print("Don't forget to wear warm clothes.")
else:
    print("It's impossible to determine the weather today due to invalid input.")  # Message for invalid input
print("Enjoy your day!")


# Section 2: House Price Calculation
house_price = 1000000
has_good_credit = input("Do you have good credit? (True/False): ").lower() == 'true'

if has_good_credit:
    down_payment_percentage = 0.1
else:
    down_payment_percentage = 0.2

down_payment = down_payment_percentage * house_price
print(f"Down payment: ${down_payment}")

has_high_income = input("Do you have a high income? (True/False): ").lower() == 'true'
has_good_credit = input("Do you have good credit? (True/False): ").lower() == 'true'
has_criminal_record = input("Do you have a criminal record? (True/False): ").lower() == 'true'

if has_high_income and has_good_credit and has_criminal_record:
    print("Based on your income and credit history, you may not be eligible for a loan at this time.")
else:
    print("Based on your income and credit history, you may be eligible for a loan.")


# Section 3: Temperature Check
temperature = int(input("What is the temperature today? Enter a number: "))

if temperature > 30:
    print("It's a hot day.")
else:
    print("It's not a hot day.")


# Section 4: Name Validation
user_name = input("Enter your name: ")

if len(user_name) < 3:
    print("Name must be at least 3 characters.")
elif len(user_name) > 50:
    print("Name can be a maximum of 50 characters.")
else:
    print("Name looks good!")


# Section 5: Weight Conversion
user_weight = int(input("Enter your weight: "))
weight_unit = input('(L)bs or (K)g: ')

if weight_unit.upper() == "L":
    converted_weight = user_weight * 0.45
    print(f"You weigh {converted_weight} kilograms.")
else:
    converted_weight = user_weight / 0.45
    print(f"You weigh {converted_weight} pounds.")
