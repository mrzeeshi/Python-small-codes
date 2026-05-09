#Today we will deal with the Pandas that is the famous python library used to perform cleanin sorting and arranging operations on the data
#There is the concept of the dataframes here to perform the pandas operations on the data we first convert it into the dataframes
#The dataframe is like the 2d array
#Below are the practice questions done on the pandas library
#In order to run the pandas code you have to install it using this command --> pip install pandas

import pandas as pd
import random
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

#Thats enough for now and now in the next file I am going to make the program for the data entry for the students
#Hey wassup guys we are back and in this coding practice we will try to perform the cleaning operations on our dataframes.
#Cleaning the data is very important because the messy and the wrong data can lead to the invalid results.
#In order to clean the data we will be using the large dataset file having the thousands of lines of data and then we will perform the operations on that dataframe
#So we have our data set in a file named as the data.csv.

print()
df=pd.read_csv("data.csv")
print(df)
#This will print our complete dataset now if we want to print info about our dataset like number of rows columns and number of empty rows etc as shown below

print(df.info())

#Now we can see from the info that out dataset has some empty rows now either we can drop these empty rows or can we put some values in them
#Dropping some empty rows 
x=df.dropna()
print(x.info())

#Now you can see that it had dropped the rows but the changes are'nt made yet and to make the changes we also have to use some inplace true like as shown below
print("Before making changes i mean dropping rows : \n ")
df.info()
df.dropna(inplace=True)
print("After dropping the rows and making the changes \n ")
df.info()

#Now we will try to change datatype of the some columns as shown below
#Currently duration is int type and we will try to convert it to the float
df['Duration']=df['Duration'].astype(float)
df.info()

#You see from the output that we have converted the datatype of the duration from the int to float
print(df.head(20))

#Now we will try to edit or remove the values that seem to be incorrect like the workout.Nobody can do the workout of 300 minutes so we have to make it a random number that is in the range of 120 for every duration that is more than 120 minutes so we do it as follows
for i in df.index:
    if df.loc[i,"Duration"]>120:
        df.loc[i,"Duration"]=random.uniform(1,120)
print(df.to_string())

#Now you can see that no workout duration is more than the 120 minutes now if we want to make changes to file we write below code you can uncomment it 
# df.to_csv('data.csv',index=False)

#Now we will try to fill some details to the empty rows
df.fillna(random.uniform(1,50))
print(df.to_string())
#But as we had already droped the empty lines so it will not do entry as there are no empty rows
#And if we want to give the different values to the different collumns than we use the following code
df.fillna({'Duration':100,
           'Pulse':50},
           inplace=True)