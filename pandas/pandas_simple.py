#First of all we will see that how can we make the dataframes and this is very simple and shown below
import pandas as pd
first_df=pd.DataFrame({
    "Roll No":[1,2,3,4],
    "Name":["Zeeshan ","Ali ", "Ahmad ", "Hassan"],
    "Biology":[23,45,34,25],
    "Maths":[22,43,55,22],
    "Computer Science":[55,32,77,33]
})
print(first_df.to_string)

#Now we will try to enter the new column.So
first_df["Total"]=[0,0,0,0]
print(first_df.to_string)

#Now we will try to enter some of the values into the column that is based on some of the functions like here the total marks
for i in first_df.index:
    first_df.loc[i,"Total"]=first_df.loc[i,"Biology"]+first_df.loc[i,"Maths"]+first_df.loc[i,"Computer Science"]
print(first_df.to_string)

#Now we will try to use the concepts of the pandas so far learned concepts and will try to build the mini project of a schools result making system


print("=" * 50)
print("||"," "*44,"||")
print("=" * 50)