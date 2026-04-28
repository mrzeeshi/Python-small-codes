FILE_NAME = "demo.txt"


def add_note():
    note = input("Enter your note: ")

    with open(FILE_NAME, "a") as file:
        file.write(note + "\n")

    print("Note saved successfully.")


def view_notes():
    try:
        with open(FILE_NAME, "r") as file:
            content = file.read()
            if content:
                print("\nYour Notes:")
                print(content)
            else:
                print("No notes available.")
    except FileNotFoundError:
        print("File does not exist yet.")


def search_note():
    word = input("Enter a word to search: ")

    try:
        with open(FILE_NAME, "r") as file:
            found = False
            for line in file:
                if word.lower() in line.lower():
                    print(line.strip())
                    found = True

            if not found:
                print("No matching notes found.")
    except FileNotFoundError:
        print("File does not exist yet.")


def menu():
    while True:
        print("\nNotes Menu")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Search Note")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            search_note()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")


menu()