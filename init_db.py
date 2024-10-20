import sqlite3

# Подключение к базе данных (если базы данных нет, она будет создана)
conn = sqlite3.connect('university.db')

# Создание объекта курсора
cursor = conn.cursor()

# Создание таблицы студентов
cursor.execute('''
CREATE TABLE IF NOT EXISTS Students (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Surname TEXT NOT NULL,
    Department TEXT NOT NULL,
    DateOfBirth DATE NOT NULL
);
''')

# Создание таблицы преподавателей
cursor.execute('''
CREATE TABLE IF NOT EXISTS Teachers (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Surname TEXT NOT NULL,
    Department TEXT NOT NULL
);
''')

# Создание таблицы курсов
cursor.execute('''
CREATE TABLE IF NOT EXISTS Courses (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Title TEXT NOT NULL,
    Description TEXT,
    TeacherID INTEGER,
    FOREIGN KEY (TeacherID) REFERENCES Teachers(ID)
);
''')

# Создание таблицы экзаменов
cursor.execute('''
CREATE TABLE IF NOT EXISTS Exams (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Date DATE NOT NULL,
    CourseID INTEGER,
    MaxScore INTEGER NOT NULL,
    FOREIGN KEY (CourseID) REFERENCES Courses(ID)
);
''')

# Создание таблицы оценок
cursor.execute('''
CREATE TABLE IF NOT EXISTS Grades (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    StudentID INTEGER,
    ExamID INTEGER,
    Score INTEGER NOT NULL,
    FOREIGN KEY (StudentID) REFERENCES Students(ID),
    FOREIGN KEY (ExamID) REFERENCES Exams(ID)
);
''')

# Сохранение изменений и закрытие соединения
conn.commit()
conn.close()

print("База данных и таблицы созданы успешно.")