# Assign a string to a variable and check its type
magic = 'HOCUS POCUS'
print(type(magic))

# Use the swapcase() string method to convert from caps to lowercase.
magic = 'HOCUS POCUS'
magic = magic.swapcase()
print(magic)

# Use the replace() string method to replace some letters with other letters
magic = magic.replace('cus','key')
print(magic)

# Use the split() string method to split the string into two strings.
magic = magic.split()
print(magic)

# Set up the cell to create the `planets` dataframe.
# (This cell was not shown in the instructional video.)
import pandas as pd
data = [['Mercury', 2440, 0], ['Venus', 6052, 0,], ['Earth', 6371, 1],
        ['Mars', 3390, 2], ['Jupiter', 69911, 80], ['Saturn', 58232, 83],
        ['Uranus', 25362, 27], ['Neptune', 24622, 14]
]

cols = ['Planet', 'radius_km', 'moons']

planets = pd.DataFrame(data, columns=cols)

# Display the planets dataframe
print(planets)

# Use the shape dataframe attribute to check the number of rows and columns.
print(planets.shape)

# Use the columns dataframe attribute to check column names.
print(planets.columns)