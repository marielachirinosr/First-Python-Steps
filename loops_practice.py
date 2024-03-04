# Section 1: Counting with Break statement
i = 1
while True:
    print(i)
    user_input = input("Press Enter to continue, or 'stop' to quit: ").lower()
    if user_input == "stop":
        break
    i += 1
print("Done")


# Section 2: List Comprehension with User Input and Filtering
# Get a range from the user
start_num = int(input("Enter the starting number: "))
end_num = int(input("Enter the ending number: "))

# Filter even numbers using list comprehension
even_squares = [num ** 2 for num in range(start_num, end_num + 1) if num % 2 == 0]
print("Even squares:", even_squares)


# Section 3: Nested Loops with Customization and Data Analysis
# Get dimensions for the multiplication table from the user
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

# Print a nicely formatted table with headers
print("  ", end=" ")  # Align first row with numbers
for j in range(1, cols + 1):
    print(f"{j:<3}", end=" ") 
print()

for i in range(1, rows + 1):
    print(f"{i:<2}", end=" ")  
    for j in range(1, cols + 1):
        product = i * j
        print(f"{product:<3}", end=" ") 
    print()


# Section 4: Simple Car Games
started = False
print('Starting Car Game')
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started")
        else:
            started = True
            print("Car started")
    elif command == "stop":
        if not started:
            print("Car is already stopped")
        else:
            started = False
            print("Car stopped")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit
""")
    elif command == "quit":
        break
    else:
        print("I don't understand that")
