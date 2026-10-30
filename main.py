"""
Student Grade Calculator
A beginner-friendly Python project that calculates total, average, and grade.
"""

def calculate_grade(average):
    """Return a letter grade based on the average mark."""
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


def main():
    print("=" * 40)
    print("       STUDENT GRADE CALCULATOR")
    print("=" * 40)

    name = input("Enter student name: ").strip()
    while not name:
        print("Name cannot be empty.")
        name = input("Enter student name: ").strip()

    try:
        count = int(input("How many subjects? "))
        if count <= 0:
            raise ValueError
    except ValueError:
        print("Please enter a valid positive number of subjects.")
        return

    marks = []
    for subject_no in range(1, count + 1):
        while True:
            try:
                mark = float(input(f"Enter mark for subject {subject_no} (0-100): "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                print("Mark must be between 0 and 100.")
            except ValueError:
                print("Please enter a valid number.")

    total = sum(marks)
    average = total / count
    grade = calculate_grade(average)
    result = "Pass" if all(mark >= 35 for mark in marks) else "Fail"

    print("\n" + "=" * 40)
    print("              RESULT")
    print("=" * 40)
    print(f"Student Name : {name}")
    print(f"Total Marks  : {total:.2f} / {count * 100}")
    print(f"Average      : {average:.2f}%")
    print(f"Grade        : {grade}")
    print(f"Result       : {result}")
    print("=" * 40)


if __name__ == "__main__":
    main()
