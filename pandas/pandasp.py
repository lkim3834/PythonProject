# let us import the Pandas Library
import pandas as pd
#Define a dictionary 'x'

x = {'Name': ['Rose','John', 'Jane', 'Mary'], 'ID': [1, 2, 3, 4], 'Department': ['Architect Group', 'Software Group', 'Design Team', 'Infrastructure'], 
      'Salary':[100000, 80000, 50000, 60000]}

#casting the dictionary to a DataFrame
df = pd.DataFrame(x)

#display the result df
print(df)

#Retrieving the "ID" column and assigning it to a variable x
x = df[['ID']]
print(x)

#check the type of x
print(type(x))

z = df[['Department','Salary','ID']]
print(z)


##############loc and iloc#################
# indexed-based selecting method which means that we have to pass an integer index in the method to select a specific row/column.
print(df.iloc[0, 0])

# Access the column using the name

print(df.loc[0, 'Salary'])

# create the new df2 and  set the "Name" column as an index column using the method set_index().
df2=df
df2=df2.set_index("Name")
#To display the first 5 rows of new dataframe
print(df2.head())
#Now, let us access the column using the name
print(df2.loc['Jane', 'Salary'])


########### Slicing ######################
# let us do the slicing using old dataframe df
print(df)
# row would be 0 - 1 (2 is exclusive), column would be 0 - 2 (3 !exclusive)
print("slicing 0 to 2\n ", df.iloc[0:2, 0:3])
#let us do the slicing using loc() function on old dataframe df where index column is having labels as 0,1,2 ( !inclusive)
print(df.loc[0:2,'ID':'Department'])
#let us do the slicing using loc() function on new dataframe df2 where index column is Name having labels: Rose, John and Jane
print(df2.loc['Rose':'Jane', 'ID':'Department'])