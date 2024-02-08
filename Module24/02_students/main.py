# TODO здесь писать код
class Student:

    def __init__(self, famyly_name, group_number, grade, department, phone):
        self.famyly_name = famyly_name
        self.group_number = group_number
        self.grade = grade
        self.department = department
        self.phone = phone


student_list = []
for i in range(10):
    famyly_name = input("ФИ: ")
    group_number = input("Номер группы: ")
    grade = float(input("Средний балл: "))
    department = input("Направление обучения: ")
    phone = input("Введите номер телефона: ")

    student = Student(famyly_name, group_number, grade, department, phone)
    student_list.append(student)

sorted_students = sorted(student_list, key=lambda student: student.grade)

for info_stud in sorted_students:
    print(f"\nСтудент: {info_stud.famyly_name}, Группа: {info_stud.group_number}, Средний балл: {info_stud.grade}")
    print(f"Дополнительная информация:\nФакультет: {info_stud.department}\nНомер телефона: {info_stud.phone}\n\n")
