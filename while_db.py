from using_db import (
    add_student,
    add_teacher,
    add_course,
    add_exam,
    add_grade,
    update_student,
    delete_student,
    get_students_by_department,
    get_courses_by_teacher,
    get_students_by_course,
    get_grades_by_course,
    get_average_score_by_student_and_course,
    get_average_score_by_student,
    get_average_score_by_department
)

def main():
    while True:
        print("nЧто вы хотите сделать с базой данных?")
        print("1. Добавить запись")
        print("2. Изменить информацию")
        print("3. Удалить запись")
        print("4. Получить список студентов по факультету")
        print("5. Получить список курсов, читаемых определенным преподавателем")
        print("6. Получить список студентов, зачисленных на конкретный курс")
        print("7. Получить оценки студентов по определенному курсу")
        print("8. Средний балл студента по определенному курсу")
        print("9. Средний балл студента в целом")
        print("10. Средний балл по факультету")
        print("11. Выйти")

        choice = input("Введите номер действия: ")

        if choice == '1':
            print("nЧто вы хотите добавить?")
            print("1. Студента")
            print("2. Преподавателя")
            print("3. Курс")
            print("4. Экзамен")
            print("5. Оценку")

            add_choice = input("Введите номер добавляемой записи: ")

            if add_choice == '1':
                name = input("Введите имя студента: ")
                surname = input("Введите фамилию студента: ")
                department = input("Введите факультет: ")
                date_of_birth = input("Введите дату рождения (YYYY-MM-DD): ")
                add_student(name, surname, department, date_of_birth)

            elif add_choice == '2':
                name = input("Введите имя преподавателя: ")
                surname = input("Введите фамилию преподавателя: ")
                department = input("Введите факультет: ")
                add_teacher(name, surname, department)

            elif add_choice == '3':
                course_name = input("Введите название курса: ")
                department = input("Введите факультет: ")
                teacher_id = int(input("Введите ID преподавателя, который ведет курс: "))  # Новый ввод
                add_course(course_name, department, teacher_id)  # Передаем все три аргумента


            elif add_choice == '4':  # Примерный номер выбора
                exam_name = input("Введите название экзамена: ")
                course_id = int(input("Введите ID курса: "))
                max_score = int(input("Введите максимальный балл за экзамен: "))  # Новый ввод
                add_exam(exam_name, course_id, max_score)  # Передаем все три аргумента


            elif add_choice == '5':
                student_id = int(input("Введите ID студента: "))
                course_id = int(input("Введите ID курса: "))
                grade = float(input("Введите оценку: "))
                add_grade(student_id, course_id, grade)

        elif choice == '2':
            student_id = int(input("Введите ID студента для изменения: "))
            name = input("Введите новое имя (оставьте пустым для пропуска): ") or None
            surname = input("Введите новую фамилию (оставьте пустым для пропуска): ") or None
            department = input("Введите новый факультет (оставьте пустым для пропуска): ") or None
            date_of_birth = input("Введите новую дату рождения (YYYY-MM-DD) (оставьте пустым для пропуска): ") or None
            update_student(student_id, name, surname, department, date_of_birth)

        elif choice == '3':
            student_id = int(input("Введите ID студента для удаления: "))
            delete_student(student_id)

        elif choice == '4':
            department = input("Введите название факультета: ")
            students = get_students_by_department(department)
            for student in students:
                print(student)

        elif choice == '5':
            teacher_id = int(input("Введите ID преподавателя: "))
            courses = get_courses_by_teacher(teacher_id)
            for course in courses:
                print(course)

        elif choice == '6':
            course_id = int(input("Введите ID курса: "))
            students = get_students_by_course(course_id)
            for student in students:
                print(student)

        elif choice == '7':
            course_id = int(input("Введите ID курса: "))
            grades = get_grades_by_course(course_id)
            for grade in grades:
                print(grade)

        elif choice == '8':
            student_id = int(input("Введите ID студента: "))
            course_id = int(input("Введите ID курса: "))
            average_score = get_average_score_by_student_and_course(student_id, course_id)
            print(f"Средний балл студента {student_id} по курсу {course_id}: {average_score}")

        elif choice == '9':
            student_id = int(input("Введите ID студента: "))
            average_score = get_average_score_by_student(student_id)
            print(f"Средний балл студента {student_id}: {average_score}")

        elif choice == '10':
            department = input("Введите название факультета: ")
            average_score = get_average_score_by_department(department)
            print(f"Средний балл по факультету {department}: {average_score}")

        elif choice == '11':
            print("Выход из программы.")
            break

        else:
            print("Ошибка: неверный ввод. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()