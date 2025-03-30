import sqlite3


def runQuery (crsr, qryString, qryIntro):
    crsr.execute(qryString)
    ans = crsr.fetchall()
    print (qryIntro, ":")
    for i in ans:
        print (i)

# Task 1: Create a New SQLite Database
# Write code to connect to a new SQLite database, ./db/new.db and to close the connection.
with  sqlite3.connect("./db/new.db") as conn:  # Create the file here, so that it is not pushed to GitHub!
    print("Database created and connected successfully.")

    # Task 2: Define Database Structure
    #Add SQL statements to sql_intro.py that create the following tables:
    #  Students: Include fields for student ID, name, age, and major.
    #  Courses: Include fields for course ID, course name, and instructor name.
    #  Enrollments: Include fields for enrollment ID, student ID, and course ID. The student ID and course ID in the Enrollments table should be foreign keys. Each of these values must correspond to actual records in the Students and Courses tables.
    cursor = conn.cursor()
    if (True):
        # Create tables
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Students (
            student_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER,
            major TEXT
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Courses (
            course_id INTEGER PRIMARY KEY,
            course_name TEXT NOT NULL,
            instructor_name TEXT
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Enrollments (
            enrollment_id INTEGER PRIMARY KEY,
            student_id INTEGER,
            course_id INTEGER,
            FOREIGN KEY (student_id) REFERENCES Students (student_id),
            FOREIGN KEY (course_id) REFERENCES Courses (course_id)
        )
        """)

        print("Tables created successfully.")

        conn.execute("PRAGMA foreign_keys = 1")

        # Add code to sql_intro.py to insert sample data into the Students, Courses, and Enrollments tables. Don't forget to do a conn.commit() for your inserts!
        cursor.execute("INSERT INTO Students (name, age, major) VALUES ('Alice', 20, 'Computer Science')")
        cursor.execute("INSERT INTO Students (name, age, major) VALUES ('Alice', 20, 'Computer Science')")
        cursor.execute("INSERT INTO Students (name, age, major) VALUES ('Bob', 22, 'History')") 
        cursor.execute("INSERT INTO Students (name, age, major) VALUES ('Charlie', 19, 'Biology')") 
        cursor.execute("INSERT INTO Courses (course_name, instructor_name) VALUES ('Math 101', 'Dr. Smith')")
        cursor.execute("INSERT INTO Courses (course_name, instructor_name) VALUES ('English 101', 'Ms. Jones')") 
        cursor.execute("INSERT INTO Courses (course_name, instructor_name) VALUES ('Chemistry 101', 'Dr. Lee')") 
        cursor.execute("INSERT INTO Enrollments (student_id, course_id) VALUES (1, 1)") 
        cursor.execute("INSERT INTO Enrollments (student_id, course_id) VALUES (1, 2)") 
        cursor.execute("INSERT INTO Enrollments (student_id, course_id) VALUES (2, 1)") 
        cursor.execute("INSERT INTO Enrollments (student_id, course_id) VALUES (3, 3)") 

        conn.commit() 
        print("Sample data inserted successfully.")


    # Task 5
    # execute the command to fetch all the data from the table emp
    runQuery (cursor, "Select * from Students", "Student Information")

    # Write a query to find courses taught by a specific instructor.
    INSTRUCTOR = "Dr. Smith"
    runQuery (cursor, f'SELECT * FROM Courses WHERE instructor_name = "{INSTRUCTOR}";', f'Courses taught by {INSTRUCTOR}')

    # Write a query to retrieve student enrollments along with course names using a JOIN.
    queryString = "SELECT Students.name, Courses.course_name \
                    FROM Enrollments \
                    JOIN Students ON Enrollments.student_id = Students.student_id \
                    JOIN Courses ON Enrollments.course_id = Courses.course_id; "
    runQuery (cursor, queryString, "Students and classes")

    # Write a query to list students ordered by age.
    queryString = "SELECT * FROM Students ORDER BY age;"
    runQuery (cursor, queryString, "Students by age")


