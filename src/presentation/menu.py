from __future__ import annotations
from abc import abstractmethod
from typing import TYPE_CHECKING
from models.professor import Professor
from models.student import Student

if TYPE_CHECKING:
    from presentation.terminal import Terminal

class Menu:
    def __init__(self, terminal: Terminal):

        self.terminal: Terminal = terminal

    @abstractmethod
    def render(self) -> None:
        pass

class MainMenu(Menu):
    

    def render(self) -> None:

        # print("""
        #      ===========================
        #     Welcome to Revature Admin
        #     1) Create new student
        #     2) Create new professor
        #     3) Enroll student in class
        #     4) Show Student
        #     5) Show All Students
        #     Q) Exit
        #      ===========================
        #             """)
        print("""
             ===========================
            Welcome to Revature Admin
            
            1) Manage Students
            2) Manage Professors
            3) Manage Courses
            4) Reports
            Q) Exit
             ===========================
                    """)
        
        user_input: str = input().lower()


        # Switch statement for user input
        match user_input:
            case "1":
                self.terminal.navigateToMenu(ManageStudentsMenu(self.terminal))

            case "2":
                self.terminal.navigateToMenu(ManageProfessorsMenu(self.terminal))

            case "3":
                self.terminal.navigateToMenu(ManageCoursesMenu(self.terminal))

            case "4":
                self.terminal.navigateToMenu(ReportsMenu(self.terminal))

            case "q":
                self.terminal.exit()


class ManageStudentsMenu(Menu):

    def render(self) -> None:
        
        print("""
             ===========================
                 Manage Students
            1) Add new student
            2) Show student
            3) Show all students
            4) Update student
            5) Remove student
            B) Back to main menu
             ===========================
                    """)
        
        user_input: str = input().lower()

        match user_input:
            case "1":
                self.terminal.navigateToMenu(NewStudentMenu(self.terminal))

            case "2":
                self.terminal.navigateToMenu(ShowStudentMenu(self.terminal))

            case "3":
                self.terminal.navigateToMenu(ShowAllStudentsMenu(self.terminal))

            case "4":
                self.terminal.navigateToMenu(UpdateStudentMenu(self.terminal))

            case "5":
                self.terminal.navigateToMenu(RemoveStudentMenu(self.terminal))

            case "b":
                self.terminal.navigateToMenu(MainMenu(self.terminal))


class ManageProfessorsMenu(Menu):

    def render(self) -> None:

        print("""
             ===========================
                Manage Professors
            1) Add new professor
            2) Show all professors
            3) Update professor
            4) Remove professor
            B) Back to main menu
             ===========================
                    """)
        user_input: str = input().lower()

        match user_input:
            case "1":
                self.terminal.navigateToMenu(NewProfessorMenu(self.terminal))
            
            case "2":
                self.terminal.navigateToMenu(ShowAllProfessorsMenu(self.terminal))

            case "3":
                self.terminal.navigateToMenu(UpdateProfessorMenu(self.terminal))

            case "4":
                self.terminal.navigateToMenu(DeleteProfessorMenu(self.terminal))

            case "b":
                self.terminal.navigateToMenu(MainMenu(self.terminal))


class ManageCoursesMenu(Menu):


    def render(self) -> None:

        from presentation.course_menu import (
            NewCourseMenu,
            ShowAllCoursesMenu,
            UpdateCourseMenu,
            DeleteCourseMenu,
            EnrollStudentMenu,
            DropStudentMenu,
            ShowEnrolledStudentsMenu,
            ShowStudentCoursesMenu
        )

        print("""
             ===========================
                 Manage Courses
            1) Add new course
            2) Show all courses
            3) Update course
            4) Remove course
            5) Enroll student in course
            6) Drop student from course
            7) Show all students in course
            8) Show all courses for student
            B) Back to main menu
             ===========================
                    """)
    
        user_input: str = input().lower()

        match user_input:
            case "1":
                self.terminal.navigateToMenu(NewCourseMenu(self.terminal))

            case "2":
                self.terminal.navigateToMenu(ShowAllCoursesMenu(self.terminal))

            case "3":
                self.terminal.navigateToMenu(UpdateCourseMenu(self.terminal))

            case "4":
                self.terminal.navigateToMenu(DeleteCourseMenu(self.terminal))

            case "5":
                self.terminal.navigateToMenu(EnrollStudentMenu(self.terminal))

            case "6":
                self.terminal.navigateToMenu(DropStudentMenu(self.terminal))

            case "7":
                self.terminal.navigateToMenu(ShowEnrolledStudentsMenu(self.terminal))

            case "8":
                self.terminal.navigateToMenu(ShowStudentCoursesMenu(self.terminal))

            case "b":
                self.terminal.navigateToMenu(MainMenu(self.terminal))


class ReportsMenu(Menu):

    def render(self) -> None:

        print("""
             ===========================
                    Reports Menu Coming Soon
             ===========================
                    """)


class NewStudentMenu(Menu):

    def render(self):
        print("""Create New Student""")
        print()
        print("Enter the student's id:")
        id: int = int(input())
        print("Enter first name:")
        first_name: str = input()
        print("Enter last name:")
        last_name: str = input()
        print("Enter email:")
        email: str = input()
        print("Enter year: ")
        year: str = input()
        print("Enter major: ")
        major: str = input()

        new_student = Student(id, first_name, last_name, major, email, year)
        self.terminal.student_service.save(new_student)

        input("Press Enter to return to go back ...")
        self.terminal.navigateToMenu(ManageStudentsMenu(self.terminal))


class ShowStudentMenu(Menu):

    def render(self):
        print("""
             ===========================
                    Show Student
             ===========================
                    """)
        print()
        print("Enter student's ID:")
        id: int = int(input())

        student = self.terminal.student_service.get_student_by_id(id)

        if not student:
            print(f"No student found with ID '{id}'.")
        else:
            print(f"Student found with ID '{id}':")
            print(f"Name: {student.first_name} {student.last_name}")
            print(f"Email: {student.email}")
            print(f"Year: {student.year}")
            print(f"Major: {student.major}")

        input("Press Enter to return to go back...")
        self.terminal.navigateToMenu(ManageStudentsMenu(self.terminal))


class ShowAllStudentsMenu(Menu):

    def render(self):
        print("""All Registered Students""")
        students = self.terminal.student_service.get_all_students()

        if not students:
            print("No students found.")
        else:
            for student in students:
                print(f"[{student.id}] {student.first_name} {student.last_name} - {student.email} - {student.year} - {student.major}")

        
        input("Press Enter to return to go back...")
        self.terminal.navigateToMenu(ManageStudentsMenu(self.terminal))


class UpdateStudentMenu(Menu):
    def render(self):
        print("""
             ===========================
                  Update Student
             ===========================
                    """)

        print("Enter student ID:")
        student_id: int = int(input())

        student = self.terminal.student_service.get_student_by_id(student_id)

        if student is None:
            print(f"No student found with ID '{student_id}'.")
            input("Press Enter to return to go back...")
            self.terminal.navigateToMenu(ManageStudentsMenu(self.terminal))
            return
    

        print(f"\nCurrent Last Name: {student.last_name}")
        print("Enter new last name (or press Enter to keep current):")
        updated_last_name: str = input()

        print(f"\nCurrent major: {student.major}")
        print("Enter new major (or press Enter to keep current):")
        updated_major: str = input()

        print(f"\nCurrent email: {student.email}")
        print("Enter new email (or press Enter to keep current):")
        updated_email: str = input()

        print(f"\nCurrent year: {student.year}")
        print("Enter new year (or press Enter to keep current):")
        updated_year: str = input()

        self.terminal.student_service.update_student(student_id, updated_last_name, updated_major, updated_email, updated_year)

        input("\nPress Enter to return to go back...")
        self.terminal.navigateToMenu(ManageStudentsMenu(self.terminal))


class DeleteStudentMenu(Menu):
    def render(self):
        print("""
             ===========================
                  Remove Student
             ===========================
                    """)
        print("Enter student ID:")
        student_id: int = int(input())

        student = self.terminal.student_service.get_student_by_id(student_id)

        if student is None:
            print(f"No student found with ID '{student_id}'.")
            input("Press Enter to return to go back...")
            self.terminal.navigateToMenu(ManageStudentsMenu(self.terminal))
            return

        self.terminal.student_service.delete_student(student_id)
        print(f"Student with ID '{student_id}' has been removed.")

        input("\nPress Enter to return to go back...")
        self.terminal.navigateToMenu(ManageStudentsMenu(self.terminal))


# To be implemented

class NewProfessorMenu(Menu):
    def render(self):
        print("""
             ===========================
                 Add New Professor
             ===========================
                    """)

        print("Enter professor ID:")
        id: int = int(input())
        print("Enter first name:")
        first_name: str = input()
        print("Enter last name:")
        last_name: str = input()
        print("Enter email:")
        email: str = input()
        print("Enter department:")
        department: str = input()

        new_professor = Professor(id, first_name, last_name, email, department)
        operation = self.terminal.professor_service.save(new_professor)

        if operation:
            print(f"Professor {first_name} {last_name} saved successfully.")

        input("Press Enter to return to go back ...")
        self.terminal.navigateToMenu(ManageProfessorsMenu(self.terminal))


class UpdateProfessorMenu(Menu):
    def render(self):
        print("""
             ===========================
                 Update Professor
             ===========================
                    """)

        print("Enter professor ID:")
        professor_id: int = int(input())

        professor = self.terminal.professor_service.get_professor_by_id(professor_id)

        if professor is None:
            print(f"No professor found with ID '{professor_id}'.")
            input("Press Enter to return to go back...")
            self.terminal.navigateToMenu(ManageProfessorsMenu(self.terminal))
            return
        
        print(f"\nCurrent Last Name: {professor.last_name}")
        print("Enter new last name (or press Enter to keep current):")
        updated_last_name: str = input()

        print(f"\nCurrent department: {professor.department}")
        print("Enter new department (or press Enter to keep current):")
        updated_department: str = input()   

        self.terminal.professor_service.update_professor(professor_id, updated_last_name, updated_department)

        input("\nPress Enter to return to go back...")
        self.terminal.navigateToMenu(ManageProfessorsMenu(self.terminal))


class DeleteProfessorMenu(Menu):
    def render(self):
        print("""
             ===========================
                 Remove Professor
             ===========================
                    """)

        print("Enter professor ID:")
        professor_id: int = int(input())

        professor = self.terminal.professor_service.get_professor_by_id(professor_id)

        if professor is None:
            print(f"No professor found with ID '{professor_id}'.")
            input("Press Enter to return to go back...")
            self.terminal.navigateToMenu(ManageProfessorsMenu(self.terminal))
            return
        
        self.terminal.professor_service.delete_professor(professor_id)
        print(f"Professor with ID '{professor_id}' has been removed.")

        input("\nPress Enter to return to go back...")
        self.terminal.navigateToMenu(ManageProfessorsMenu(self.terminal))

# class NewCourseMenu(Menu):
#     def render(self):
#         print("\n[Course Creation Coming Soon]")
#         input("Press Enter to return...")
#         self.terminal.navigate(MainMenu(self.terminal))

# class EnrollmentMenu(Menu):
#     def render(self):
#         print("\n[Enrollment Feature Coming Soon]")
#         input("Press Enter to return...")
#         self.terminal.navigateToMenu(MainMenu(self.terminal))

            