# class animal:
#     def legs(self):
#         print("Has four legs..")
#     def makes_sound(self):
#         print("sound")
#     def eats(self):
#         print("food")
#     def type(self):
#         print("type")
# class dog(animal):
#     def makes_sound(self):
#         print("Dog says woof woof!")
#     def eats(self):
#         print("Dog eats Meat!")
#     def type(self):
#         print("Dog is a carnivore animal!")
# class cat(animal):
#     def makes_sound(self):
#         print("Cat says meow meow!!")
#     def eats(self):
#         print("Cat eats the cat food...")
#     def type(self):
#         print("Cat is carnivore...")
# class sparrow(animal):
#     def legs(self):
#         print("Sparrow has 2 legs...")
#     def eats(self):
#         print("Sparrow eats grains...")
#     def makes_sound(self):
#         print("Sparrow says chi chi !!!")
#     def type(self):
#         print("Sparrow is a bird...")

# animals=[dog(),cat(),sparrow()]
# for animall in animals:
#     animall.eats()
#     animall.legs()
#     animall.makes_sound()
#     animall.type()


#Now using these basic OOPs concepts we will try to make a library management system........
class person:
    def __init__(self,name,cellNo,email,type="",book_count=0):
        self.name=name
        self.cellNo=cellNo
        self.email=email
        self.type=type
        self.book_count=book_count
        self.books=["Mr.Chips","1983","Atomic Habbits","Rich Dad Poor Dad"]
    def add_book(self,book):
        self.books.append(book)
        self.book_count=len(self.books)
    def see_books(self):
        for book in self.books:
            print(book)
    def see_profile(self):
        print(f"Name: {self.name} \n Cell No: {self.cellNo} \n Email: {self.email} \nType: {self.type}")
    def borrow_books(self,bookname):
        if bookname in self.books:
            print(f"{bookname} issued successfully!!!")
            self.book_count-=1
        else:
            print(f"Sorry {bookname} isn't present in our library...")
class librarian(person):
    def __init__(self, name, cellNo, email, type):
        super().__init__(name, cellNo, email, type)
class student(person):
    def __init__(self, name, cellNo, email, type):
        super().__init__(name, cellNo, email, type)
    def return_book(self,book):
        self.books.append(book)
        self.book_count+=1
        print(f"{book} returned successfully...")


print("Library ...................")
name=input("What is your name? ")
cell_no=input("What is your cell phone number ?")
email=input("What is your email ?")
print("Who you are? \n 1.Librarian \n 2.Student")
choice=int(input("enter your choice..."))
if choice==1:
    type="Librarian"
    librarian1=librarian(name,cell_no,email,type)
    librariann=True
    while librariann:
        print("1.See Profile  \n 2.Add Books \n 3.See All Books \n 4.Exit")
        librarian_choice=int(input("Enter the corresponding number for you services....."))
        if librarian_choice==1:
            librarian1.see_profile()
        elif librarian_choice==2:
            book=input("Enter the name of book you want to add...")
            librarian1.add_book(book)
            continue
        elif librarian_choice==3:
            librarian1.see_books()
            continue
        elif librarian_choice==4:
            print("Exiting.....")
            librariann=False
        else:
            print("Invalid choice...Put a  valid one.........")
            continue
elif choice==2:
    type="student"
    student1=student(name,cell_no,email,type)
    studentt=True
    while studentt:
        print("1.See Profile \n 2.See All Books \n 3.Borrow A Book \n 4.Return A Book 5.Exit")
        student_choice=int(input("Enter Your Choice....."))
        if student_choice==1:
            student1.see_profile()
            continue
        elif student_choice==2:
            student1.see_books()
            continue
        elif student_choice==3:
            borrowing_book=input("Enter the name of book you want to borrow...")
            student1.borrow_books(borrowing_book)
            continue
        elif student_choice==4:
            returned_book=input("Enter the name of book you are returning...")
            student1.add_book(returned_book)
            continue
        elif student_choice==5:
            print("Exiting from the library........")
            studentt=False
        else:
            print("Invalid Choice...Enter a valid one.........")
            continue
else:
    print("Invalid Choice ......Put a valid choice.....")