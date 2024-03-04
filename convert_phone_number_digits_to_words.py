def convert_phone_digits(phone_number):

    digits_mapping = {
        "1": "One",
        "2": "Two",
        "3": "Three",
        "4": "Four",
        "5": "Five",
        "6": "Six",
        "7": "Seven",
        "8": "Eight",
        "9": "Nine",
        "0": "Zero"
    }

    output = ""
    for char in phone_number:
        if char.isdigit():  # Check if character is a digit
            output += digits_mapping.get(char, "?") + " "  # Use '?' for unknown digits
        else:
            return "Invalid input: Please enter a phone number with only digits."

    return output.rstrip()  # Remove trailing whitespace

if __name__ == "__main__":
    phone_number = input("Phone: ")
    converted_digits = convert_phone_digits(phone_number)
    print(converted_digits)
