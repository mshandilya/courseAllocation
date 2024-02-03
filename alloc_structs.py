# A class for courses
class Course:
    # A course is identified by its course code. Additionally, we also store the course name.
    # sn                            denotes the number of students assigned to the course supernumerarily
    # cap                           denotes the capacity of the course
    # r_cap                         denotes the remaining capacity of the course
    # temp_assigned_students        a list containing the students allocated this course temporarily
    # perm_assigned_students        a list containing the students allocated this course permanently
    # popularity_index              the score indicating the sum of 'minimum positive score change' that
    #                               could've been gained by a student provided there was one more seat
    #                               for all students
    def __init__(self, code, name, cap=40):
        self.code = code
        self.name = name
        self.sn = 0
        self.cap = cap
        self.r_cap = cap
        self.temp_assigned_students = []
        self.perm_assigned_students = []
        self.popularity_index = 0

    # Given an unassigned student, allocate this course (none of his/her preference) to that student.
    def add_clueless_student(self, stud):
        self.temp_assigned_students.append(stud)
        stud.allocated_courses.append(self)
        self.r_cap -= 1

    # Given a student, allocate this course to that student temporarily.
    def add_student(self, stud):
        self.temp_assigned_students.append(stud)
        stud.allocated_courses.append(self)
        stud.change_score((1 - (stud.course_preferences.index(self.code) / len(stud.course_preferences))) * 100.0)
        self.temp_assigned_students.sort(key=lambda x: (100 / len(x.course_preferences))*1000 + 100 - x.temp_score, reverse=True)
        self.r_cap -= 1

    # Given a student, assign them to this course supernumerarily (no change in remaining capacity).
    def add_super_student(self, stud):
        self.perm_assigned_students.append(stud)
        stud.allocated_courses.append(self)
        stud.change_score((1 - (stud.course_preferences.index(self.code) / len(stud.course_preferences))) * 100.0)
        stud.fixate()
        self.sn += 1

    # Unassign the student at the course's least preference (according to the dynamic ranking
    # introduced for Hospital Resident Matching Algorithm).
    def remove_last(self):
        unlucky_stud = self.temp_assigned_students.pop()
        self.r_cap += 1
        unlucky_stud.allocated_courses.remove(self)
        unlucky_stud.tempScore = 0
        return unlucky_stud.roll

    # Make all temporarily assigned students permanent.
    def fixate(self):
        for stud in self.temp_assigned_students:
            stud.fixate()
        self.perm_assigned_students.extend(self.temp_assigned_students)
        self.temp_assigned_students = []

    def __repr__(self):
        return f'Code:\t\t\t\t\t\t{self.code}\n' \
               f'Name:\t\t\t\t\t\t{self.name}\n' \
               f'Capacity:\t\t\t\t\t{self.cap}\n' \
               f'Allocated Number:\t\t\t{self.cap - self.r_cap}\n' \
               f'Supernumerarily Allocated:\t{self.sn}'

    def __str__(self):
        return f'Code:\t\t\t\t\t\t{self.code}\n' \
               f'Name:\t\t\t\t\t\t{self.name}\n' \
               f'Capacity:\t\t\t\t\t{self.cap}\n' \
               f'Allocated Number:\t\t\t{self.cap - self.r_cap}\n' \
               f'Supernumerarily Allocated:\t{self.sn}'


# A class for students
class Student:
    # A student is identified by his/her roll number. Additionally, we also store their names.
    # desired_n             denotes the desired number of courses for the student
    # actual_n              denotes the number of courses actually allocated to the student
    # course_preferences    a list containing the course codes of the preferences of a student
    # allocated_courses     a list containing the courses allocated to the students
    # score                 the satisfaction score of the student based on the permanently allocated courses to them
    # temp_score            the score denoting the satisfaction of a student with the currently
    #                       allocated temporary course
    def __init__(self, roll, name, dn=0, cpref=None):
        if cpref is None:
            cpref = []
        self.roll = roll
        self.name = name
        self.desired_n = dn
        self.actual_n = 0
        self.course_preferences = cpref
        self.allocated_courses = []
        self.score = 0.0
        self.temp_score = 0.0

    # Given a course, allocate it permanently to the student.
    def allocate(self, course):
        self.allocated_courses.append(course)
        course.r_cap -= 1
        course.perm_assigned_students.append(self)

    # A function to enable changing the temporary score externally.
    def change_score(self, score):
        self.temp_score = score

    # Calling the fixate() function indicates that the last
    # course allocated to the student is now permanently allocated to him/her.
    def fixate(self):
        if self.allocated_courses[-1].code in self.course_preferences:
            self.course_preferences.remove(self.allocated_courses[-1].code)
        self.actual_n += 1
        self.score += (self.temp_score / self.desired_n)
        self.temp_score = 0

    def __repr__(self):
        return f'Name:\t\t\t\t{self.name}\n' \
               f'Roll Number:\t\t{self.roll}\n' \
               f'Allocated Courses:\t{", ".join(list(map(lambda x: x.code, self.allocated_courses)))}\n' \
               f'Satisfaction Score:\t{self.score}'

    def __str__(self):
        return f'Name:\t\t\t\t{self.name}\n' \
               f'Roll Number:\t\t{self.roll}\n' \
               f'Allocated Courses:\t{", ".join(list(map(lambda x: x.code, self.allocated_courses)))}\n' \
               f'Satisfaction Score:\t{self.score}'
