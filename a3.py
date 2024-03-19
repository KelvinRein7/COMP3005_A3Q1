import psycopg2
from psycopg2 import Error
from datetime import date

#Database connection info
hostname = "localhost"
dbname = "A3Q1"
username = "postgres"
dbpassword = "142002"
portnumber = "5432"

#Connecting to Postgre SQL DB
def connect():
    try:
        connection = psycopg2.connect(
            user=username,
            password=dbpassword,
            host=hostname,
            database=dbname,
            port=portnumber
        )
        return connection
    except Error as e:
        print(f"Error while connecting to the database: {e}")
        return None

#Get all students in database
def getAllStudents():

    try:
        connection = connect()
        cur = connection.cursor()
        cur.execute("SELECT * FROM students;")

        students = cur.fetchall()
        print("All Students:")

        for student in students:
            print(student)

        print()

        cur.close()
        connection.close()

    except Error as e:
        print(f"Error while fetching all students: {e}")

#Inserting a new student to students table
def addStudent(first_name, last_name, email, enrollment_date):

    try:
        connection = connect()
        cur = connection.cursor()
        cur.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s);",
                       (first_name, last_name, email, enrollment_date))
        connection.commit()
        print("Student added successfully to database!")

        cur.close()
        connection.close()

    except Error as e:
        print(f"Error while adding student: {e}")

#Update the email of the student by id
def updateStudentEmail(student_id, new_email):

    try:
        connection = connect()
        cur = connection.cursor()
        cur.execute("UPDATE students SET email = %s WHERE student_id = %s;", 
                    (new_email, student_id))
        
        connection.commit()
        print("Student email updated successfully to database!")

        cur.close()
        connection.close()

    except Error as e:
        print(f"Error while updating student email: {e}")

#Remove student from database by id
def deleteStudent(student_id):
    try:
        connection = connect()
        cur = connection.cursor()
        cur.execute("DELETE FROM students WHERE student_id = %s;", 
                    (student_id,))
        
        connection.commit()
        print("Student deleted successfully from database!")

        cur.close()
        connection.close()

    except Error as e:
        print(f"Error while deleting student: {e}")

# Main
def main():

    connection = connect()

    #Insert students
    addStudent('John', 'Doe', 'john.doe@example.com', date(2023, 9, 1))
    addStudent('Jane', 'Smith', 'jane.smith@example.com', date(2023, 9, 1))
    addStudent('Jim', 'Beam', 'jim.beam@example.com', date(2023, 9, 2))

    #Get all students in db
    getAllStudents()

    #Update a student's email by id
    updateStudentEmail(3, 'john.doe.updated@example.com')

    #Get students after email is updated
    print("All students after email update:")
    getAllStudents()

    #Remove a student from database by id
    deleteStudent(2)

    #Get students list after removing a student
    print("All students after deletion:")
    getAllStudents()

    connection.close()

if __name__ == "__main__":
    main()
