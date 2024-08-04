# NumPy and pandas are typically imported together.
# np and pd are conventional aliases.
import numpy as np
import pandas as pd

# read in data from a .csv file.
dataframe = pd.read_csv('C:\\Users\\css7c\\OneDrive\\Desktop\\Coursera Data Analytics Certificate\\COURSE 2 - PYTHON PROGRAMMING\\train.csv')

# Print the first 25 rows.
print ( dataframe.head(25) )

# Calculate the mean of the Age column.
dataframe['Age'].mean()
dataframe['Age'].max()

print ( dataframe.describe() )

# Filter the data to return only rows where value in Age column is greater than 60
# and value in Pclass column equals 3.
dataframe[ (dataframe['Age'] > 60 ) & (dataframe['Pclass'] ==  3)]

# Use iloc to access data using index numbers.
# Select row 1, column 3.
#dataframe.iloc[1][3]


# Group customers by Sex and Pclass and calculate the total paid for each group
# and the mean price paid for each group.
fare = dataframe.groupby( ['Sex', 'Pclass']).agg( {'Fare': ['count', 'sum']})
fare['fare_avg'] = fare['Fare']['sum'] / fare['Fare']['count']
print(fare)

import pandas as pd

# Use pd.DataFrame() function to create a dataframe from a dictionary.
data = {'col1': [1, 2], 'col2': [3, 4]}
df = pd.DataFrame(data=data)
print(df)

# Use pd.DataFrame() function to create a dataframe from a NumPy array.
df2 = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                   columns=['a', 'b', 'c'], index=['x', 'y', 'z'])
print(df2)

# Use pd.read_csv() function to create a dataframe from a .csv file
# from a URL or filepath.
df3 = pd.read_csv('C:\\Users\\css7c\\OneDrive\\Desktop\\Coursera Data Analytics Certificate\\COURSE 2 - PYTHON PROGRAMMING\\train.csv')
print ( df3.head() )

# Print class of first row
print(type(df3.iloc[0]))

# Print class of "Name" column
print(type(df3['Name']))

# Create a copy of df3 named 'titanic'
titanic = df3
# The head() method outputs the first 5 rows of dataframe.
print (titanic.head())

print( titanic.shape)
print ( titanic.info())

'''
In the Python Pandas library, .iloc[] is an indexer used for integer-location-based 
indexing of data in a DataFrame. It allows users to select specific rows and columns 
by providing integer indices, making it a valuable tool for data manipulation and extraction 
based on numerical positions within the DataFrame. This indexer is particularly useful when 
you want to access or manipulate data using integer-based positional indexing rather than 
labels.
'''
print('Use iloc to return a series object of the data in row 0: \n')
# Use iloc to return a Series object of the data in row 0.
# Basically this just tabulates (makes a data frame) from the first 'row' 'record' 'observation'
# Or whatever you like to call it
print(titanic.iloc[0])

# Use iloc to return a DataFrame view of the data in row 0.
print(titanic.iloc[[0]])

# Use iloc to ruetnr a DataFrame view of the data in rows 0,1,2.
print(titanic.iloc[0:3])








