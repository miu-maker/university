import sqlite3


conn = sqlite3.connect('university.db')


cursor = conn.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS Students (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Surname TEXT NOT NULL,
    Department TEXT NOT NULL,
    DateOfBirth DATE NOT NULL
);
''')


cursor.execute('''
CREATE TABLE IF NOT EXISTS Teachers (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Surname TEXT NOT NULL,
    Department TEXT NOT NULL
);
''')


cursor.execute('''
CREATE TABLE IF NOT EXISTS Courses (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Title TEXT NOT NULL,
    Description TEXT,
    TeacherID INTEGER,
    FOREIGN KEY (TeacherID) REFERENCES Teachers(ID)
);
''')


cursor.execute('''
CREATE TABLE IF NOT EXISTS Exams (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Date DATE NOT NULL,
    CourseID INTEGER,
    MaxScore INTEGER NOT NULL,
    FOREIGN KEY (CourseID) REFERENCES Courses(ID)
);
''')


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


conn.commit()
conn.close()

print("База данных и таблицы созданы успешно.")
