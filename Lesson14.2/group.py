class Group:
    def __init__(self, group_name):
        self.group_name = group_name
        self.students = set()

    def add_student(self, student):
        if len(self.students) >= 20:
            raise ValueError("The group is full")
        self.students.add(student)

    def delete_student(self, last_name):
        student_to_delete = None
        for student in self.students:
            if student.last_name == last_name:
                student_to_delete = student
                break
        if student_to_delete:
            self.students.remove(student_to_delete)

    def find_student(self, last_name):
        for student in self.students:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        students_str = ', '.join(str(student) for student in self.students)
        return f'Group {self.group_name}: {students_str}'
