from __future__ import annotations
from abc import abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from presentation.terminal import Terminal

class Menu:
    def __int__(self, terminal: Terminal):

        self.terminal: Terminal = terminal

    @abstractmethod
    def render(self) -> None:
        pass

class MainMenu(Menu):
    

    def render(self) -> None:

        print("""
             ===========================
            Welcome to Revature Admin
            1) Create new student
            2) Create new professor
            3) Enroll student in class
            4) Show Student
            5) Show All Students
            Q) Exit
             ===========================
                    """)
        
        user_input: str = input().lower()


        # Switch statement for user input
        match user_input:
            case "1":
                self.terminal.navigateToMenu(NewStudentMenu(self.terminal))

            case "2":
                self.terminal.navigateToMenu(NewProfessorMenu(self.terminal))

            case "3":
                self.terminal.navigateToMenu(EnrollStudentMenu(self.terminal))

            case "4":
                self.terminal.navigateToMenu(ShowStudentMenu(self.terminal))

            case "5":
                self.terminal.navigateToMenu(ShowAllStudentsMenu(self.terminal))

            case "q":
                self.terminal.exit()

class NewStudentMenu(Menu):

    def render(self):
        print("""Create New Student""")
        print()
        print("Enter the student's first name:")
        first_name: str = input()
        print("Enter the student's last name:")
        last_name: str = input()
        print("Enter the student's email:")
        email: str = input()
        print("Enter the school year:")
        year: str = input()
        print("Enter the student's major:")
        major: str = input()

class ShowAllStudentsMenu(Menu):

    def render(self):
        print("""All Registered Students""")
        students = self.terminal.student_service.get_all_students()

        if not students:
            print("No students found.")
        else:
            for student in students:
                print(f"{student.first_name} {student.last_name} - {student.email} - {student.year} - {student.major}")

        
        input("Press Enter to return to the main menu...")
        self.terminal.navigateToMenu(MainMenu(self.terminal))

class ShowStudentMenu(Menu):

    def render(self):
        print("""Show Student""")
        print("Enter the student's first name:")
        first_name: str = input()

        student = self.terminal.student_service.get_student_by_first_name(first_name)

        if not student:
            print(f"No student found with the first name '{first_name}'.")
        else:
            print(f"Name: {student.first_name} {student.last_name}")
            print(f"Email: {student.email}")
            print(f"Year: {student.year}")
            print(f"Major: {student.major}")

        input("Press Enter to return to the main menu...")
        self.terminal.navigateToMenu(MainMenu(self.terminal))


# To be implemented

class NewProfessorMenu(Menu):
    def render(self):
        print("\n[Professor Feature Coming Soon]")
        input("Press Enter to return...")
        self.terminal.navigate(MainMenu(self.terminal))

class NewCourseMenu(Menu):
    def render(self):
        print("\n[Course Creation Coming Soon]")
        input("Press Enter to return...")
        self.terminal.navigate(MainMenu(self.terminal))

class EnrollmentMenu(Menu):
    def render(self):
        print("\n[Enrollment Feature Coming Soon]")
        input("Press Enter to return...")
        self.terminal.navigate(MainMenu(self.terminal))

            