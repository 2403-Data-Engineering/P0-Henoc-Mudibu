from contextlib import closing
from dao.db_connection import DBConnection
from mysql.connector import Error
from models.course import Course


class CourseDAO:

    def save(self, course: Course) -> Course | None:
        
        sql = """
            INSERT INTO courses (course_name, course_code, course_description, professor_id)
            VALUES (%s, %s, %s, %s)
        """
        
        values = (
            course.name,
            course.code,
            course.description,
            course.professor_id
        )
        
        try:
            with DBConnection().get_connection() as conn:
                with closing(conn.cursor()) as cursor:
                    cursor.execute(sql, values)
                    conn.commit()
                    course.id = cursor.lastrowid
                    print(f"Course '{course.name}' saved successfully with ID {course.id}.")
                    return course
        except Error as e:
            print(f"Error while saving course: {e}")
            return None
    
    def get_course_by_id(self, course_id: int) -> Course | None:
        
        if course_id is None or course_id <= 0:
            print("Course ID is required and must be valid.")
            return None
        
        sql = """
            SELECT course_id, course_name, course_code, course_description, professor_id 
            FROM courses 
            WHERE course_id = %s
        """
        
        try:
            with DBConnection().get_connection() as conn:
                with closing(conn.cursor()) as cursor:
                    cursor.execute(sql, (course_id,))
                    row = cursor.fetchone()
                    
                    if row:
                        return Course(
                            id=row[0],
                            name=row[1],
                            code=row[2],
                            description=row[3],
                            professor_id=row[4]
                        )
                    return None
        except Error as e:
            print(f"Error while retrieving course: {e}")
            return None
    
    def get_all_courses(self) -> list[Course]:
        
        sql = """
            SELECT course_id, course_name, course_code, course_description, professor_id 
            FROM courses
        """
        
        courses = []
        
        try:
            with DBConnection().get_connection() as conn:
                with closing(conn.cursor()) as cursor:
                    cursor.execute(sql)
                    rows = cursor.fetchall()
                    
                    if rows:
                        for row in rows:
                            courses.append(Course(
                                id=row[0],
                                name=row[1],
                                code=row[2],
                                description=row[3],
                                professor_id=row[4]
                            ))
                    else:
                        print("No courses found in the database.")
            
            return courses
        except Error as e:
            print(f"Error while retrieving courses: {e}")
            return []
    
    def update_course(self, course: Course) -> bool:
        
        sql = """
            UPDATE courses
            SET course_name = %s, 
                course_code = %s, 
                course_description = %s, 
                professor_id = %s
            WHERE course_id = %s
        """
        
        values = (
            course.name,
            course.code,
            course.description,
            course.professor_id,
            course.id
        )
        
        try:
            with DBConnection().get_connection() as conn:
                with closing(conn.cursor()) as cursor:
                    cursor.execute(sql, values)
                    conn.commit()
                    
                    if cursor.rowcount > 0:
                        print(f"Course with ID {course.id} updated successfully.")
                        return True
                    else:
                        print(f"No course found with ID {course.id}. Update failed.")
                        return False
        except Error as e:
            print(f"Error while updating course: {e}")
            return False
    
    def delete_course(self, course_id: int) -> bool:
        
        sql = "DELETE FROM courses WHERE course_id = %s"
        
        try:
            with DBConnection().get_connection() as conn:
                with closing(conn.cursor()) as cursor:
                    cursor.execute(sql, (course_id,))
                    conn.commit()
                    
                    if cursor.rowcount > 0:
                        print(f"Course with ID {course_id} deleted successfully.")
                        return True
                    else:
                        print(f"No course found with ID {course_id}. Delete failed.")
                        return False
        except Error as e:
            print(f"Error while deleting course: {e}")
            return False
