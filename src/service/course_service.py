


from models.course import Course
from models.student import Student


class CourseService:

    def __init__(self):
        self.courses_list: list[Course] = []

    def save(self, course: Course) -> None:
        self.courses_list.append(course)
        print(f"Course {course.id}: {course.name} saved successfully")

    def get_all_courses(self) -> list[Course]:
        return self.courses_list
    
    def get_course_by_id(self, course_id: int) -> Course | None:

        for course in self.courses_list:
            if course.id == course_id:
                return course
        return None
    
    def update_course(self, course_id: int, updated_name: str, updated_professor_id: int) -> bool:

        course = self.get_course_by_id(course_id)

        if course is None:
            print(f"No course found with ID {course_id}. Update failed.")
            return False
        
        course.name = updated_name or course.name
        course.professor_id = updated_professor_id or course.professor_id
        print(f"Course {course.id}: {course.name} updated successfully")
        return True
    
    def delete_course(self, course_id: int) -> bool:

        course = self.get_course_by_id(course_id)

        if course is None:
            print(f"No course found with ID {course_id}. Deletion failed.")
            return False
        
        self.courses_list.remove(course)
        print(f"Course {course.id}: {course.name} deleted successfully")
        return True
    
    def enroll_student(self, course_id: int, student: Student) -> bool:

        course = self.get_course_by_id(course_id)

        if course is None:
            print(f"No course found with ID {course_id}. Enrollment failed.")
            return False
        
        if student in course.enrolled_students:
            print(f"Student {student.first_name} {student.last_name} is already enrolled in course {course.name}.")
            return False
        
        course.enrolled_students.append(student)
        print(f"Student {student.first_name} {student.last_name} enrolled in course {course.name} successfully.")
        return True
    
    def drop_student(self, course_id: int, student_id: int) -> bool:

        course = self.get_course_by_id(course_id)

        if course is None:
            print(f"No course found with ID {course_id}. Drop failed.")
            return False
        
        student_to_drop = None
        for student in course.enrolled_students:
            if student.id == student_id:
                student_to_drop = student
                break
        
        if student_to_drop is None:
            print(f"No student found with ID {student_id} in course {course.name}. Drop failed.")
            return False
        
        course.enrolled_students.remove(student_to_drop)
        print(f"Student {student_to_drop.first_name} {student_to_drop.last_name} dropped from course {course.name} successfully.")
        return True
    
    def get_enrolled_students(self, course_id: int) -> list[Student] | None:

        course = self.get_course_by_id(course_id)

        if course is None:
            print(f"No course found with ID {course_id}.")
            return None
        
        return course.enrolled_students
    
    def get_courses_for_student(self, student_id: int) -> list[Course]:

        return [course for course in self.courses_list if any(student.id == student_id for student in course.enrolled_students)]