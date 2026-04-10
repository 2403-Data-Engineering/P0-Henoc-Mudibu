from contextlib import closing
from mysql.connector import Error
from models.enrollment import Enrollment
from models.student import Student
from models.course import Course
from dao.db_connection import DBConnection


class EnrollmentDAO:

    def enroll_student(self, enrollment: Enrollment) -> Enrollment | None:
        # Insert a student-course relationship into enrollments table
        query = """
            INSERT INTO enrollments (student_id, course_id)
            VALUES (%s, %s)
        """

        values = (enrollment.student_id, enrollment.course_id)

        try:
            with DBConnection().get_connection() as conn:
                with closing(conn.cursor()) as cursor:
                    cursor.execute(query, values)
                    conn.commit()

                    enrollment.enrollment_id = cursor.lastrowid
                    return enrollment
        except Error as e:
            print(f"Error enrolling student: {e}")
            return None

    def drop_student(self, student_id: int, course_id: int) -> bool:
        # Delete a student-course enrollment
        query = """
            DELETE FROM enrollments
            WHERE student_id = %s AND course_id = %s
        """

        try:
            with DBConnection().get_connection() as conn:
                with closing(conn.cursor()) as cursor:
                    cursor.execute(query, (student_id, course_id))
                    conn.commit()
                    return cursor.rowcount > 0
        except Error as e:
            print(f"Error dropping student from course: {e}")
            return False

    def get_students_in_course(self, course_id: int) -> list[Student]:
        # Join enrollments with students to return all students in a course
        query = """
            SELECT s.id, s.first_name, s.last_name, s.major, s.email, s.year
            FROM enrollments e
            JOIN students s ON e.student_id = s.id
            WHERE e.course_id = %s
        """

        students = []

        try:
            with DBConnection().get_connection() as conn:
                with closing(conn.cursor()) as cursor:
                    cursor.execute(query, (course_id,))
                    rows = cursor.fetchall()

                    for row in rows:
                        students.append(
                            Student(
                                id=row[0],
                                first_name=row[1],
                                last_name=row[2],
                                major=row[3],
                                email=row[4],
                                year=row[5]
                            )
                        )

            return students
        except Error as e:
            print(f"Error fetching students in course: {e}")
            return []

    def get_courses_for_student(self, student_id: int) -> list[Course]:
        # Join enrollments with courses to return all courses for a student
        query = """
            SELECT c.course_id, c.course_name, c.course_code, c.course_description, c.professor_id
            FROM enrollments e
            JOIN courses c ON e.course_id = c.course_id
            WHERE e.student_id = %s
        """

        courses = []

        try:
            with DBConnection().get_connection() as conn:
                with closing(conn.cursor()) as cursor:
                    cursor.execute(query, (student_id,))
                    rows = cursor.fetchall()

                    for row in rows:
                        courses.append(
                            Course(
                                id=row[0],
                                name=row[1],
                                code=row[2],
                                description=row[3],
                                professor_id=row[4]
                            )
                        )

            return courses
        except Error as e:
            print(f"Error fetching courses for student: {e}")
            return []

    def get_enrollment(self, student_id: int, course_id: int) -> Enrollment | None:
        # Check whether a specific enrollment already exists
        query = """
            SELECT enrollment_id, student_id, course_id, enrollment_date
            FROM enrollments
            WHERE student_id = %s AND course_id = %s
        """

        try:
            with DBConnection().get_connection() as conn:
                with closing(conn.cursor()) as cursor:
                    cursor.execute(query, (student_id, course_id))
                    row = cursor.fetchone()

                    if row:
                        return Enrollment(
                            enrollment_id=row[0],
                            student_id=row[1],
                            course_id=row[2],
                            enrollment_date=row[3]
                        )
                    return None
        except Error as e:
            print(f"Error checking enrollment: {e}")
            return None

    def get_all_enrollments_report(self):

        query = """
            SELECT s.first_name, s.last_name, s.email, s.major, c.course_name, e.enrollment_date
            FROM enrollments e
            JOIN students s ON e.student_id = s.id
            JOIN courses c ON e.course_id = c.course_id
            ORDER BY e.enrollment_date DESC
            """
        
        try:
            with DBConnection().get_connection() as conn:
                with closing(conn.cursor()) as cursor:

                    cursor.execute(query)
                    return cursor.fetchall()
                
        except Error as e:
            print(f"Error fetching enrollment report: {e}")
            return []
