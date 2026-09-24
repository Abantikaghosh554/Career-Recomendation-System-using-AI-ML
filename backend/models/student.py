from pydantic import BaseModel


class Student(BaseModel):
    name: str
    education: str
    specialization: str
    skills: str
    certifications: str
    cgpa: float
    problem_solving: int
    communication: int