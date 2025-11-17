# Objective:
# Students will understand how to create, modify, and access elements in Python lists.

# Topics Covered:
# Creating lists, indexing, slicing, appending, popping, sorting, reversing.

#collctions are usee t5oi store mulitple items in a string varible\
#Listes are ordered collectiojns of items 
# lists are matuble, meaning you can change thier content
# Lists are crerated using square brackets 

# Examples:

list_of_fruits = ["apple", "banana", "cherry", "date"]
print(list_of_fruits)
print(type(list_of_fruits))

print (list_of_fruits[0])
print (list_of_fruits[1])
print (list_of_fruits[-1])
print (list_of_fruits[1:3])

list_of_fruits.reverse()
print(list_of_fruits)
print(list_of_fruits[::-1])


list_of_fruits.append("elderberry")
print(list_of_fruits)
list_of_fruits.append("mango")
list_of_fruits.append("orange")
print(list_of_fruits)
list_of_fruits.extend(["fig","grape","honeydew"])
list_of_fruits.reverse()
print(list_of_fruits)


pooped_item = list_of_fruits.pop()
print(pooped_item)
print(list_of_fruits)

list_of_fruits.insert(1, "blueberry")
print(list_of_fruits)

list_of_fruits.remove("banana")
print(list_of_fruits)

list_of_fruits.insert(3, "pear")
print(list_of_fruits)

list_of_fruits.sort()
print(list_of_fruits)

list_of_items = list(range(1, 101))
print(list_of_items)
list_of_items = list(range(1, 1001))
print(list_of_items)
print(len(list_of_items))



set1 = {1,2,3,4}
set2 = {"apple", "banana", "cherry"}
print(set1)
print(set2)
print(type(set1))

set_with_duplicates = {1,2,2,3,4,4,5}
print(set_with_duplicates)

print(3 in set)
print(6 in set2)

truple1 = {1,2,3,4,5}
truple2 = ("apple","banana", "cherry")
print(truple1)
print(truple2)
print(type(truple1))


# my_list = ['apple', 'banana', 'cherry']
# print(my_list[0])         # apple
# print(my_list[1:])        # ['banana', 'cherry']

# my_list.append('grape')
# print(my_list)

# my_list.pop(1)
# print(my_list)

# numbers = [3, 1, 4, 2]
# numbers.sort()
# print(numbers)


# Practice Problems:

# Create a list with 5 of your favorite foods.

# Print the second and last item.

# Add a new item using .append().

# Remove the first item using .pop(0).

# Reverse your list using .reverse().

# Create a list of 3 lists (matrix), and access the middle element.