#Creating Person Class
class Person:
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number

    def __str__(self):
        return f"Name: {self.name}, ID: {self.id_number}"

#Creating Student Class
class Student(Person):
    def __init__(self, name, id_number, major):
        super().__init__(name, id_number)
        self.major = major

    def __str__(self):
        return f"{super().__str__()}, Major: {self.major}"

#Creating Instructor Class
class Instructor(Person):
    def __init__(self, name, id_number, department):
        super().__init__(name, id_number)
        self.department = department

    def __str__(self):
        return f"{super().__str__()}, Department: {self.department}"

#Creating Course Class
class Course:
    def __init__(self, course_name, course_id):
        self.course_name = course_name
        self.course_id = course_id
        self.enrolled_students = []

    def add_student(self, student):
        if student not in self.enrolled_students:
            self.enrolled_students.append(student)

    def remove_student(self, student):
        if student in self.enrolled_students:
            self.enrolled_students.remove(student)

    def __str__(self):
        return f"Course: {self.course_name} (ID: {self.course_id}), Enrolled Students: {len(self.enrolled_students)}"

#Creating Enrollment Class
class Enrollment:
    def __init__(self, student, course):
        self.student = student
        self.course = course
        self.grade = None

    def assign_grade(self, grade):
        self.grade = grade

    def __str__(self):
        return f"Student: {self.student.name}, Course: {self.course.course_name}, Grade: {self.grade or 'Not assigned'}"

#Creating StudentManagementSystem Class
class StudentManagementSystem:
    def __init__(self):
        self.students = {}
        self.instructors = {}
        self.courses = {}
        self.enrollments = []

    def add_student(self, student):
        self.students[student.id_number] = student

    def remove_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]

    def update_student(self, student_id, **kwargs):
        if student_id in self.students:
            student = self.students[student_id]
            for key, value in kwargs.items():
                setattr(student, key, value)

    def add_instructor(self, instructor):
        self.instructors[instructor.id_number] = instructor

    def remove_instructor(self, instructor_id):
        if instructor_id in self.instructors:
            del self.instructors[instructor_id]

    def update_instructor(self, instructor_id, **kwargs):
        if instructor_id in self.instructors:
            instructor = self.instructors[instructor_id]
            for key, value in kwargs.items():
                setattr(instructor, key, value)

    def add_course(self, course):
        self.courses[course.course_id] = course

    def remove_course(self, course_id):
        if course_id in self.courses:
            del self.courses[course_id]

    def update_course(self, course_id, **kwargs):
        if course_id in self.courses:
            course = self.courses[course_id]
            for key, value in kwargs.items():
                setattr(course, key, value)

    def enroll_student(self, student_id, course_id):
        if student_id in self.students and course_id in self.courses:
            student = self.students[student_id]
            course = self.courses[course_id]
            course.add_student(student)
            enrollment = Enrollment(student, course)
            self.enrollments.append(enrollment)

    def assign_grade(self, student_id, course_id, grade):
        for enrollment in self.enrollments:
            if enrollment.student.id_number == student_id and enrollment.course.course_id == course_id:
                enrollment.assign_grade(grade)
                break

    def get_students_in_course(self, course_id):
        if course_id in self.courses:
            return self.courses[course_id].enrolled_students
        return []

    def get_courses_for_student(self, student_id):
        return [enrollment.course for enrollment in self.enrollments if enrollment.student.id_number == student_id]

#Testing
if __name__ == "__main__":
    sms = StudentManagementSystem()

    # Adding students
    s1 = Student("Gbenga", "SE001", "Data Science")
    s2 = Student("Femi", "SE002", "Systems Engineering")
    sms.add_student(s1)
    sms.add_student(s2)

    # Adding instructors
    i1 = Instructor("Ike Mowete", "A001", "Data Science")
    sms.add_instructor(i1)

    # Adding courses
    c1 = Course("Introduction to Programming", "CSC101")
    c2 = Course("Logics and Sequence", "MTH101")
    sms.add_course(c1)
    sms.add_course(c2)

    # Enrolling students
    sms.enroll_student("SE001", "CSC101")
    sms.enroll_student("SE001", "MTH101")
    sms.enroll_student("S002", "MATH101")

    # Assigning grades
    sms.assign_grade("SE001", "CSC101", "A1")
    sms.assign_grade("SE001", "MTH101", "B2")
    sms.assign_grade("SE002", "MTH101", "C3")

    # Demonstrating functionality
    print("Students in CSC101:", [str(s) for s in sms.get_students_in_course("CSC101")])
    print("Courses for SE001:", [str(c) for c in sms.get_courses_for_student("SE001")])

    print("\nAll Enrollments:")
    for enrollment in sms.enrollments:
        print(enrollment)

    # Updating a student
    sms.update_student("SE001", major="Computer Engineering")
    print("\nUpdated Student SE001:", sms.students["SE001"])

    # Removing a student
    sms.remove_student("SE002")
    print("\nStudents after removing SE002:", [str(s) for s in sms.students.values()])