from contextlib import closing
from dao.db_connection import DBConnection
from mysql.connector import Error
from models.student import Student


class StudentDAO:

    def save(self, student: Student) -> Student | None:

        sql= """
            INSERT INTO students (first_name, last_name, major, email, year) 
            VALUES (%s, %s, %s, %s, %s)
        """
        values = (
            student.first_name,
            student.last_name,
            student.major,
            student.email,
            student.year
        )

        try:
            with DBConnection().get_connection() as conn:

                with closing(conn.cursor()) as cursor:

                    cursor.execute(sql, values)

                    conn.commit()

                    # Retrieves the auto-generated ID for the new student
                    student.id = cursor.lastrowid

                    return student
        except Error as e:
            print(f"Error while saving student: {e}")
            return None