import csv
import math
import time

GRADE_FILE = "student_grades.txt"
MIN_SCORE = 0
MAX_SCORE = 100


def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    return "F"


def read_records():
    try:
        with open(GRADE_FILE, "r", newline="", encoding="utf-8") as file:
            return list(csv.reader(file))
    except FileNotFoundError:
        return []


def add_student():
    name = input("Enter student's name: ").strip()
    student_id = input("Enter student's ID: ").strip()

    try:
        score = float(input("Enter assignment score (0-100): "))
    except ValueError:
        print("Enter a valid number.")
        return

    if not name or not student_id:
        print("Name and ID cannot be empty.")
        return
    if not math.isfinite(score) or score < MIN_SCORE or score > MAX_SCORE:
        print("Score must be between 0 and 100.")
        return

    with open(GRADE_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([name, student_id, score, get_letter_grade(score)])

    print("Student record saved.")


def view_records():
    records = read_records()
    if not records:
        print("No student records found.")
        return

    total = 0
    highest = MIN_SCORE
    lowest = MAX_SCORE

    for record in records:
        name, student_id, score_text, grade = record
        score = float(score_text)
        total += score
        if score > highest:
            highest = score
        if score < lowest:
            lowest = score
        print(f"Name: {name}, ID: {student_id}, Score: {score:g}, Grade: {grade}")

    print(f"Class average: {total / len(records):.2f}")
    print(f"Highest score: {highest:g}")
    print(f"Lowest score: {lowest:g}")


def main():
    while True:
        time.sleep(1)
        print("\n1. Add student grade\n2. View records\n3. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_records()
        elif choice == "3":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
