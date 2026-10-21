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

    # Read student records from the file.
    with open("student_grades.txt", "r") as file:
        records = file.readlines()

    # Display all student records.
    print("\nAll Student Records:")
    for record in records:
        name, id, score = record.strip().split(",")
        print(f"Name: {name}, ID: {id}, Score: {score}")

    # Calculate and display the average score of all students.
    total_score = sum(float(record.strip().split(",")[2]) for record in records)
    average_score = total_score / len(records)
    print(f"\nAverage Score of All Students: {average_score:.2f}")
    
