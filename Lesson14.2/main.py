from student import Student
from group import Group

# Створюємо студентів
st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')

# Створюємо групу та додаємо студентів
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)

# Виводимо інформацію про групу
print(gr)

# Перевірка пошуку студента
assert gr.find_student('Jobs') == st1  # 'Steve Jobs'
assert gr.find_student('Jobs2') is None

# Видаляємо студента
gr.delete_student('Taylor')
print(gr)  # Only one student
