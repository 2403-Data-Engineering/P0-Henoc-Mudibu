from dao.enrollment_dao import EnrollmentDAO
from models.enrollment import Enrollment
from models.student import Student
from models.course import Course


class EnrollmentService:

    def __init__(self):
        self.enrollment_dao = EnrollmentDAO()

    def enroll_student(self, student_id: int, course_id: int) -> Enrollment | None:
        
        if not student_id or not course_id:
            print("Student ID and Course ID are required for enrollment.")
            return None
        
        # Check if already enrolled
        existing_enrollment = self.enrollment_dao.get_enrollment(student_id, course_id)
        if existing_enrollment:
            print(f"Student {student_id} is already enrolled in course {course_id}.")
            return None
        
        enrollment = Enrollment(
            enrollment_id=None,
            student_id=student_id,
            course_id=course_id
        )
        
        result = self.enrollment_dao.enroll_student(enrollment)
        
        if result:
            print(f"Student {student_id} enrolled in course {course_id} successfully.")
        else:
            print(f"Failed to enroll student {student_id} in course {course_id}.")
        
        return result
    
    def drop_student(self, student_id: int, course_id: int) -> bool:
        
        if not student_id or not course_id:
            print("Student ID and Course ID are required for dropping.")
            return False
        
        result = self.enrollment_dao.drop_student(student_id, course_id)
        
        if result:
            print(f"Student {student_id} dropped from course {course_id} successfully.")
        else:
            print(f"Failed to drop student {student_id} from course {course_id}.")
        
        return result
    
    def get_students_in_course(self, course_id: int) -> list[Student]:
        
        if not course_id:
            print("Course ID is required.")
            return []
        
        return self.enrollment_dao.get_students_in_course(course_id)
    
    def get_courses_for_student(self, student_id: int) -> list[Course]:
        
        if not student_id:
            print("Student ID is required.")
            return []
        
        return self.enrollment_dao.get_courses_for_student(student_id)
