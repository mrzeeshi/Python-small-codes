#This is a school result maker mini project made using the pandas concepts
#Using this program the users can generate the result report of the students and can edit the file also there exists the sorting to arrange based on the percentage obtained
#Keep in mind that this is the basic program and the errors are expected so wisely give the input because there is the least error handling and wrong input can lead to the worng output
#Thanks
import pandas as pd

print("=" * 50)
print("||", " " * 44, "||")
print("=" * 50)

while True:
    print("Welcome to ZeeSchool")
    print("Select the respective number")
    print("1.Create New Result File")
    print("2.Open Existing File...")
    print("3.Exit")

    choice = int(input("Enter Your Choice.....: "))

    if choice == 1:
        data = pd.DataFrame({})

        cols = int(input("Enter number of columns: "))
        rows = int(input("Enter number of students: "))

        for i in range(cols):
            col_name = input(f"Enter column {i+1} name: ")
            data[col_name] = []

        print("\nEmpty structure created:")
        print(data)

        for i in range(rows):
            for col in data.columns:
                value = input(f"Enter value for {col} in row {i+1}.....: ")
                data.loc[i, col] = value

        total_marks = int(input("Enter the total marks of the exam: "))
        data["Total"] = total_marks
        filename = input("Enter file name (or full path): ") + ".csv"

        data.to_csv(filename, index=False)
        print("File saved successfully.........")

    elif choice == 2:
        try:
            existing_file_path = input(
                "Enter file path (with .csv extension): "
            )

            existing_file_df = pd.read_csv(existing_file_path)
            print("File imported successfully")

            while True:
                print("\nOperations Menu")
                print("1.Display Full File")
                print("2.Edit Some Value")
                print("3.Do Calculations Like Total Marks Percentage etc")
                print("4.Clean Dataset")
                print("5.Exit")

                user_choice = int(input("Enter your choice: "))

                if user_choice == 1:
                    print(existing_file_df.to_string())
                    continue

                elif user_choice == 2:
                    row_no = int(input("Enter row number: "))

                    col_input = input(
                        "Enter column numbers separated by commas: "
                    )
                    col_no = [int(x) for x in col_input.split(",")]

                    col_names = list(existing_file_df.columns)

                    for each_col in col_no:
                        edited_col = col_names[each_col]
                        val = input(f"Enter value for {edited_col}: ")
                        existing_file_df.loc[row_no, edited_col] = val

                    existing_file_df.to_csv(existing_file_path, index=False)
                    print("Changes Made Successfully.....")
                    continue

                elif user_choice == 3:
                    existing_file_df["Obtained Marks"] = existing_file_df.select_dtypes(include="number").sum(axis=1)-existing_file_df["Total"]

                    if "Total" in existing_file_df.columns:
                        existing_file_df["Percentage"] = (
                            existing_file_df["Obtained Marks"] /
                            existing_file_df["Total"]
                        ) * 100
                    else:
                        print("Total column not found!")

                    if "Percentage" in existing_file_df.columns:
                        existing_file_df = existing_file_df.sort_values(
                            by="Percentage",
                            ascending=False
                        )

                    print("Calculations Done Successfully")
                    print(existing_file_df.to_string())

                    existing_file_df.to_csv(existing_file_path, index=False)
                    continue

                elif user_choice == 4:
                    print("Dataset Info:")
                    existing_file_df.info()

                    cleaning_choice = int(input(
                        "1.Drop empty rows\n"
                        "2.Fill empty values\n"
                        "3.Skip\n"
                        "Enter choice: "
                    ))

                    if cleaning_choice == 1:
                        existing_file_df.dropna(inplace=True)

                    elif cleaning_choice == 2:
                        value_for_empty = input("Enter fill value: ")
                        existing_file_df.fillna(value_for_empty, inplace=True)

                    elif cleaning_choice == 3:
                        continue

                    else:
                        print("Invalid choice")

                    existing_file_df.to_csv(existing_file_path, index=False)
                    print("Changes Saved Successfully")
                    continue

                elif user_choice == 5:
                    print("Exiting.....")
                    break

        except Exception as e:
            print("Error occurred:", e)

    elif choice == 3:
        print("Exiting.....")
        break

    else:
        print("Invalid Choice...")
        continue