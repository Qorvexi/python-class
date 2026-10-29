# =======================================PART 1============================================================
ADMIN_EMAIL = "admin@school.com"
ADMIN_PASS = "Python123"

# ======================================PART 2=============================================================
students_db = {
    "ST001": {"id": "ABC001", "name": "Tony Stark", "age": 18, "dept": "Computer Science", "level": 100},
    "ST002": {"id": "ABC002", "name": "Kara Johnson", "age": 19, "dept": "Accounting", "level": 200},
    "ST003": {"id": "ABC003", "name": "Bruce Wayne", "age": 21, "dept": "Engineering", "level": 300},
    "ST004": {"id": "ABC004", "name": "Peter Parker", "age": 18, "dept": "Computer Science", "level": 100},
    "ST005": {"id": "ABC005", "name": "Tiana James", "age": 20, "dept": "Accounting", "level": 200}
}

# =====================================PART 3=============================================================
def list_students():
    print("\n--- ALL STUDENTS ---")
    for sid, info in students_db.items():
        print(f"ID: {info['id']} | Name: {info['name']} | Dept: {info['dept']} | Level: {info['level']}")


# ===================================PART 4===============================================================
def find_student():
    sid = input("\nEnter Student ID (e.g., ABC001): ").strip().upper()
    student = students_db.get(sid)
    if student:
        print(f"Found: {student['name']} | Dept: {student['dept']} | Level: {student['level']}")
    else:
        print("Student not found.")


# =================================PART 5==================================================================
all_courses = ["Python", "Database Systems", "Web Development", "Mathematics", "Computer Networks", "English", "React", "JavaScript"]
def list_catalog():
    print("\n--- AVAILABLE COURSES ---")
    for i, course in enumerate(all_courses, start=1):
        print(f"{i}. {course}")


# ==================================PART 6=================================================================
david_registered = ["Python", "Mathematics", "Database Systems"]
def list_david_courses():
    print("\n--- TONY'S COURSES ---")
    for course in david_registered:
        print(f"- {course}")


# ===================================PART 7===============================================================
raw_courses = ["Python", "Mathematics", "Python", "Database Systems", "Mathematics"]
def list_unique_courses():
    print("\n--- UNIQUE COURSES ---")
    for course in set(raw_courses):
        print(f"- {course}")


# =================================PART 8================================================================
david_tuple = ("Tony Stark", 18, "Computer Science")
def show_tuple_info():
    print("\n--- TUPLE INFO ---")
    print(f"Name: {david_tuple[0]}\nAge: {david_tuple[1]}\nDept: {david_tuple[2]}")

def get_grade(score):
    if score >= 70: return "Pass", "Grade A"
    if score >= 60: return "Pass", "Grade B"
    if score >= 50: return "Pass", "Grade C"
    if score >= 40: return "Fail", "Grade D"
    return "Fail", "Grade F"


# =================================PART 9 & 10==========================================================
david_scores = {"Python": 85, "Mathematics": 72, "English": 42, "Database Systems": 90}
def show_results():
    print("\n--- STUDENT RESULTS ---")
    for subject, score in david_scores.items():
        status, grade = get_grade(score)
        print(f"{subject}: {score} -> {status} ({grade})")


# ===================================PART 11=============================================================
def list_departments():
    print("\n--- DEPARTMENTS ---")
    depts = {info['dept'] for info in students_db.values()}
    for dept in depts:
        print(f"- {dept}")


# =====================================PART 12============================================================
def full_report():
    print("\n========================================")
    print("         FULL STUDENT REPORT            ")
    print("========================================")
    student = students_db["ST001"]
    print(f"ID: {student['id']}\nName: {student['name']}\nDept: {student['dept']}\nLevel: {student['level']}")

    print("\nRegistered Courses:")
    for c in david_registered:
        print(f" - {c}")

    print("\nAcademic Performance:")
    for subject, score in david_scores.items():
        _, grade = get_grade(score)
        print(f" - {subject}: {score} ({grade})")
    print("========================================")


# =============================================PART 14=====================================================
def add_student():
    sid = input("\nEnter New Student ID (e.g., ST006): ").strip().upper()
    if sid in students_db:
        print("Error: Student ID already exists.")
        return

    name = input("Enter Name: ").strip()
    age = int(input("Enter Age: "))
    dept = input("Enter Department: ").strip()
    level = int(input("Enter Level: "))

    students_db[sid] = {"id": sid, "name": name, "age": age, "dept": dept, "level": level}
    print(f"Student {name} added successfully.")


# ==========================================PART 15====================================================
def calculate_gpa():
    scores = david_scores.values()
    avg = sum(scores) / len(scores)
    print(f"\nAverage Score: {avg:.2f}")


def main():
    print("========================================")
    print("       SCHOOL SYSTEM ADMIN LOGIN        ")
    print("========================================")
    email = input("Email: ").strip()
    password = input("Password: ").strip()

    # Part 1: Authentication Check
    if email != ADMIN_EMAIL or password != ADMIN_PASS:
        print("\nAccess Denied: Invalid credentials.")
        return

    print("\nAccess Granted!")

    # System Loop for Menu Navigation (Part 13)
    while True:
        print("\n========================================")
        print("        STUDENT MANAGEMENT SYSTEM       ")
        print("========================================")
        print("1.  Display All Students")
        print("2.  Search Students")
        print("3.  Display Course Catalog")
        print("4.  Display Registered Courses")
        print("5.  Display Unique Courses")
        print("6.  Display Tuple Information")
        print("7.  Calculate Results & Grades")
        print("8.  Display Departments")
        print("9.  Generate Full Report")
        print("10. Add New Student")
        print("11. Calculate Average Score")
        print("12. System Summary")
        print("0.  Exit System")
        print("========================================")

        choice = input("Select an option (0-12): ").strip()

        if choice == "1":
            list_students()
        elif choice == "2":
            find_student()
        elif choice == "3":
            list_catalog()
        elif choice == "4":
            list_david_courses()
        elif choice == "5":
            list_unique_courses()
        elif choice == "6":
            show_tuple_info()
        elif choice == "7":
            show_results()
        elif choice == "8":
            list_departments()
        elif choice == "9":
            full_report()
        elif choice == "10":
            add_student()
        elif choice == "11":
            calculate_gpa()
        elif choice == "12":
            system_summary()
        elif choice == "0":
            print("\nLogging out... Goodbye!")
            break
        else:
            print("\nInvalid choice. Please select between 0 and 12.")


# =============================================BONUS================================================================
def system_summary():
    print("\n--- SYSTEM SUMMARY STATISTICS ---")
    print(f"Total Students: {len(students_db)}")
    print(f"Total Catalog Courses: {len(all_courses)}")
    print(f"Total Unique Departments: {len({s['dept'] for s in students_db.values()})}")


if __name__ == "__main__":
    main()