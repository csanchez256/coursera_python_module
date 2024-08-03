# Create a dictionary with pens as keys and the animals they contain as values.
# Dictionaries can be instantiated using braces.
zoo = {
    'pen_1': 'penguins',
    'pen_2': 'zebras',
    'pen_3': 'lions',
    }

# Selecting the `pen_2` key returns `zebras`, the value stored at that key.
zoo['pen_2']

# You can't access values the same way. This produces an error
# zoo['zebras']


# Dictionaries can also be instantiated using the dict() function.
zoo = dict(
    pen_1='monkeys',
    pen_2='zebras',
    pen_3='lions',
    )

print ( zoo['pen_2'] )

# Dictionaries are unordered and do not support numerical indexing. This throws an error.
# zoo[2]


# Create a lists of tuples, each representing the name, age, and position of a 
# Player
team = [
    ('Marta', 20, 'center'),
    ('Ana', 22, 'point guard'),
    ('Gabi', 22, 'shooting guard'),
    ('Luz', 21, 'power forward'),
    ('Lorena', 19, 'small forward'),
    ('Sandra', 19, 'center'),
    ('Mari', 18, 'point guard'),
    ('Esme', 18, 'shooting guard'),
    ('Lin', 18, 'power forward'),
    ('Sol', 19, 'small forward'),
    ]

# Instatiate an empty dictionary.
new_team = {}

# Loop over the tuples in the list of players and upack their values
# It already knows we're iterating on three things in each dictionary entry
# ...because team is defined already. Each record has three items.
# Notice the iterator is "team". It would throw an error with a dictionary that
# has a different structure.

for name, age, position in team:
    if position in new_team:
        new_team[position].append((name, age))
    else:
        new_team[position] = [(name,age)]

print(new_team)

# In words: "check if there's a position for this already, otherwise set that player's position"

# Exampine the value at the 'point guard' key.
print ( new_team['point guard'] )

# You can access the dictionary's keys by looping
for x in new_team:
    print(x)

# The items() method returns both the keys and the values.
for a, b in new_team.items():
    print(a, b)
