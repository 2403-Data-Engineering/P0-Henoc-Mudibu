from __future__ import annotations
from typing import TYPE_CHECKING

from src.service.student_service import StudentService

# To prevent circular imports
if TYPE_CHECKING:
    from presentation.menu import Menu


class Terminal:
    def __init__(self, student_service: StudentService):
        from presentation.menu import MainMenu
        
        #Start with the Main Menu
        self.current_menu = MainMenu(self)

        self.running = True

        self.student_service = student_service


    def navigateToMenu(self, menu: Menu):

        self.current_menu = menu

    def exit(self):

        self.running = False
        print("Exiting the application. Goodbye!")