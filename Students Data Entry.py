import pandas as pd
print("Welcome to the students data entry software that gets the data like the \nstudent marks names ages etc and saves them to the file.")
data=pd.DataFrame({
    'No.':[],
    'Name':[],
    'Age':[],
    'Marks':[]
})
no=1
entries=int(input("How many entries you want to make?"))
file=open("data.txt","a")
for i in range(entries):
    name=input("Enter the name of student: ")
    age=int(input(f"what is the age of {name} : "))
    marks=int(input(f"enter the marks of {name} : "))
    data.loc[i]=[no,name,age,marks]
    no+=1
    file.write(f"{no},{name},{age},{marks}\n")
file.close()
print("Data saved to file successfully!")
print(f"data \n {data}")