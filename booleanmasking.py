# NumPy and pandas are typically imported together.
# np and pd are conventional aliases.
import numpy as np
import pandas as pd

# Instantiate a dictionary of planetary data.
data = {'planet': ['Mercury', 'Venus', 'Earth', 'Mars',
                   'Jupiter', 'Saturn', 'Uranus', 'Neptune'],
       'radius_km': [2440, 6052, 6371, 3390, 69911, 58232,
                     25362, 24622],
       'moons': [0, 0, 1, 2, 80, 83, 27, 14]
        }
# Use pd.DataFrame() function to convert dictionary to dataframe.
planets = pd.DataFrame(data)
print(planets)

# Create a Boolean mask of planets with fewer than 20 moons.
mask = planets['moons'] < 20
print(mask)

# This is a way to query relevant information that you need.
print('Create a Boolean mask of planets with fewer than 20 moons.')
print(planets[mask])

# Create a Boolean mask of planets with fewer than 10 moons OR more than 50 moons.
mask = (planets['moons'] < 10) | (planets['moons'] > 50)
mask