def calculate_grade(avg):
    if avg >= 85:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 50:
        return "C"
    else:
        return "F"


def add_student(students):
    name = input("Enter student name: ")
    marks = []

    for i in range(3):
        m = float(input(f"Enter marks for subject {i+1}: "))
        marks.append(m)

    avg = sum(marks) / len(marks)
    grade = calculate_grade(avg)

    students.append({
        "name": name,
        "marks": marks,
        "average": avg,
        "grade": grade
    })

    print("Student added successfully!\n")


def show_all(students):
    if not students:
        print("No students found.\n")
        return

    print("\n--- Student Records ---")
    for s in students:
        print(f"{s['name']} | Avg: {round(s['average'],2)} | Grade: {s['grade']}")
    print()


def search_student(students):
    name = input("Enter name to search: ").lower()

    for s in students:
        if s["name"].lower() == name:
            print(f"Found: {s['name']} | Marks: {s['marks']} | Grade: {s['grade']}\n")
            return

    print("Student not found.\n")


def top_student(students):
    if not students:
        print("No data available.\n")
        return

    top = students[0]

    for s in students:
        if s["average"] > top["average"]:
            top = s

    print(f"Top Student: {top['name']} with Avg {round(top['average'],2)}\n")


def main():
    students = []

    while True:
        print("1. Add Student")
        print("2. Show All")
        print("3. Search Student")
        print("4. Top Student")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            show_all(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            top_student(students)
        elif choice == "5":
            print("Good luck with exams!")
            break
        else:
            print("Invalid choice\n")


main()