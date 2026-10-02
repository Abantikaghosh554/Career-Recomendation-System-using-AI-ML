from fastapi import APIRouter
from models.db_models import CareerDB
from database import SessionLocal
from models.career import Career
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

@router.get("/careers/{career_id}")
def get_career(career_id: int):

    db = SessionLocal()

    career = db.query(CareerDB).filter(
        CareerDB.id == career_id
    ).first()

    db.close()

    if career is None:
        return {
            "message": "Career not found"
        }

    return {
        "id": career.id,
        "name": career.name,
        "description": career.description,
        "required_skills": career.required_skills
    }

@router.post("/careers")
def create_career(career: Career):

    db = SessionLocal()

    new_career = CareerDB(
        name=career.name,
        description=career.description,
        required_skills=career.required_skills
    )

    db.add(new_career)
    db.commit()
    db.refresh(new_career)
    db.close()

    return {
        "message": "Career added successfully",
        "career_id": new_career.id
    }