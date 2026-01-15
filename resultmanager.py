import json

FILE_NAME = "students.json"

# Load data from file
def load_data():
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except:
        return []

# Save data to file
def save_data(data):
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)

# Grade calculator
def get_grade(avg):
    if avg >= 70: return "A", "Excellent"
    elif avg >= 60: return "B", "Very Good"
    elif avg >= 50: return "C", "Good"
    elif avg >= 45: return "D", "Fair"
    elif avg >= 40: return "E", "Poor"
    else: return "F", "Fail"

# Add student
def add_student(data):
    name = input("Name: ")
    matric = input("Matric No: ")
    course = input("Course: ")
    scores = []
    for i in range(3):
        scores.append(float(input(f"Score {i+1}: ")))

    total = sum(scores)
    avg = total / len(scores)
    grade, remark = get_grade(avg)

    student = {
        "name": name,
        "matric": matric,
        "course": course,
        "scores": scores,
        "total": total,
        "average": avg,
        "grade": grade,
        "remark": remark
    }

    data.append(student)
    save_data(data)
    print("Student added successfully!")

# View all
def view_all(data):
    if not data:
        print("No records found.")
        return
    for s in data:
        print("-"*30)
        print("Name:", s["name"])
        print("Matric:", s["matric"])
        print("Course:", s["course"])
        print("Scores:", s["scores"])
        print("Total:", s["total"])
        print("Average:", round(s["average"],2))
        print("Grade:", s["grade"])
        print("Remark:", s["remark"])

# Search
def search(data):
    key = input("Enter name or matric: ").lower()
    for s in data:
        if key in s["name"].lower() or key == s["matric"].lower():
            print(s)
            return
    print("Student not found.")

# Edit score
def edit(data):
    matric = input("Enter matric to edit: ")
    for s in data:
        if s["matric"] == matric:
            s["scores"] = [float(input("New score 1: ")),
                           float(input("New score 2: ")),
                           float(input("New score 3: "))]
            s["total"] = sum(s["scores"])
            s["average"] = s["total"]/3
            s["grade"], s["remark"] = get_grade(s["average"])
            save_data(data)
            print("Updated successfully!")
            return
    print("Student not found.")

# Delete
def delete(data):
    matric = input("Enter matric to delete: ")
    for s in data:
        if s["matric"] == matric:
            data.remove(s)
            save_data(data)
            print("Deleted successfully!")
            return
    print("Student not found.")

# Main menu
def main():
    data = load_data()
    while True:
        print("\n--- STUDENT RESULT MANAGER ---")
        print("1. Add Student")
        print("2. View All")
        print("3. Search Student")
        print("4. Edit Student Scores")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Choose: ")

        if choice == "1": add_student(data)
        elif choice == "2": view_all(data)
        elif choice == "3": search(data)
        elif choice == "4": edit(data)
        elif choice == "5": delete(data)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

main()
