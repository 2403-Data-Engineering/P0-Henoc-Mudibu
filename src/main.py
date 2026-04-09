from presentation.terminal import Terminal
from service.student_service import StudentService


#student = Student("John", "Doe", "Computer Science", "john.doe@example.com", "Sophomore")
#student_service = StudentService()
#student_service.save(student)
#student_service.print_student_info(student)

def main():

    #student_Service = StudentService()

    terminal = Terminal()

    while terminal.running:
        terminal.current_menu.render()

if __name__ == "__main__":
    main()