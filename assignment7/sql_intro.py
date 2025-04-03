import sqlite3

DUPEERROR = "UNIQUE constraint failed:"

def runQuery (crsr, qryString, qryIntro):
    crsr.execute(qryString)
    ans = crsr.fetchall()
    print (qryIntro, ":")
    for i in ans:
        print (i)

# Task 1: Create a New SQLite Database
# Write code to connect to a new SQLite database, ./db/new.db and to close the connection.
with  sqlite3.connect("../db/magazines.db") as conn:  # Create the file here, so that it is not pushed to GitHub!
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
        CREATE TABLE IF NOT EXISTS Publishers (
            publisher_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Magazines (
            magazine_id INTEGER PRIMARY KEY,
            magazine_name TEXT NOT NULL,
            publisher_id INTEGER,
            FOREIGN KEY (publisher_id) REFERENCES Publishers (publisher_id)

        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Subscribers (
            subscriber_id INTEGER PRIMARY KEY,
            subscriber_name TEXT NOT NULL,
            subscriber_addr TEXT NOT NULL

        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Subscriptions (
            subscription_id INTEGER PRIMARY KEY,
            subscriber_id INTEGER,
            magazine_id INTEGER,
            expiration_date STRING NOT NULL,
            FOREIGN KEY (subscriber_id) REFERENCES Subscribers (subscriber_id),
            FOREIGN KEY (magazine_id) REFERENCES Magazines (magazine_id)
        )
        """)

        print("Tables created successfully.")

        # Task 4: Populate Tables with Data

        conn.execute("PRAGMA foreign_keys = 1")

        def generalInsert (qry, values):
            try:
                cursor.execute(qry, values)
                conn.commit()
                print("Record inserted successfully.")
            except Exception as e:
                if (e.sqlite_errorname != "SQLITE_CONSTRAINT_PRIMARYKEY"):          
                    print(f"Error inserting record for {qry}: {e}")    

        def addPublisher(pub_data):
            qryString = "INSERT INTO Publishers (publisher_id,name) VALUES (?, ?)"
            generalInsert (qryString, pub_data)

        def addMagazine(mag_data):
            qryString = "INSERT INTO Magazines (magazine_id, publisher_id, magazine_name) VALUES (?, ?, ?)"
            generalInsert (qryString, mag_data)
        
        def addSubscriber (sub_data):
            qryString = "INSERT INTO Subscribers (subscriber_id, subscriber_name, subscriber_addr) VALUES (?,?,?)"
            generalInsert (qryString, sub_data)
        
        def addSubscripion (subscription_data):
            qryString = "INSERT INTO Subscriptions (subscription_id, magazine_id, subscriber_id, expiration_date) VALUES (?,?,?,?)"
            generalInsert (qryString, subscription_data)

        # Add Three publishers
        addPublisher ((1, "Newsweek Inc."))
        addPublisher ((2, "Time Inc."))
        addPublisher ((3, "Dotdash Meredith"))

        # Add Magazines
        addMagazine ((1, 1, "Newsweek"))
        addMagazine ((2, 2, "Time"))
        addMagazine ((3, 3, "People"))

        # Subscribers
        addSubscriber ((1, "Dave Cowens", "34 Main Street, Reading MA"))
        addSubscriber ((2, "Nate Archibald", "35 Main Street, Reading MA"))
        addSubscriber ((3, "Steve Nelson", "36 Main Street, Reading, MA"))

        # Subscriptions
        addSubscripion ((1, 1, 1, "August 1, 2026"))
        addSubscripion ((2, 2, 2, "August 1, 2026"))
        addSubscripion ((3, 3, 3, "August 1, 2026"))

        # Task 5: Write SQL Queries        

        def genQuery (qryString, title):
            cursor.execute (qryString)
            results = cursor.fetchall()
            print (title)
            for row in results:
                print("   ", row)     

        # Write a query to retrieve all information from the subscribers table.
        genQuery ("SELECT * FROM Subscribers", "Subscribers:")
  

        # Write a query to retrieve all magazines sorted by name.
        genQuery ("Select * FROM Magazines ORDER BY magazine_name", "Magazines Sorted By Name:")

        # Wite a query to find magazines for a particular publisher, one of the publishers you created. This requires a JOIN.
        genQuery ("Select Publishers.name, Magazines.magazine_name FROM Magazines \
                  INNER JOIN Publishers ON Magazines.publisher_id = Publishers.publisher_id WHERE Publishers.PUBLISHER_ID = 1", \
                  "Magazines and Publishers:")


