# Objective:
# Students will use logical (and, or, not) and chained comparison operators in Python to build compound conditions.

# Key Notes:

# and → Both conditions must be True

# or → At least one condition must be True

# not → Inverts True/False

# You can chain comparisons: 1 < x < 5

# Examples:
x = 10
print(x > 5 and x < 15)   # True
print(x < 5 or x == 10)   # True
print(not(x == 10))       # False
print(1 < x < 20)         # True


# Practice Problems:
score = 89

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")


# Write an expression that checks if a number is between 50 and 100 (inclusive).
number = 76
50 <= number <= 100

# Write an expression that checks if a number is NOT equal to 0 and greater than 10.
number = 15

if number != 0 and number > 10:
    print("Number is not zero and greater than 10.")
else:
    print("Condition not met.")

# Use chained comparison to check if 3 < 4 < 5.
if 3 < 4 < 5:
    print("True.")
else:
    print("False.")

# Challenge: Create a password rule using logical operators:
password = "my@securepass"

if len(password) >= 8 and "@" in password and password != "password123":
    print("Password is valid!")
else:
    print("Password does not meet the rules.")

