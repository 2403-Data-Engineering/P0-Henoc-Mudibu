


from models.student import Student
from service.student_service import StudentService


student = Student("John", "Doe", "Computer Science", "john.doe@example.com", "Sophomore")
student_service = StudentService()
student_service.save(student)
#student_service.print_student_info(student)