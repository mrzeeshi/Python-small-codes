#Today we will deal with the Pandas that is the famous python library used to perform cleanin sorting and arranging operations on the data
#There is the concept of the dataframes here to perform the pandas operations on the data we first convert it into the dataframes
#The dataframe is like the 2d array
#Below are the practice questions done on the pandas library
#In order to run the pandas code you have to install it using this command --> pip install pandas

import pandas as pd
first_data=pd.DataFrame({
    'Names':["Ali","Zeeshan","Roshan"],
    'Ages':[20,30,23],
    'Salaries':[20000,30000,40000]
})
print(first_data)

#Now our first data frame is being created and now we will use some pandas functions on it like
print(f"The frist line: \n{first_data.loc[0]}")
print(f"Printing only the names column: \n{first_data['Names']}")

#We can also add the new rows and columns to out datasets by the  ways that is given below
first_data.loc[3] = ["Mazhar", 28, 35000]
first_data.loc[4] = ["Tahir", 20, 30000]
first_data.loc[5] = ["Sammar", 18, 25000]

print("Our dataset after adding the three new lines: \n ",first_data)
#We can also add a column as given below
first_data['Heights']=[7.6,5,6,5.3,7,5.6]
print("Our dataset after adding the new column named as Heights: \n",first_data)

#Now we can also use some filters like 
print("Names and salaries of individuals whose salaries are greater than 30000: \n",first_data.loc[first_data['Salaries']>30000,['Names','Salaries']])

#Now we will try to update the values
first_data.loc[first_data['Salaries'] > 20000, 'Salaries'] = first_data['Salaries'] + 5000
print("The persons who have the ages greater than 20 will get the increment of 5000 in their salaries: \n",first_data)