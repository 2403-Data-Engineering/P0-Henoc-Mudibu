


from dao.student_dao import StudentDAO
from models.student import Student


class StudentService:

    def __init__(self):
        # self.students_list: list[Student] = []
        self.student_dao = StudentDAO()

    def save(self, student: Student) -> Student | None:
        # self.students_list.append(student)
        # print(f"Student {student.first_name}-{student.last_name} saved successfully")

        fields = [student.first_name, student.last_name, student.major, student.email, student.year]

        if not all(fields):
            print("All student fields must be provided. Save failed.")
            return None
        
        saved_student = self.student_dao.save(student)

        if saved_student:
            print(f"\n[SUCCESS]Student {saved_student.first_name} {saved_student.last_name} saved successfully with ID {saved_student.id}.")
        else:
            print("\n[ERROR] Failed to save student.")

        return 

    # def print_student_info(self, student: Student):
    #     print(f"Name: {student.first_name}-{student.last_name}")
    #     print(f"Major: {student.major}")
    #     print(f"Email: {student.email}")
    #     print(f"Year: {student.year}")

    def get_all_students(self) -> list[Student]:
        # formatted_Students = []
        # for student in self.students_list:
        #     line = f"{student.first_name}-{student.last_name} - {student.major} - {student.email} - {student.year}"
        #     formatted_Students.append(line)
        return self.student_dao.get_all_students()


    # def get_student_by_first_name(self, first_name: str) -> Student | None:
    #     for student in self.students_list:
    #         if student.first_name == first_name:
    #             return student
    #     return None

    def get_student_by_id(self, id: int) -> Student | None:
        
        if id is None:
            print("Student ID is required to retrieve student.")
            return None
        
        if id <= 0:
            print("Enter a valid Student ID")
            return None
        
        student = self.student_dao.get_student_by_id(id)

        if student:
            return student
        else:
            print(f"\n[ERROR] No student found with ID {id}.")

        return None


    
    def update_student(
            self, id: int, 
            first_name: str | None, 
            last_name: str | None, 
            major: str | None, 
            email: str | None, 
            year: int | None
        ) -> bool:

        
        if id is None or id <= 0:
            print("Enter a valid Student ID")
            return False
        
        student = self.student_dao.get_student_by_id(id)
        if not student:
            print(f"No student found with ID {id}. Update failed.")
            return False
        
        updated_student = Student(
            id=id,
            first_name=first_name or student.first_name,
            last_name=last_name or student.last_name,
            major=major or student.major,
            email=email or student.email,
            year=year or student.year
        )

        return self.student_dao.update_student(updated_student)



    def delete_student(self, id: int) -> bool:
        if id is None or id <= 0:
            print("Enter a valid Student ID")
            return False
        
        student = self.student_dao.get_student_by_id(id)
        if not student:
            print(f"No student found with ID {id}. Deletion failed.")
            return False
        
        return self.student_dao.delete_student(id)