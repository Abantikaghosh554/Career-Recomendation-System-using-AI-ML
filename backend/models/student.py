from pydantic import BaseModel


class Student(BaseModel):
    name: str
    education: str
    cgpa: float
    java_skill: int
    python_skill: int
    sql_skill: int
    problem_solving: int
    communication: int
    interest: str
    experience: str