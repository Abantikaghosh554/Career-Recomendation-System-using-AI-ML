from fastapi import APIRouter
from models.db_models import CareerDB
from database import SessionLocal

router = APIRouter()


@router.get("/careers")
def get_careers():

    db = SessionLocal()

    careers = db.query(CareerDB).all()

    result = []

    for career in careers:
        result.append({
            "id": career.id,
            "name": career.name,
            "description": career.description,
            "required_skills": career.required_skills
        })

    db.close()

    return result