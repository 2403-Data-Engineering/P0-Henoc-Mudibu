from __future__ import annotations
from typing import TYPE_CHECKING

from service.course_service import CourseService
from service.professor_service import ProfessorService
from service.student_service import StudentService

# To prevent circular imports
if TYPE_CHECKING:
    from presentation.menu import Menu


class Terminal:
    def __init__(self):
        from presentation.menu import MainMenu

         # Each service is instantiated once and shared across all menus via self.terminal.
        # This ensures all menus read and write to the same data.
        self.student_service = StudentService()
        self.professor_service = ProfessorService()
        self.courses_service = CourseService()
        
        #Start with the Main Menu
        self.current_menu = MainMenu(self)

        self.running = True


    def navigateToMenu(self, menu: Menu):

        self.current_menu = menu

    def exit(self):

        self.running = False
        print("Exiting the application. Goodbye!")