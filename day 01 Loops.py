# ---------------------- Loops Practice File ----------------------
#Practicing the questions on the LOOPS...
#hello there whats going on here
print("Practicing the basic loops concepts...")
# 1. Printing natural numbers from 0 to 10
for i in range(11):
    print(i)


# 2. Prime and non-prime numbers from 1 to 100
for i in range(1, 100):
    count = 2
    is_prime = True

    if i <= 1:
        continue

    while count * count <= i:
        if i % count == 0:
            is_prime = False
            break
        count += 1

    if is_prime:
        print(i, "is a prime number!")
    else:
        print(i, "is not a prime number!")


# 3. Patterns

# *
# **
# ***
# ****
# *****
for i in range(5):
    print("*" * (i + 1))


#     *
#    ***
#   *****
#  *******
# *********
rows = 5
cols = 1

for i in range(rows):
    print(" " * (rows - i), "*" * cols, sep="")
    cols += 2


#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *
rows = 5
cols = 1

for i in range(rows):
    print(" " * (rows - i), "*" * cols, sep="")
    cols += 2

cols -= 2  # adjust before decreasing pattern

for i in range(rows):
    cols -= 2
    print(" " * (i + 1), "*" * cols, sep="")


# 4. Largest and smallest in a list
numbers = [3, 4, 6, 4, 3, 6, 7, 8654, 3, 3, 5]

largest = numbers[0]
smallest = numbers[0]

for i in range(len(numbers)):
    if numbers[i] > largest:
        largest = numbers[i]
    if numbers[i] < smallest:
        smallest = numbers[i]

print("Largest Number:", largest)
print("Smallest Number:", smallest)


# 5. Count each character in a word
word = input("Enter a word to find count of each character: ")
visited = []

for alphabet in word:
    if alphabet in visited:
        continue

    visited.append(alphabet)
    word_count = 0

    for char in word:
        if char == alphabet:
            word_count += 1

    print(f"Count of '{alphabet}' in '{word}' is {word_count}")


# 6. Floyd Triangle
rows = 5
counter = 1

for row in range(rows):
    col = 0
    while col <= row:
        print(counter, end=" ")
        counter += 1
        col += 1
    print()
#7. Printing all the even numbers from 1 to 100
for i in range(1, 101):
    if i % 2 == 0:
        print(i)
    else:
        continue