from __future__ import annotations
from typing import TYPE_CHECKING
from models.course import Course


if TYPE_CHECKING:
    from presentation.terminal import Terminal

from presentation.menu import Menu

class NewCourseMenu(Menu):

    def render(self):
        print("""
              ============================
               |     Add New Course     |
              ============================
              """)
        
        print("Enter the course ID:")
        id: int = int(input())
        print("Enter the course name:")
        name: str = input()
        print("Enter the course code:")
        code: str = input()
        print("Enter the course description:")
        description: str = input()

        professors = self.terminal.professor_service.get_all_professors()
        
        # Show professors to assign to the course
        if not professors:
            print("No professors available to assign to the course.")
            assigned_professor = None
        else:
            print("Available Professors:")
            for professor in professors:
                print(f"[{professor.id}] {professor.first_name} {professor.last_name} - {professor.department}")

            print("\nEnter professor ID to assign to the course (or press Enter to skip):")
            professor_id_input = input()

            professor_id = int(professor_id_input) if professor_id_input.strip() else None

        new_course = Course(id=id, name=name, code=code, description=description, assigned_professor_id=professor_id)
        self.terminal.course_service.save(new_course)

        print(f"Course '{new_course.name}' added successfully!")
        
        input("Press Enter to go back...")
        from presentation.menu import ManageCoursesMenu
        self.terminal.navigateToMenu(ManageCoursesMenu(self.terminal))


class ShowAllCoursesMenu(Menu):

    def render(self):
        print("""
              ============================
               |     All Courses     |
              ============================
              """)
        
        courses = self.terminal.course_service.get_all_courses()

        if not courses:
            print("No courses available.")
        else:
            for course in courses:

                if course.professor_id is None:
                    professor_name = "Unassigned"
                else:
                    professor = self.terminal.professor_service.get_professor_by_id(course.professor_id)
                    professor_name = f"{professor.first_name} {professor.last_name}" if professor else "Unknown"

                print(f"ID: {course.id}, Name: {course.name}, Code: {course.code}, Description: {course.description}, Professor: {professor_name}")

        
        input("Press Enter to return to go back...")
        from presentation.menu import ManageCoursesMenu
        self.terminal.navigateToMenu(ManageCoursesMenu(self.terminal))


class UpdateCourseMenu(Menu):

    def render(self):
        print("""
              ============================
               |     Update Course     |
              ============================
              """)
        
        print("Enter the course ID to update:")
        course_id: int = int(input())

        course = self.terminal.course_service.get_course_by_id(course_id)

        if course is None:
            print(f"No course found with ID {course_id}.")
            input("Press Enter to return to go back...")
            from presentation.menu import ManageCoursesMenu
            self.terminal.navigateToMenu(ManageCoursesMenu(self.terminal))
            return
        
        print(f"Current name: {course.name}")
        print("Enter new name (or press Enter to keep current):")
        new_name: str = input()

        print(f"Current code: {course.code}")
        print("Enter new code (or press Enter to keep current):")
        new_code: str = input() 

        print(f"\nCurrent professor: {course.professor_id}")

        # Show available professors to assign to the course
        professors = self.terminal.professor_service.get_all_professors()
        if professors:
            print("Available Professors:")
            for professor in professors:
                print(f"[{professor.id}] {professor.first_name} {professor.last_name} - {professor.department}")

            print("\nEnter new professor ID to assign to the course (or press Enter to keep current):")
            professor_id_input = input()
            new_professor_id = int(professor_id_input) if professor_id_input.strip() else course.professor_id

        self.terminal.course_service.update_course(course_id, new_name, new_code, new_professor_id)
        print(f"Course '{course.name}' updated successfully!")

        input("Press Enter to return to go back...")
        self.terminal.navigateToMenu(ManageCoursesMenu(self.terminal))


class DeleteCourseMenu(Menu):

    def render(self):
        print("""
             ===========================
                   Remove Course
             ===========================
                    """)
        
        print("Enter the course ID to delete:")
        course_id: int = int(input())

        course = self.terminal.course_service.get_course_by_id(course_id)
        if course is None:
            print(f"No course found with ID {course_id}.")
            input("Press Enter to return to go back...")
            from presentation.menu import ManageCoursesMenu
            self.terminal.navigateToMenu(ManageCoursesMenu(self.terminal))
            return
        
        self.terminal.course_service.delete_course(course_id)
        print(f"Course '{course.name}' deleted successfully!")

        input("Press Enter to return to go back...")
        self.terminal.navigateToMenu(ManageCoursesMenu(self.terminal))


class EnrollStudentMenu(Menu):

    def render(self):
        print("""
             ===========================
                  Enroll Student
             ===========================
                    """)
        
        courses = self.terminal.course_service.get_all_courses()
        if not courses:
            print("No courses available for enrollment.")
            input("Press Enter to return to go back...")
            from presentation.menu import ManageCoursesMenu
            self.terminal.navigateToMenu(ManageCoursesMenu(self.terminal))
            return
        
        print("Available Courses:")
        for course in courses:
            print(f"[{course.id}] {course.name} - {course.code}")

        print("\nEnter the course ID to enroll in:")
        course_id: int = int(input())

        # Show students to enroll in the course
        students = self.terminal.student_service.get_all_students()
        if not students:
            print("No students available for enrollment.")
            input("Press Enter to return to go back...")
            self.terminal.navigateToMenu(ManageCoursesMenu(self.terminal))
            return
        
        print("Available Students:")
        for student in students:
            print(f"[{student.id}] {student.first_name} {student.last_name} - {student.email}")

        print("\nEnter the student ID to enroll in the course:")
        student_id: int = int(input())

        student = self.terminal.student_service.get_student_by_id(student_id)
        if not student:
            print(f"No student found with ID {student_id}.")
            input("Press Enter to return to go back...")
            self.terminal.navigateToMenu(ManageCoursesMenu(self.terminal))
            return
        
        self.terminal.course_service.enroll_student(course_id, student_id)
        print(f"Student '{student.first_name} {student.last_name}' enrolled in course '{course.name}' successfully!")

        input("Press Enter to return to go back...")
        self.terminal.navigateToMenu(ManageCoursesMenu(self.terminal))


class DropStudentMenu(Menu):

    def render(self):
           print("""
             ===========================
                   Drop Student
             ===========================
                    """)
           
           print("Enter the course ID to drop from:")
           course_id: int = int(input())

           print("Enter the student ID to drop from the course:")
           student_id: int = int(input())

           student = self.terminal.student_service.get_student_by_id(student_id)
           if not student:
               print(f"No student found with ID {student_id}.")
               input("Press Enter to return to go back...")
               from presentation.menu import ManageCoursesMenu
               self.terminal.navigateToMenu(ManageCoursesMenu(self.terminal))
               return
           
           self.terminal.course_service.drop_student(course_id, student_id)
           print(f"Student '{student.first_name} {student.last_name}' dropped from course successfully!")

           input("Press Enter to return to go back...")
           self.terminal.navigateToMenu(ManageCoursesMenu(self.terminal))


class ShowEnrolledStudentsMenu(Menu):

    def render(self):
        print("""
             ===========================
               Enrolled Students
             ===========================
                    """)
        
        print("Enter the course ID to view enrolled students:")
        course_id: int = int(input())

        enrolled_students = self.terminal.course_service.get_enrolled_students(course_id)

        if not enrolled_students:
            print("No students enrolled in this course.")
        else:
            for student in enrolled_students:
                print(f"[{student.id}] {student.first_name} {student.last_name} - {student.email}")


        input("Press Enter to return to go back...")
        from presentation.menu import ManageCoursesMenu
        self.terminal.navigateToMenu(ManageCoursesMenu(self.terminal))


class ShowStudentCoursesMenu(Menu):

    def render(self):
        print("""
             ===========================
               Student's Courses
             ===========================
                    """)
        
        print("Enter the student ID to view their courses:")
        student_id: int = int(input())

        courses = self.terminal.course_service.get_courses_for_student(student_id)

        if not courses:
            print(f"No courses found for student with ID {student_id}.")
        else:
            for course in courses:
                print(f"[{course.id}] {course.name} - {course.description}")

        input("Press Enter to return to go back...")
        from presentation.menu import ManageCoursesMenu
        self.terminal.navigateToMenu(ManageCoursesMenu(self.terminal))


