def initialize_dict(student_name, subject_grades):
    return {student_name: subject_grades}

def add_student(student_grades=None):
    if student_grades is None:
        student_grades = {}
    name = input ("Enter student name:\n").title()
    subjects = {}
    while True:
        entry = input(
            "Enter subject and grade (or 'exit' to finish):\n"
        )
        if entry.lower()== "exit":
            break 
        subject, grade = entry.split(",")
        subject = subject.strip().title()
        grade = float(grade.strip())
        subjects[subject] = grade
    student_grades[name] = subjects
    print(
        f"Student {name} successfully added to the grades management system."
    )
    return student_grades

def get_students(student_grades, keys):
    result = {}
    for name in keys:
        found = False
        for student, grades in student_grades.items():
            if student.lower()== name.lower():
                result[student.title()] = grades 
                found = True
                break 
        if not found:
            print(f"{name.title()}not found!")
    return result

def avg_by_student(student_grades, keys= None):
    if keys is not None:
        students = get_students (student_grades, keys)
    else:
        students = student_grades
    for student, subjects in students.items():
        if len(subjects) == 0:
            average = 0 
        else:
            average = sum(subjects.values()) / len(subjects)
        print(f"{student}: {average:1f}")