# Constants
minimumscore = 0
maximumscore = 100
run = True



while run == True:
    # Ask the user for their Name, Id, and assignment score()
    studentName = input("Enter student's name: ")
    studentId = input("Enter student's ID: ")
    assignmentScore = float(input("Enter assignment score: "))

    # Assign letter grades based on the assignment score using if-elif-else statements
    if assignmentScore >= 90:
        letterGrade = "A"
    elif assignmentScore >= 80:
        letterGrade = "B"
    elif assignmentScore >= 70:
        letterGrade = "C"
    elif assignmentScore >= 60:
        letterGrade = "D"
    else:
        letterGrade = "F"

    # Save the student's information to a file
    with open("student_grades.txt", "a") as file:
        file.write(f"{studentName},{studentId},{assignmentScore},{letterGrade}\n")

    # Read student records from the file.
    with open("student_grades.txt", "r") as file:
        records = file.readlines()

    # Display all student records.
    print("\nAll Student Records:")
    for record in records:
        name, id, score, grade = record.strip().split(",")
        print(f"Name: {name}, ID: {id}, Score: {score}, Grade: {grade}")

    # Calculate and display the average score of all students.
    total_score = sum(float(record.strip().split(",")[2]) for record in records)
    average_score = total_score / len(records)
    print(f"\nAverage Score of All Students: {average_score:.2f}")

    # validate grades are within an acceptable range (0-100)
    if assignmentScore < minimumscore or assignmentScore > maximumscore:
        print("Error: Assignment score must be between 0 and 100.")
        continue

    # Use string operations to format and display the student's information in a readable format from highest to lowest scores.
    print(f"\nStudent Information:\nName: {studentName}\nID: {studentId}\nScore: {assignmentScore}\nGrade: {letterGrade}")


