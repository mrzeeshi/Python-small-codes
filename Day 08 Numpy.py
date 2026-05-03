# Today in this python file we will play with the numpy library.
# The numpy is the famous python library that is used to perform the numerical operations on the heavy amount of the data.
# We use the numpy because the lists when large amount of data is stored in them become too slow
# This is the basic practice file in which we will try to make the arrays using the numpy

import numpy as np
import random
arr=np.array([1,2,3,4,5,6])
print(arr)

#Now if we want to make an array of any size which has only zeros
zero_array=np.zeros((3,3))
print("The 3x3 array having only zeroes... \n",zero_array)


#Now we will make the array that has only ones....
print("The 2x3 array with only having the ones...\n",np.ones((2,3)))

#Now we will try to make the array with a range and constant increment on each value...
print()
print("The array from 0 to 10 with 2 incremet on each element...\n ", np.arange(0,10,2))

#Now the array of any size having the diagonal as 1s
print()
print("The array of size 3x3 having diagonal as one...\n",np.eye(3))

#Now we will try to make an array of n equal steps...
print()
print("An array of 5 equal steps...\n",np.linspace(0,10,5))

#Now finding the dimensions of an array...
print("\n The array having the dimensions...\n ",zero_array,"\n Dimensions: ",zero_array.shape)

#Now giving the size of an array.....
print(f"\nThe size of \n{zero_array} is {zero_array.size}")

#Now we will try to change the shape of an array
print("\n Reshaping the array...")
print(f"\n Array Before: \n{arr}\n Array After: \n {arr.reshape(2,3)}")

#The next main topic in the numpy library is the indexing and slicing,like some of the operations performed on the numpy arrays
arrr=np.array([1,2,3,4,5,6])
new_array=arrr[1:3]
print(f"The original array :{arrr} \n New array by slicing: {new_array}")

print(f"Now if we try to change any elements of {new_array} it will make the changes to our original array {arr}z\n and it is given below the "
      "first index of the both arrays will be set to 99 when it is changed in new array")
new_array[0]=99
print(f"The original array : {arr} \n The array whose index was changed : {new_array} and now after change the original array: {arrr}")
print("Now to avoid that issue of coming change in the original array if new array sliced from it is changed is due to the fact that the "
      "new array we make by slicing is actualy the referance of the original array so both are changed and this issue we can handle by using the "
      " copy method of the numpy library.")
new_array2=arrr[1:3].copy()
print(f"Now the original array is {arr} and the new of its copy is {new_array2} \n now making the index 0 of copy equal to 1 \n let's see what happens"
      f" {new_array2}")


# Now as the practice we will try to make the tik tak toe game

tic_tac_toe = np.array([1,2,3,4,5,6,7,8,9])
tic_tac_toe = tic_tac_toe.reshape(3,3)

print("="*20)
print("TIC TAC TOE GAME...")
print("You = 0 | Computer = 1")
print("Choose box number (1-9)")

while True:
    print("\n")
    print(tic_tac_toe)

    # WIN CONDITIONS (Computer = 1)
    if ((tic_tac_toe[0,0]==1 and tic_tac_toe[1,0]==1 and tic_tac_toe[2,0]==1) or
        (tic_tac_toe[0,0]==1 and tic_tac_toe[0,1]==1 and tic_tac_toe[0,2]==1) or
        (tic_tac_toe[1,0]==1 and tic_tac_toe[1,1]==1 and tic_tac_toe[1,2]==1) or
        (tic_tac_toe[2,0]==1 and tic_tac_toe[2,1]==1 and tic_tac_toe[2,2]==1) or
        (tic_tac_toe[0,0]==1 and tic_tac_toe[1,1]==1 and tic_tac_toe[2,2]==1)):
        print("Computer Won!")
        break

    # WIN CONDITIONS (User = 0)
    elif ((tic_tac_toe[0,0]==0 and tic_tac_toe[1,0]==0 and tic_tac_toe[2,0]==0) or
          (tic_tac_toe[0,0]==0 and tic_tac_toe[0,1]==0 and tic_tac_toe[0,2]==0) or
          (tic_tac_toe[1,0]==0 and tic_tac_toe[1,1]==0 and tic_tac_toe[1,2]==0) or
          (tic_tac_toe[2,0]==0 and tic_tac_toe[2,1]==0 and tic_tac_toe[2,2]==0) or
          (tic_tac_toe[0,0]==0 and tic_tac_toe[1,1]==0 and tic_tac_toe[2,2]==0)):
        print("You Won!")
        break

    # CHECK DRAW
    elif np.all((tic_tac_toe == 0) | (tic_tac_toe == 1)):
        print("Game Draw!")
        break

    # ================= USER MOVE =================
    while True:
        try:
            user = int(input("Enter position (1-9): "))

            # mapping manual (your style)
            if user == 1 and tic_tac_toe[0,0] not in [0,1]:
                tic_tac_toe[0,0] = 0
                break
            elif user == 2 and tic_tac_toe[0,1] not in [0,1]:
                tic_tac_toe[0,1] = 0
                break
            elif user == 3 and tic_tac_toe[0,2] not in [0,1]:
                tic_tac_toe[0,2] = 0
                break
            elif user == 4 and tic_tac_toe[1,0] not in [0,1]:
                tic_tac_toe[1,0] = 0
                break
            elif user == 5 and tic_tac_toe[1,1] not in [0,1]:
                tic_tac_toe[1,1] = 0
                break
            elif user == 6 and tic_tac_toe[1,2] not in [0,1]:
                tic_tac_toe[1,2] = 0
                break
            elif user == 7 and tic_tac_toe[2,0] not in [0,1]:
                tic_tac_toe[2,0] = 0
                break
            elif user == 8 and tic_tac_toe[2,1] not in [0,1]:
                tic_tac_toe[2,1] = 0
                break
            elif user == 9 and tic_tac_toe[2,2] not in [0,1]:
                tic_tac_toe[2,2] = 0
                break
            else:
                print("Invalid move! Try again.")

        except:
            print("Enter a valid number!")

    # ================= COMPUTER MOVE =================
    while True:
        myNo = random.randint(1,9)

        if myNo == 1 and tic_tac_toe[0,0] not in [0,1]:
            tic_tac_toe[0,0] = 1
            break
        elif myNo == 2 and tic_tac_toe[0,1] not in [0,1]:
            tic_tac_toe[0,1] = 1
            break
        elif myNo == 3 and tic_tac_toe[0,2] not in [0,1]:
            tic_tac_toe[0,2] = 1
            break
        elif myNo == 4 and tic_tac_toe[1,0] not in [0,1]:
            tic_tac_toe[1,0] = 1
            break
        elif myNo == 5 and tic_tac_toe[1,1] not in [0,1]:
            tic_tac_toe[1,1] = 1
            break
        elif myNo == 6 and tic_tac_toe[1,2] not in [0,1]:
            tic_tac_toe[1,2] = 1
            break
        elif myNo == 7 and tic_tac_toe[2,0] not in [0,1]:
            tic_tac_toe[2,0] = 1
            break
        elif myNo == 8 and tic_tac_toe[2,1] not in [0,1]:
            tic_tac_toe[2,1] = 1
            break
        elif myNo == 9 and tic_tac_toe[2,2] not in [0,1]:
            tic_tac_toe[2,2] = 1
            break
        