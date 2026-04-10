from dataclasses import dataclass
from datetime import datetime


@dataclass
class Enrollment:
    enrollment_id: int | None
    student_id: int
    course_id: int
    enrollment_date: datetime | None = None
