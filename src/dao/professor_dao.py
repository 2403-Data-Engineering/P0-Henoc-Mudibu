from contextlib import closing
from dao.db_connection import DBConnection
from mysql.connector import Error
from models.professor import Professor

class ProfessorDAO:

    def save(self, professor: Professor) -> Professor | None:

        # Insert SQL query to save professor to the database
        sql = """
            INSERT INTO professors (first_name, last_name, email, department)
            VALUES (%s, %s, %s, %s)
        """

        values = (
            professor.first_name,
            professor.last_name,
            professor.email,
            professor.department   
        )

        try:
            with DBConnection().get_connection() as conn:
                with closing(conn.cursor()) as cursor:

                    cursor.execute(sql, values)

                    conn.commit()

                    professor.id = cursor.lastrowid
                    return professor
        
        except Error as e:
            print(f"Error while saving professor: {e}")
            return None
        

    def get_professor_by_id(self, professor_id: int) -> Professor | None:
        
        sql= """SELECT * FROM professors WHERE professor_id = %s"""

        try:
            with DBConnection().get_connection() as conn:
                with closing(conn.cursor()) as cursor:

                    cursor.execute(sql, (professor_id,))
                    
                    row = cursor.fetchone()

                    if row:
                        return Professor(
                            id=row[0],
                            first_name=row[1],
                            last_name=row[2],
                            department=row[3],
                            email=row[4]
                        )
                    return None
                
        except Error as e:
            print(f"Error while retrieving professor: {e}")
            return None
        

    def get_all_professors(self) -> list[Professor]:

        sql= """SELECT * FROM professors"""

        professors= []

        try:
            with DBConnection().get_connection() as conn:
                with closing(conn.cursor()) as cursor:

                    cursor.execute(sql)

                    rows = cursor.fetchall()

                    for row in rows:
                        professors.append(Professor(
                            id=row[0],
                            first_name=row[1],
                            last_name=row[2],
                            department=row[3],
                            email=row[4]
                        ))

                    return professors
                
        except Error as e:
            print(f"Error while retrieving professors: {e}")
            return []

    def update_professor(self, professor: Professor) -> bool:

        sql = """
            UPDATE professors
            SET first_name = %s, last_name = %s, department = %s, email = %s
            WHERE professor_id = %s
            """

        values = (
            professor.first_name if professor.first_name else None,
            professor.last_name if professor.last_name else None,
            professor.department if professor.department else None,
            professor.email if professor.email else None,
            professor.id    
        )

        try:
            with DBConnection().get_connection() as conn:
                with closing(conn.cursor()) as cursor:

                    cursor.execute(sql, values)

                    conn.commit()

                    return cursor.rowcount > 0
                
        except Error as e:
            print(f"Error while updating professor: {e}")
            return False
        
    def delete_professor(self, professor_id: int) -> bool:

        sql = "DELETE FROM professors WHERE professor_id = %s"

        try:
            with DBConnection().get_connection() as conn:
                with closing(conn.cursor()) as cursor:

                    cursor.execute(sql, (professor_id,))

                    conn.commit()

                    return cursor.rowcount > 0
                
        except Error as e:
            print(f"Error while deleting professor: {e}")
            return False