# #In this file we will try to understand the some of the basic concepts of the file handling like reading,writing and appending the data to the files.....
# #We have a file named as the "demo.txt" and we will perform the actions on this file...
# #Writing to the file
# File=open("demo.txt","w")
# File.write("Hey, this is the first sentense written to the file.")
# File.close()

# #Reading the data from the file...
# File=open("demo.txt","r")
# File.read()
# File.close()
# #Now if I try to again write to the file the previous data will be erased...
# File=open("demo.txt","w")
# File.write("This is the new data added to the file and the previous data is overwrited....")
# File.close()

# File=open("demo.txt","r")
# File.read()
# File.close()

# #And now to avoid this issue we will use the "a" flag in the place of the "r" in order to avoid the overwriting and now the data is appended...
# File=open("demo.txt","a")
# for i in range(10):
#     File.write(f"\nThe {(i+1)}th line appended.")
# File.close()

#Now let's see whether the data is overwritten or appended....Data is appended as you will see in the output....
File=open("demo.txt","r")
File.read()
File.close()