import sqlite3

def connect_db():
    return sqlite3.connect('university.db')

# 1. Добавление нового студента, преподавателя, курса, экзамена и оценки
def add_student(name, surname, department, date_of_birth):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Students (Name, Surname, Department, DateOfBirth) VALUES (?, ?, ?, ?)', 
                   (name, surname, department, date_of_birth))
    conn.commit()
    conn.close()

def add_teacher(name, surname, department):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Teachers (Name, Surname, Department) VALUES (?, ?, ?)', 
                   (name, surname, department))
    conn.commit()
    conn.close()

def add_course(title, description, teacher_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Courses (Title, Description, TeacherID) VALUES (?, ?, ?)', 
                   (title, description, teacher_id))
    conn.commit()
    conn.close()

def add_exam(date, course_id, max_score):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Exams (Date, CourseID, MaxScore) VALUES (?, ?, ?)', 
                   (date, course_id, max_score))
    conn.commit()
    conn.close()

def add_grade(student_id, exam_id, score):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Grades (StudentID, ExamID, Score) VALUES (?, ?, ?)', 
                   (student_id, exam_id, score))
    conn.commit()
    conn.close()

# 2. Изменение информации о студентах, преподавателях и курсах
def update_student(student_id, name=None, surname=None, department=None, date_of_birth=None):
    conn = connect_db()
    cursor = conn.cursor()
    if name:
        cursor.execute('UPDATE Students SET Name = ? WHERE ID = ?', (name, student_id))
    if surname:
        cursor.execute('UPDATE Students SET Surname = ? WHERE ID = ?', (surname, student_id))
    if department:
        cursor.execute('UPDATE Students SET Department = ? WHERE ID = ?', (department, student_id))
    if date_of_birth:
        cursor.execute('UPDATE Students SET DateOfBirth = ? WHERE ID = ?', (date_of_birth, student_id))
    conn.commit()
    conn.close()

def update_teacher(teacher_id, name=None, surname=None, department=None):
    conn = connect_db()
    cursor = conn.cursor()
    if name:
        cursor.execute('UPDATE Teachers SET Name = ? WHERE ID = ?', (name, teacher_id))
    if surname:
        cursor.execute('UPDATE Teachers SET Surname = ? WHERE ID = ?', (surname, teacher_id))
    if department:
        cursor.execute('UPDATE Teachers SET Department = ? WHERE ID = ?', (department, teacher_id))
    conn.commit()
    conn.close()

def update_course(course_id, title=None, description=None, teacher_id=None):
    conn = connect_db()
    cursor = conn.cursor()
    if title:
        cursor.execute('UPDATE Courses SET Title = ? WHERE ID = ?', (title, course_id))
    if description:
        cursor.execute('UPDATE Courses SET Description = ? WHERE ID = ?', (description, course_id))
    if teacher_id:
        cursor.execute('UPDATE Courses SET TeacherID = ? WHERE ID = ?', (teacher_id, course_id))
    conn.commit()
    conn.close()

# 3. Удаление студентов, преподавателей, курсов и экзаменов
def delete_student(student_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Students WHERE ID = ?', (student_id,))
    conn.commit()
    conn.close()

def delete_teacher(teacher_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Teachers WHERE ID = ?', (teacher_id,))
    conn.commit()
    conn.close()

def delete_course(course_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Courses WHERE ID = ?', (course_id,))
    conn.commit()
    conn.close()

def delete_exam(exam_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Exams WHERE ID = ?', (exam_id,))
    conn.commit()
    conn.close()

# 4. Получение списка студентов по факультету
def get_students_by_department(department):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Students WHERE Department = ?', (department,))
    students = cursor.fetchall()
    conn.close()
    return students

# 5. Получение списка курсов, читаемых определенным преподавателем
def get_courses_by_teacher(teacher_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Courses WHERE TeacherID = ?', (teacher_id,))
    courses = cursor.fetchall()
    conn.close()
    return courses

# 6. Получение списка студентов, зачисленных на конкретный курс
def get_students_by_course(course_id):
    conn = connect_db()
    cursor = conn.cursor()
    query = '''
        SELECT Students.* FROM Students
        JOIN Grades ON Students.ID = Grades.StudentID
        JOIN Exams ON Grades.ExamID = Exams.ID
        WHERE Exams.CourseID = ?
    '''
    cursor.execute(query, (course_id,))
    students = cursor.fetchall()
    conn.close()
    return students

# 7. Получение оценок студентов по определенному курсу
def get_grades_by_course(course_id):
    conn = connect_db()
    cursor = conn.cursor()
    query = '''
        SELECT Students.Name, Students.Surname, Grades.Score FROM Grades
        JOIN Students ON Grades.StudentID = Students.ID
        JOIN Exams ON Grades.ExamID = Exams.ID
        WHERE Exams.CourseID = ?
    '''
    cursor.execute(query, (course_id,))
    grades = cursor.fetchall()
    conn.close()
    return grades

# 8. Средний балл студента по определенному курсу
def get_average_score_by_student_and_course(student_id, course_id):
    conn = connect_db()
    cursor = conn.cursor()
    
    query = '''
        SELECT AVG(Grades.Score) FROM Grades
        JOIN Exams ON Grades.ExamID = Exams.ID
        WHERE Grades.StudentID = ? AND Exams.CourseID = ?
    '''
    
    cursor.execute(query, (student_id, course_id))
    
    average_score = cursor.fetchone()[0]
    
    conn.close()
    
    return average_score

# 9. Средний балл студента в целом
def get_average_score_by_student(student_id):
    conn = connect_db()
    cursor = conn.cursor()

    query = '''
        SELECT AVG(Score) FROM Grades
        WHERE StudentID = ?
    '''

    cursor.execute(query, (student_id,))
    
    average_score = cursor.fetchone()[0]
    
    conn.close()

    return average_score

# 10. Средний балл по факультету
def get_average_score_by_department(department):
    conn = connect_db()
    cursor = conn.cursor()

    query = '''
        SELECT AVG(Grades.Score) FROM Grades
        JOIN Students ON Grades.StudentID = Students.ID
        WHERE Students.Department = ?
    '''

    cursor.execute(query, (department,))
    
    average_score = cursor.fetchone()[0]
    
    conn.close()

    return average_score

