#Your Name
#CIS261
#VIBE Coding

class Student:
    def __init__(self, name, student_id, test1, test2, test3):
        self.name = name
        self.student_id = student_id
        self.test1 = test1
        self.test2 = test2
        self.test3 = test3
        self.average = (test1 + test2 + test3) / 3
        if 90 <= self.average <= 100:
            self.grade = 'A'
        elif 80 <= self.average < 90:
            self.grade = 'B'
        elif 70 <= self.average < 80:
            self.grade = 'C'
        elif 60 <= self.average < 70:
            self.grade = 'D'
        else:
            self.grade = 'F'

    def display_record(self):
        print(f"Student Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print(f"Test 1: {self.test1:.2f}")
        print(f"Test 2: {self.test2:.2f}")
        print(f"Test 3: {self.test3:.2f}")
        print(f"Average Score: {self.average:.2f}")
        print(f"Letter Grade: {self.grade}")
        print("-" * 40)

def load_students():
    try:
        with open("student_grades.txt", "r") as f:
            students = {}
            for line in f:
                parts = line.strip().split("|")
                if len(parts) == 7:
                    name, sid, t1, t2, t3, avg, grade = parts
                    try:
                        student = Student(name, sid, float(t1), float(t2), float(t3))
                        student.average = float(avg)
                        student.grade = grade
                        students[sid] = student
                    except ValueError:
                        print(f"Error parsing line: {line.strip()}. Skipping.")
            return students
    except (FileNotFoundError, IOError, OSError) as e:
        print(f"Error loading file: {e}")
        return {}

def save_students(students):
    try:
        with open("student_grades.txt", "w") as f:
            for student in students.values():
                f.write(f"{student.name}|{student.student_id}|{student.test1}|{student.test2}|{student.test3}|{student.average}|{student.grade}\n")
        print("Records saved successfully.")
    except (IOError, OSError) as e:
        print(f"Error saving file: {e}")

def display_table(students):
    if not students:
        print("No students found.")
        return
    print(f"{'Name':<20} {'ID':<10} {'Test1':<8} {'Test2':<8} {'Test3':<8} {'Average':<8} {'Grade':<5}")
    print("-" * 75)
    for student in students.values():
        print(f"{student.name:<20} {student.student_id:<10} {student.test1:<8.2f} {student.test2:<8.2f} {student.test3:<8.2f} {student.average:<8.2f} {student.grade:<5}")

def class_statistics(students):
    if not students:
        print("No students found.")
        return
    avgs = [s.average for s in students.values()]
    highest = max(avgs)
    lowest = min(avgs)
    class_avg = sum(avgs) / len(avgs)
    print(f"Highest Average: {highest:.2f}")
    print(f"Lowest Average: {lowest:.2f}")
    print(f"Class Average: {class_avg:.2f}")

def search_student(students):
    name = input("Enter student name: ").strip().lower()
    found = [s for s in students.values() if s.name.lower() == name]
    if found:
        for s in found:
            s.display_record()
    else:
        print("Student not found.")

def main():
    students = load_students()
    
    while True:
        print("\nStudent Record Management System")
        print("1. Add Student")
        print("2. View Student Record")
        print("3. Display All Students (Table)")
        print("4. Class Statistics")
        print("5. Search Student by Name")
        print("6. Save Records")
        print("7. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter student name: ")
            student_id = input("Enter student ID: ")
            if student_id not in students:
                try:
                    test1 = float(input("Enter Test 1 score: "))
                    test2 = float(input("Enter Test 2 score: "))
                    test3 = float(input("Enter Test 3 score: "))
                    if all(0 <= score <= 100 for score in [test1, test2, test3]):
                        students[student_id] = Student(name, student_id, test1, test2, test3)
                        print(f"Student {name} added.")
                    else:
                        print("Invalid scores. Must be between 0 and 100.")
                except ValueError:
                    print("Invalid input. Scores must be numbers.")
            else:
                print("Student ID already exists.")
        
        elif choice == '2':
            student_id = input("Enter student ID: ")
            if student_id in students:
                students[student_id].display_record()
            else:
                print("Student not found.")
        
        elif choice == '3':
            display_table(students)
        
        elif choice == '4':
            class_statistics(students)
        
        elif choice == '5':
            search_student(students)
        
        elif choice == '6':
            save_students(students)
            print("Records saved.")
        
        elif choice == '7':
            save_students(students)  # Auto-save on exit
            break
        
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main() 