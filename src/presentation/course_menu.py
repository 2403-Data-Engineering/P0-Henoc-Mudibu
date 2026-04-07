from __future__ import annotations
from typing import TYPE_CHECKING
from models.course import Course
from models.student import Student


if TYPE_CHECKING:
    from presentation.terminal import Terminal

from presentation.menu import ManageCoursesMenu, Menu

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
