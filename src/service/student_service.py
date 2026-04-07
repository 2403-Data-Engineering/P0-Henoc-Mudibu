


from models.student import Student


class StudentService:

    def __init__(self):
        self.students_list: list[Student] = []

    def save(self, student: Student):
        self.students_list.append(student)
        print(f"Student {student.first_name}-{student.last_name} saved successfully")

    # def print_student_info(self, student: Student):
    #     print(f"Name: {student.first_name}-{student.last_name}")
    #     print(f"Major: {student.major}")
    #     print(f"Email: {student.email}")
    #     print(f"Year: {student.year}")

    def get_all_students(self) -> list[str]:
        # formatted_Students = []
        # for student in self.students_list:
        #     line = f"{student.first_name}-{student.last_name} - {student.major} - {student.email} - {student.year}"
        #     formatted_Students.append(line)
        return self.students_list


    # def get_student_by_first_name(self, first_name: str) -> Student | None:
    #     for student in self.students_list:
    #         if student.first_name == first_name:
    #             return student
    #     return None

    def get_student_by_id(self, id: int) -> Student | None:
        for student in self.students_list:
            if student.id == id:
                return student
        return None
    
    def update_student(self, id: int, updated_student: Student) -> bool:
        for index, student in enumerate(self.students_list):
            if student.id == id:
                self.students_list[index] = updated_student
                return True
            
        print(f"Student with id {id} not found.")
        return False

    def delete_student(self, id: int) -> bool:
        for index, student in enumerate(self.students_list):
            if student.id == id:
                del self.students_list[index]
                return True
            
        print(f"Student with id {id} not found.")
        return False