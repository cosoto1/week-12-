
list1 = [1,2,3]
print(list1[-1])
list2 = [4,5,6]
print(list2[0])
nested_list = [list1, list2]
print(nested_list[0])
print(nested_list[1])
print(nested_list[1][1])
print(nested_list[1][0])


fruits = ["apple", "orange", "banana", "coconut"]
veggies = ["celery", "carrots", "potatoes"]
meats = ["chiecken", "fish", "turkey"]

groceries = [fruits, veggies, meats]
print(groceries[1][1])

for collections in groceries:
    for food in collections:
        print(food, end="")

#nested loops
for i in range(1,1001):
    for j in range(1,1001):
        if i > 0 and j > 0:
          for k in range(1, 1001):
            print("the number is ", i)

# Objective:
# Students will manipulate nested lists and understand basic list comprehensions.

# Key Notes:

# A list can contain other lists.

# List comprehensions provide a concise way to create lists.

# Examples:Objective:
# Students will manipulate nested lists and understand basic list comprehensions.

# Key Notes:

# A list can contain other lists.

# List comprehensions provide a concise way to create lists.

# Examples:

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[1][2])    # 6

# List comprehension

# Practice Problems:

# Build a matrix variable containing 3 lists of 3 numbers each.

# Print the first list.
print(matrix[0])

# Print the second item from the third list.
print(matrix[2][1])

# Use a list comprehension to extract the last item from each sub-list.
sum_list =[row[-1] for row in matrix]
print(sum_list)

# Challenge: Create a new list containing squares of numbers from 1–10 using a comprehension.
squares = [x**2 for x in range (1,11)]
print(squares)

