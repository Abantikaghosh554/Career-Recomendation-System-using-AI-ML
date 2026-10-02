from fastapi import APIRouter
from models.student import Student
from models.db_models import StudentDB
from database import SessionLocal

router = APIRouter()


@router.post("/recommend")
def recommend_career(student: Student):

    db = SessionLocal()

    try:
        new_student = StudentDB(
            name=student.name,
            education=student.education,
            cgpa=student.cgpa,

            java_skill=student.java_skill,
            python_skill=student.python_skill,
            sql_skill=student.sql_skill,
            web_development_skill=student.web_development_skill,
            data_analysis_skill=student.data_analysis_skill,
            machine_learning_skill=student.machine_learning_skill,
            database_management_skill=student.database_management_skill,
            cloud_computing_skill=student.cloud_computing_skill,
            networking_cybersecurity_skill=student.networking_cybersecurity_skill,

            ms_excel_skill=student.ms_excel_skill,
            power_bi_skill=student.power_bi_skill,
            tableau_skill=student.tableau_skill,
            statistics_skill=student.statistics_skill,
            data_visualization_skill=student.data_visualization_skill,

            problem_solving=student.problem_solving,
            analytical_thinking=student.analytical_thinking,
            logical_reasoning=student.logical_reasoning,
            communication=student.communication,

            interest=student.interest,
            experience=student.experience
        )

        db.add(new_student)
        db.commit()
        db.refresh(new_student)

        scores = {
            "Data Analyst": (
                student.sql_skill
                + student.data_analysis_skill
                + student.ms_excel_skill
                + student.power_bi_skill
                + student.tableau_skill
                + student.statistics_skill
                + student.data_visualization_skill
                + student.analytical_thinking
            ),

            "Data Scientist": (
                student.python_skill
                + student.data_analysis_skill
                + student.machine_learning_skill
                + student.statistics_skill
                + student.problem_solving
                + student.analytical_thinking
            ),

            "ML Engineer": (
                student.python_skill
                + student.machine_learning_skill
                + student.problem_solving
                + student.logical_reasoning
            ),

            "Software Developer": (
                student.java_skill
                + student.web_development_skill
                + student.problem_solving
                + student.logical_reasoning
            ),

            "Database Administrator": (
                student.sql_skill
                + student.database_management_skill
                + student.logical_reasoning
            ),

            "Cloud Engineer": (
                student.cloud_computing_skill
                + student.networking_cybersecurity_skill
                + student.problem_solving
            ),

            "Cybersecurity Analyst": (
                student.networking_cybersecurity_skill
                + student.logical_reasoning
                + student.problem_solving
            )
        }

        recommended_career = max(scores, key=scores.get)

        return {
            "student_id": new_student.id,
            "recommended_career": recommended_career,
            "career_scores": scores
        }

    finally:
        db.close()