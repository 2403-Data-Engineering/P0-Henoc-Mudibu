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
        
    
    def get_student_by_id(self, student_id: int) -> Student | None:

        if student_id is None:
            print("Student ID is required to retrieve student.")
            return None
        
        if student_id <= 0:
            print("Enter a valid Student ID")
            return None
        
        sql= """
            SELECT id, first_name, last_name, major, email, year FROM students WHERE id = %s
            """
        
        try:
            with DBConnection().get_connection() as conn:

                with closing(conn.cursor()) as cursor:

                    cursor.execute(sql, (student_id,))

                    row = cursor.fetchone()

                    if row:
                        return Student(
                            id=row[0],
                            first_name=row[1],
                            last_name=row[2],
                            major=row[3],
                            email=row[4],
                            year=row[5]
                        )
                return None
        except Error as e:
            print(f"Error while retrieving student: {e}")
            return None
        
    def get_all_students(self) -> list[Student]:

        sql = "SELECT * FROM students"

        students =[]

        try:
            with DBConnection().get_connection() as conn:

                with closing(conn.cursor()) as cursor:

                    cursor.execute(sql)

                    rows = cursor.fetchall()

                    if rows:
                        for row in rows:
                            students.append(Student(
                                id=row[0],
                                first_name=row[1],
                                last_name=row[2],
                                major=row[3],
                                email=row[4],
                                year=row[5]
                            )
                        )
                    else:
                        print("No students found in the database.")
        
                return students
            
        except Error as e:
            print(f"Error while retrieving students: {e}")
            return []
                        

        

    def update_student(self, student: Student) -> bool:
        
        sql= """
            UPDATE students
            SET first_name = COALESCE(%s, first_name),
                last_name = COALESCE(%s, last_name),
                major = COALESCE(%s, major),
                email = COALESCE(%s, email),
                year = COALESCE(%s, year)
            WHERE id = %s
        """

        values = (
            student.first_name if student.first_name else None,
            student.last_name if student.last_name else None,
            student.major if student.major else None,
            student.email if student.email else None,
            student.year if student.year else None,
            student.id
        )

        try:
            with DBConnection().get_connection() as conn:

                with closing(conn.cursor()) as cursor:

                    cursor.execute(sql, values)

                    conn.commit()

                    if cursor.rowcount > 0:
                        print(f"Student with ID {student.id} updated successfully.")
                        return True
                    else:
                        print(f"No student found with ID {student.id}. Update failed.")
                        return False
                    
        except Error as e:
            print(f"Error while updating student: {e}")
            return False
        

    def delete_student(self, student_id: int) -> bool:

        sql= "DELETE FROM students WHERE id = %s"

        try:
            with DBConnection().get_connection() as conn:
                with closing(conn.cursor()) as cursor:

                    cursor.execute(sql, (student_id,))

                    conn.commit()

                    if cursor.rowcount > 0:
                        print(f"Student with ID {student_id} deleted successfully.")
                        return True
                    else:
                        print(f"No student found with ID {student_id}. Deletion failed.")
                        return False
                    
        except Error as e:
            print(f"Error while deleting student: {e}")
            return False