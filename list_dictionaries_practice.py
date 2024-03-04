# Section 1: Lists
# Accessing and modifying list elements
names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
names[0] = 'Jon'  
print(f"First name after modification: {names[0]}")
print(f"Names from index 2 onwards: {names[2:]}")
print(f"Full list: {names}")

# Finding the maximum value
numbers = [3, 6, 2, 8, 4, 10]
largest_number = max(numbers) 
print(f"The largest number in the list: {largest_number}")


# Section 2: 2D Lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(f"Element at row 0, column 1: {matrix[0][1]}")

for row in matrix:
    for item in row:
        print(item, end=" ")  
    print() 


# Section 3: List Methods
numbers = [5, 2, 1, 5, 7, 4]
sorted_copy = numbers.copy().sort() 
print(f"Sorted list (copy): {numbers.copy().sort()}") 

numbers.append(20) 
numbers.insert(0, 10)

print(f"List after modifications: {numbers}")

# - numbers.remove(7)  # Remove the first occurrence of 7
# - numbers.pop()  # Remove the last element
# - numbers.clear()  # Remove all elements

print(f"Is 50 in the list: {50 in numbers}")
print(f"Frequency of 5 in the list: {numbers.count(5)}")

# Removing duplicates
numbers = [2, 2, 4, 6, 3, 4, 6, 1]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(f"List with duplicates removed: {uniques}")


#Section 4: Tuples
numbers = (1, 2, 3)
print(f"First element in the tuple: {numbers[0]}")

# Unpacking tuples
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
fruits, *rest = thistuple 
print(f"First two fruits: {fruits}")
print(f"Remaining fruits: {rest}")


#Section 5: Dictionaries
customer = {
    "name": "Mary",
    "age": 30,
    "is_verified": True
}

print(f"Customer's name: {customer['name']}")
print(f"Customer's birthdate: {customer.get('birthdate', '1 Jan 2000')}")
