# Create a list of tuples, each representing the name, age, and position of a
# player on a basketball team.
team = [
    ('Marta', 20, 'center'),
    ('Ana', 22, 'point guard'),
    ('Gabi', 22, 'shooting guard'),
    ('Luz', 21, 'power forward'),
    ('Lorena', 19, 'small forward'),
    ]


# Create a function to extract and names and positions from the team list and
# format them to be printed. Returns a list.
def player_position(players):
    result = []
    for name, age, position in players:
        result.append('Name: {:>19} \nPosition: {:>15}\n'.format(name, position))

    return result


'''
note:  
>: This greater-than sign is an alignment operator. It specifies that the value should 
be right-aligned within the available space.

19: This number specifies the width of the field. The value will be placed in a field that is 
19 characters wide. If the value is shorter than 19 characters, it will be padded with spaces on the left to ensure it is right-aligned.

'''




# Loop over the list of formatted names and positions produced by 
# player_position() function and print them.
for player in player_position(team):
    print(player)


# Nested loops can produce the different combinations of pips (dots) in
# a set of dominoes.
# left and right are integers. They begin count at 0. So left starts at zero,
# ... then the inner for loop begins with "right" at zero, and continues until
# left equals "6" exclusive. Then it jumps back out to the outer loop, "left" is
# initialized to 1, and it begins all over
for left in range(7):
    for right in range(left, 7):
        print(f"[{left}|{right}]", end=" ")
    print('\n')


# Create a list of dominoes, with each domino reprented as a tuple.
dominoes = []
for left in range(7):
    for right in range(left, 7):
        dominoes.append((left, right))
dominoes


print(dominoes)
# Select index 1 of the tuple at index 4 in the list of dominoes.
# [index of list] [index of tuple]
print(dominoes[4][1])

# You can use a for loop to sum the pips on each domino and append
# the sum to a new list.
# This will flatten it out to a normal list of integers
pips_from_loop = []
for domino in dominoes:
    pips_from_loop.append(domino[0] + domino[1])
print(pips_from_loop)

# Alternatively you can do this!
# A list comprehension produces the same result with less code.
# This is basically set builder notation in math
pips_from_list_comp = [domino[0] + domino[1] for domino in dominoes]
pips_from_loop == pips_from_list_comp