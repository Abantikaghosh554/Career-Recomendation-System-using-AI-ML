from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import engine, Base
from models import db_models

from routes.student_routes import router as student_router
from routes.career_routes import router as career_router
from routes.recommendation_routes import router as recommendation_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(student_router)
app.include_router(career_router)
app.include_router(recommendation_router)


@app.get("/")
def home():
    return {"message": "Career Recommendation System Backend"}