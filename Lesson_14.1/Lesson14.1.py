class GroupLimitError(Exception):
    """Виняток, що викликається при спробі додати більше ніж 10 студентів до групи."""
    def __init__(self, message="Неможливо додати більше ніж 10 студентів до групи"):
        self.message = message
        super().__init__(self.message)

class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.age} років, {self.gender}"

class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.age} років, {self.gender}, Залікова книжка: {self.record_book}"

class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise GroupLimitError()
        self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = "\n".join(str(student) for student in self.group)
        return f"Номер групи: {self.number}\n{all_students}"

# Приклад використання і тестування
try:
    st1 = Student('Чоловік', 30, 'Стів', 'Джобс', 'AN142')
    st2 = Student('Жінка', 25, 'Ліза', 'Тейлор', 'AN145')
    st3 = Student('Чоловік', 22, 'Джон', 'Доу', 'AN146')
    st4 = Student('Жінка', 23, 'Джейн', 'Сміт', 'AN147')
    st5 = Student('Чоловік', 24, 'Джим', 'Бім', 'AN148')
    st6 = Student('Жінка', 21, 'Ана', 'Джонсон', 'AN149')
    st7 = Student('Чоловік', 27, 'Кріс', 'Еванс', 'AN150')
    st8 = Student('Жінка', 26, 'Емма', 'Стоун', 'AN151')
    st9 = Student('Чоловік', 28, 'Роберт', 'Дауні', 'AN152')
    st10 = Student('Жінка', 29, 'Скарлетт', 'Йоганссон', 'AN153')
    st11 = Student('Чоловік', 20, 'Том', 'Голланд', 'AN154')

    gr = Group('PD1')
    gr.add_student(st1)
    gr.add_student(st2)
    gr.add_student(st3)
    gr.add_student(st4)
    gr.add_student(st5)
    gr.add_student(st6)
    gr.add_student(st7)
    gr.add_student(st8)
    gr.add_student(st9)
    gr.add_student(st10)
    # Спроба додати 11-го студента повинна викликати виняток
    gr.add_student(st11)
except GroupLimitError as e:
    print(e)

print(gr)

assert str(gr.find_student('Джобс')) == str(st1), 'Тест1'
assert gr.find_student('Джобс2') is None, 'Тест2'
assert isinstance(gr.find_student('Джобс'), Student) is True, 'Метод пошуку повинен повертати екземпляр'

gr.delete_student('Тейлор')
print(gr)  # Залишається тільки один студент

gr.delete_student('Тейлор')  # Немає помилки!
