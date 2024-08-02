# Assign a list containing players' ages.
age_list = [34, 25, 23, 19, 29]

# Find the maximum age and assign to `max_age` variable.
max_age = max(age_list)
print(max_age)

# Convert max_age to a string.
max_age = str(max_age)
print(max_age)

# Reassign the value of max_age
max_age = 'ninety-nine'
print(max_age)

#===============================
# Create precise variable names
#===============================

# Order of operations: prints 14
print( 2 * (3+4))

# prints 43
print( 3 + 4*10)

#============================
# Data types and conversions
#============================

# Addition of two strings
print("hello " + "world")

# Type checking
print( type("A"))
print(type(2))
print(type(2.0))

# Implicit conversion
print(type(1 + 2.5) )

# Explicit conversion: Str() function converts a number to a string
# Explicit means you are intentionally casting the numbers to a string using a build in function
print(" 2 + 2 = " + str(2+2) )