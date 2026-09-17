from fastapi import APIRouter
from models.student import Student

router = APIRouter()


@router.post("/recommend")
def recommend_career(student: Student):

    if student.python_skill >= 8 and student.problem_solving >= 8:
        career = "Data Scientist"

    elif student.java_skill >= 8 and student.problem_solving >= 8:
        career = "Software Developer"

    elif student.sql_skill >= 8:
        career = "Data Analyst"

    else:
        career = "Software Developer"

    return {
        "recommended_career": career
    }