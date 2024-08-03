# User format() method to insert values into your string, indicated by braces.
name = 'Manuel'
number = 3
print('Hello {}, your lucky number is {}.'.format(name, number))

# Example inserting prices into string
price = 7.75
with_tax = price * 1.07

# Use :.2f to round a float value to a two places beyond the decimal.
print('Base price: ${:.2f} USD. \nWith tax: ${:.2f} USD.'.format(price, with_tax))

# Using the range() function, it takes three arguments: start, stop, step
for even_num in range(2,11,2):
    print (even_num)


# The format method inserts specific substrings into designated places withing  a larger string.

x = 'values'
y = 100

print('''String formatting lets you insert {} into strings.
      they can even be numbers, like {}. '''.format(x,y))

# Another example
var_a = 'A'
var_b = 'B'
print('{a}, {b}'.format(a=var_a, b=var_b))

# You can also include the arguments’ index numbers within the braces to indicate which arguments get inserted in specific spots:
var_a = 'A'
var_b = 'B'
print('{1}, {0}'.format(var_a, var_b))
print('{0}, {1}'.format(var_a, var_b))

# Lieteral string interpolation (f-strings). This is much simpler syntax
var_a = 1
var_b = 2
print(f'{var_a} + {var_b}')
print(f'{var_a + var_b}')
print(f'var_a = {var_a} \nvar_b = {var_b}')

# Float formatting
num = 1000.987123
f'{num:.2f}'

'''
{float:.2f} translates as:
1-<float> 
2-colon <:>
3-precision <.2>
4-presentation type <f>

'''

# For example scientific notation
num = 1000.987123
print(f'{num:.3e}')

# Or percentage
decimal = 0.2497856
print(f'{decimal:.4%}')

# Partitioning can be usefule for web scraping
my_string = 'https://www.google.com/'
print( my_string.partition('.'))

# replace 
my_string = 'https://www.google.com/'
print(my_string.replace('google', 'youtube'))

# regular expressions
import re
my_string = 'Three sad tigers swallowed wheat in a wheat field'
print (re.search('wall', my_string))