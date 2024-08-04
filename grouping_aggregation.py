import numpy as np
import pandas as pd

# Instantiate a dictionary of planetary data.
data = {'planet': ['Mercury', 'Venus', 'Earth', 'Mars',
                   'Jupiter', 'Saturn', 'Uranus', 'Neptune'],
        'radius_km': [2440, 6052, 6371, 3390, 69911, 58232,
                     25362, 24622],
        'moons': [0, 0, 1, 2, 80, 83, 27, 14],
        'type': ['terrestrial', 'terrestrial', 'terrestrial', 'terrestrial',
                 'gas giant', 'gas giant', 'ice giant', 'ice giant'],
        'rings': ['no', 'no', 'no', 'no', 'yes', 'yes', 'yes','yes'],
        'mean_temp_c': [167, 464, 15, -65, -110, -140, -195, -200],
        'magnetic_field': ['yes', 'no', 'yes', 'no', 'yes', 'yes', 'yes', 'yes']
        }

# Use pd.DataFrame() function to convert dictionary to dataframe.
planets = pd.DataFrame(data)
planets

# The groupby() function returns a groupby object.
print ( planets.groupby(['type']) )

# Apply the sum() function to the groupby object to get the sum
# of the values in each numerical column for each group.
planets.groupby(['type']).sum()


# Apply the sum function to the groupby object and select
# only the 'moons' column.
planets.groupby(['type']).sum()[['moons']]

# Group by type and magnetic_field and get the mean of the values
# in the numeric columns for each group.
planets.groupby(['type', 'magnetic_field']).mean()

# Group by type, then use the agg() function to get the mean and median
# of the values in the numeric columns for each group.
planets.groupby(['type']).agg(['mean', 'median'])