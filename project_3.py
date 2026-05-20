students = {}

print("---- WELCOME MY STUDENT MANAGEMENT SYSTEM ----")

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Check Percentage")
    print("4. Find Topper")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        marks = []

        
 
    elif choice == "2":
        if students:
            for name, marks in students.items():
                print(f"{name} : {marks}")
        else:
            print("No students found!")
    elif choice == "2":
        if students:
            for name, marks in students.items():
                print(f"{name} : {marks}")
        else:
            print("No students found!")
  
    elif choice == "3":
        name = input("Enter student name to check percentage: ")

        if name in students:
            total = sum(students[name])
            percentage = (total / 500) * 100
            print(f"{name}'s Percentage is: {percentage}%")
        else:
            print("Student not found!")

    
    elif choice == "4":
        if students:
            topper = ""
            highest = 0

            for name, marks in students.items():
                total = sum(marks)
                percentage = (total / 500) * 100

                if percentage > highest:
                    highest = percentage
                    topper = name

            print(f"Topper is {topper} with {highest}%")
        else:
            print("No students data available!")

    
    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")
