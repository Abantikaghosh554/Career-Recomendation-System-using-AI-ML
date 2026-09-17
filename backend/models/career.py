from pydantic import BaseModel


class Career(BaseModel):
    name: str
    description: str
    required_skills: str