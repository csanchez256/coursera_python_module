# This code requests a number from the user and returns its factorial,
# printing each iteration of the multiplication.

"""
a = input(); y = 1

for i in range(int(a)):
    y = y*(i+1)
    print(y)

"""


# This function takes an integer as an input and returns its factorial.
def factorial(n):
    # Exclude 0 as product, start with 1
    y = 1
    for i in range(int(n)):
        y = y*(i+1)
        return y

"""

# Enter a numerical value between 1-9 in the command line that appears.
input_num = input()
# Apply factorial function to an integer input
print(factorial(input_num))

"""

# > checks for greater than
print( 10 > 1)

# == checks for equality
print("cat" == "dog")

# Letters that occur earlier in the alphabet evaluate to less than
print("Yellow" > "Cyan" and "Brown" > "Magenta")

# Or will return true if either side evaluates to true
print( 25 > 50 or 1 != 2)

# 'not' reverses Boolean evaluation of what follows it.
print( not 42 == "Answer")

