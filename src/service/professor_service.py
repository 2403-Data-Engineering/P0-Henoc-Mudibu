from dao.professor_dao import ProfessorDAO
from models.professor import Professor


class ProfessorService:

    def __init__(self):
        self.professor_dao = ProfessorDAO()

    def save(self, first_name: str, last_name: str, email: str, department: str) -> Professor | None:

        if not all([first_name, last_name, email, department]):
            print("All professor fields must be provided. Save failed.")
            return None
        
        professor = Professor(
            id=None,
            first_name=first_name.strip(),
            last_name=last_name.strip(),
            email=email.strip(),
            department=department.strip() if department else None
        )

        return self.professor_dao.save(professor)
    

    def get_all_professors(self) -> list[Professor]:
        return self.professors_list

    def get_professor_by_id(self, professor_id: int) -> Professor | None:
        for professor in self.professors_list:
            if professor.id == professor_id:
                return professor
        return None
    
    def update_professor(self, professor_id: int, updated_last_name: str, updated_department: str) -> bool:

        professor = self.get_professor_by_id(professor_id)

        if professor is None:
            print(f"No professor found with ID {professor_id}. Update failed.")
            return False
        
        professor.last_name = updated_last_name or professor.last_name
        professor.department = updated_department or professor.department
        print(f"Professor {professor.id} updated successfully.")
        return True
    
    def delete_professor(self, professor_id: int) -> bool:

        professor = self.get_professor_by_id(professor_id)

        if professor is None:
            print(f"No professor found with ID {professor_id}. Deletion failed.")
            return False
        
        self.professors_list.remove(professor)
        print(f"Professor {professor.id} deleted successfully.")
        return True