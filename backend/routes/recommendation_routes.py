from fastapi import APIRouter
from models.student import Student

from ml.predict import predict_career


router = APIRouter()


@router.post("/recommend")
def recommend_career(student: Student):

    student_data = {
        "Education": student.education,
        "Specialization": student.specialization,
        "Skills": student.skills,
        "Certifications": student.certifications,
        "CGPA": student.cgpa,
        "Problem Solving": student.problem_solving,
        "Communication": student.communication
    }

    career = predict_career(student_data)

    return {
        "student": student.name,
        "recommended_career": career
    }