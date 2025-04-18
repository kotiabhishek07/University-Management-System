class person:
    def __init__(self, rollno, name):
        self.rollno = rollno
        self.name = name

class student(person):
    def __init__(self, rollno, name, branch):
        super().__init__(rollno, name)
        self.branch = branch

class teacher(person):
    def __init__(self, rollno, name, subject):
        super().__init__(rollno, name)
        self.subject = subject

class college:
    def __init__(self, cname):
        self.cname = cname
        self.students = []
        self.teachers = []

    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def display_students(self):
        for i, student in enumerate(self.students):
            print(f"Student {i+1}:")
            print(f"Roll Number: {student.rollno}")
            print(f"Name: {student.name}")
            print(f"Branch: {student.branch}")
            print()

    def display_teachers(self):
        for i, teacher in enumerate(self.teachers):
            print(f"Teacher {i+1}:")
            print(f"Roll Number: {teacher.rollno}")
            print(f"Name: {teacher.name}")
            print(f"Subject: {teacher.subject}")
            print()

    def search_student(self, rollno):
        for student in self.students:
            if student.rollno == rollno:
                return student
        return None

    def search_teacher(self, rollno):
        for teacher in self.teachers:
            if teacher.rollno == rollno:
                return teacher
        return None

colleges = []

def find_college_by_name(name):
    for c in colleges:
        if c.cname.lower() == name.lower():
            return c
    return None

while True:
    print("Choose the Required option: ")
    print("1. Create College.")
    print("2. Add Student.")
    print("3. Add Teacher.")
    print("4. Display Students.")
    print("5. Display Teachers.")
    print("6. Search Student.")
    print("7. Search Teacher.")
    print("8. Search College.")
    print("9. Exit.")

    x = int(input("Enter your Option: "))

    if x == 1:
        clgname = input("Enter College Name: ")
        if find_college_by_name(clgname):
            print("\nCollege Already Exists!\n")
        else:
            colleges.append(college(clgname))
            print("\nCollege Added Successfully\n")

    elif x == 2:
        clgname = input("Enter College Name: ")
        clg = find_college_by_name(clgname)
        if clg:
            rollno = input("Enter Roll No: ")
            name = input("Enter Student Name: ")
            branch = input("Enter Student Branch: ")
            clg.add_student(student(rollno, name, branch))
            print("\nStudent Added Successfully\n")
        else:
            print("\nCollege Does Not Exist!\n")

    elif x == 3:
        clgname = input("Enter College Name: ")
        clg = find_college_by_name(clgname)
        if clg:
            rollno = input("Enter Roll No: ")
            name = input("Enter Teacher Name: ")
            subject = input("Enter Subject: ")
            clg.add_teacher(teacher(rollno, name, subject))
            print("\nTeacher Added Successfully!\n")
        else:
            print("\nCollege Does Not Exist!\n")

    elif x == 4:
        clgname = input("Enter College Name: ")
        clg = find_college_by_name(clgname)
        if clg:
            clg.display_students()
        else:
            print("\nCollege Does Not Exist!\n")

    elif x == 5:
        clgname = input("Enter College Name: ")
        clg = find_college_by_name(clgname)
        if clg:
            clg.display_teachers()
        else:
            print("\nCollege Does Not Exist!\n")

    elif x == 6:
        clgname = input("Enter College Name: ")
        rollno = input("Enter Student Roll Number: ")
        clg = find_college_by_name(clgname)
        if clg:
            student = clg.search_student(rollno)
            if student:
                print("\nStudent Found:")
                print(f"Roll Number: {student.rollno}")
                print(f"Name: {student.name}")
                print(f"Branch: {student.branch}\n")
            else:
                print("\nStudent Not Found!\n")
        else:
            print("\nCollege Does Not Exist!\n")

    elif x == 7:
        clgname = input("Enter College Name: ")
        rollno = input("Enter Teacher Roll Number: ")
        clg = find_college_by_name(clgname)
        if clg:
            teacher = clg.search_teacher(rollno)
            if teacher:
                print("\nTeacher Found:")
                print(f"Roll Number: {teacher.rollno}")
                print(f"Name: {teacher.name}")
                print(f"Subject: {teacher.subject}\n")
            else:
                print("\nTeacher Not Found!\n")
        else:
            print("\nCollege Does Not Exist!\n")

    elif x == 8:
        clgname = input("Enter College Name to Search: ")
        clg = find_college_by_name(clgname)
        if clg:
            print(f"\nCollege '{clg.cname}' exists.\n")
            print(f"Number of Students: {len(clg.students)}")
            print(f"Number of Teachers: {len(clg.teachers)}\n")
        else:
            print("\nCollege Not Found!\n")

    elif x == 9:
        break

    else:
        print("\nChoose the Correct Option!\n")
