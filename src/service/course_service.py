


from models.course import Course
from models.student import Student
from dao.course_dao import CourseDAO
from service.enrollment import EnrollmentService


class CourseService:

    def __init__(self):
        self.course_dao = CourseDAO()
        self.enrollment_service = EnrollmentService()

    def save(self, course: Course) -> None:
        saved_course = self.course_dao.save(course)
        if saved_course:
            print(f"Course {saved_course.id}: {saved_course.name} saved successfully")
        else:
            print(f"Failed to save course {course.name}")

    def get_all_courses(self) -> list[Course]:
        return self.course_dao.get_all_courses()
    
    def get_course_by_id(self, course_id: int) -> Course | None:
        return self.course_dao.get_course_by_id(course_id)
    
    def update_course(self, course_id: int, updated_name: str, updated_professor_id: int) -> bool:

        course = self.get_course_by_id(course_id)

        if course is None:
            print(f"No course found with ID {course_id}. Update failed.")
            return False
        
        course.name = updated_name or course.name
        course.professor_id = updated_professor_id or course.professor_id
        
        result = self.course_dao.update_course(course)
        if result:
            print(f"Course {course.id}: {course.name} updated successfully")
        return result
    
    def delete_course(self, course_id: int) -> bool:
        return self.course_dao.delete_course(course_id)
    
    def enroll_student(self, course_id: int, student_id: int) -> bool:

        course = self.get_course_by_id(course_id)

        if course is None:
            print(f"No course found with ID {course_id}. Enrollment failed.")
            return False
        
        result = self.enrollment_service.enroll_student(student_id, course_id)
        return result is not None
    
    def drop_student(self, course_id: int, student_id: int) -> bool:
        return self.enrollment_service.drop_student(student_id, course_id)
    
    def get_enrolled_students(self, course_id: int) -> list[Student] | None:

        course = self.get_course_by_id(course_id)

        if course is None:
            print(f"No course found with ID {course_id}.")
            return None
        
        return self.enrollment_service.get_students_in_course(course_id)
    
    def get_courses_for_student(self, student_id: int) -> list[Course]:
        return self.enrollment_service.get_courses_for_student(student_id)