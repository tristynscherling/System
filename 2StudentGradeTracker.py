# Constants

run = True



while run == True:
    # Ask the user for their Name, Id, and assignment score()
    studentName = input("Enter student's name: ")
    studentId = input("Enter student's ID: ")
    assignmentScore = float(input("Enter assignment score: "))
    # Save the student's information to a file
    with open("student_grades.txt", "a") as file:
        file.write(f"{studentName},{studentId},{assignmentScore}\n")
        