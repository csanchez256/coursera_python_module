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
