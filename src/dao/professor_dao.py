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