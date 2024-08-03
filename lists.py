# Assign a list using brackets, with elements separated by commas.
x = ["Now", "we", "are", "cooking", "with", 7, "ingredients"]

# Access part of a list by slicing
x[1:3]

# Omitt the first value of the slice, implies a vlalue of 0.
print (x[:2])

# Omitting the last value of the slice implies a value of len(list)
print (x[2:])

# The `in` keyword lets you check if a value is contained in the list.
x = ["Now", "we", "are", "cooking", "with", 7, "ingredients"]
print ("This" in x)

# Modify contents of a list
# Note it's zero intexed
fruits = ['Pineapple', 'Banana', 'Apple', 'Melon']
fruits.insert(1, 'Orange')
print(fruits)

# The pop() method removes the element at a given index and returns it.
# If no index is given, it removes and returns the last element.
fruits.pop(2)
print(fruits)

