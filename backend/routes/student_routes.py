from fastapi import APIRouter
from models.student import Student
from models.db_models import StudentDB
from database import SessionLocal

router = APIRouter()


@router.post("/students")
def create_student(student: Student):

    db = SessionLocal()

    new_student = StudentDB(
        name=student.name,
        education=student.education,
        cgpa=student.cgpa,
        java_skill=student.java_skill,
        python_skill=student.python_skill,
        sql_skill=student.sql_skill,
        problem_solving=student.problem_solving,
        communication=student.communication,
        interest=student.interest,
        experience=student.experience
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    db.close()

    return {
        "message": "Student saved successfully",
        "student_id": new_student.id
    }