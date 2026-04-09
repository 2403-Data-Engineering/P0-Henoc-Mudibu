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
        return self.professor_dao.get_all_professors()

    def get_professor_by_id(self, professor_id: int) -> Professor | None:
        
        if professor_id is None or professor_id <= 0:
            print("Enter a valid Professor ID")
            return None
        
        return self.professor_dao.get_professor_by_id(professor_id)
    
    def update_professor(
            self, professor_id: int, 
            updated_first_name: str, 
            updated_last_name: str, 
            updated_department: str, 
            updated_email: str
            ) -> bool:

        professor = self.professor_dao.get_professor_by_id(professor_id)

        if professor is None:
            print(f"No professor found with ID {professor_id}. Update failed.")
            return False
        
        professor.first_name = updated_first_name or professor.first_name
        professor.last_name = updated_last_name or professor.last_name
        professor.department = updated_department or professor.department
        professor.email = updated_email or professor.email

        updated = self.professor_dao.update_professor(professor)
        if updated:
            print(f"Professor {professor.id} updated successfully.")
            return True
        else:
            print(f"Failed to update Professor {professor.id}.")
            return False

    
    def delete_professor(self, professor_id: int) -> bool:

        professor = self.professor_dao.get_professor_by_id(professor_id)

        if professor is None:
            print(f"No professor found with ID {professor_id}. Deletion failed.")
            return False
        
        deleted = self.professor_dao.delete_professor(professor_id)
        if deleted:
            print(f"Professor {professor.id} deleted successfully.")
            return True
        else:
            print(f"Failed to delete Professor {professor.id}.")
            return False