
import mysql.connector
from mysql.connector import Error


def get_connection():
    return mysql.connector.connect(
        host="127.0.0.1",
        port=3307,
        user="student",
        password="StudentPass123!",
        database="university_db",
    )


def create_table(connection):
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(150) NOT NULL UNIQUE
        )
    """)

    connection.commit()
    cursor.close()


def create_student(connection, name, email):
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO students (name, email) VALUES (%s, %s)",
        (name, email),
    )

    connection.commit()
    print(f"Student created with ID: {cursor.lastrowid}")
    cursor.close()


def read_students(connection):
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT id, name, email FROM students")
    students = cursor.fetchall()

    for student in students:
        print(student)

    cursor.close()


def update_student(connection, student_id, new_name):
    cursor = connection.cursor()

    cursor.execute(
        "UPDATE students SET name = %s WHERE id = %s",
        (new_name, student_id),
    )

    connection.commit()
    print(f"Rows updated: {cursor.rowcount}")
    cursor.close()


def delete_student(connection, student_id):
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM students WHERE id = %s",
        (student_id,),
    )

    connection.commit()
    print(f"Rows deleted: {cursor.rowcount}")
    cursor.close()


def main():
    connection = None

    try:
        connection = get_connection()
        create_table(connection)

        #create_student(connection, "Anna", "anna@example.com")
        update_student(connection, 1, "Anna Smith")
        read_students(connection)

        # delete_student(connection, 1)

    except Error as error:
        print(f"MySQL error: {error}")

    finally:
        if connection is not None and connection.is_connected():
            connection.close()


if __name__ == "__main__":
    main()

