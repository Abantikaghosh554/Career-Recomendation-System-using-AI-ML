from sqlalchemy import Column, Integer, Float, String
from database import Base

class StudentDB(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    education = Column(String(100))
    cgpa = Column(Float)

    java_skill = Column(Integer)
    python_skill = Column(Integer)
    sql_skill = Column(Integer)
    web_development_skill = Column(Integer)
    data_analysis_skill = Column(Integer)
    machine_learning_skill = Column(Integer)
    database_management_skill = Column(Integer)
    cloud_computing_skill = Column(Integer)
    networking_cybersecurity_skill = Column(Integer)
    ms_excel_skill = Column(Integer)
    power_bi_skill = Column(Integer)
    tableau_skill = Column(Integer)
    statistics_skill = Column(Integer)
    data_visualization_skill = Column(Integer)

    problem_solving = Column(Integer)
    analytical_thinking = Column(Integer)
    logical_reasoning = Column(Integer)
    communication = Column(Integer)

    interest = Column(String(100))
    experience = Column(String(100))
    
"""class StudentDB(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    education = Column(String(100))
    cgpa = Column(Float)
    java_skill = Column(Integer)
    python_skill = Column(Integer)
    sql_skill = Column(Integer)
    problem_solving = Column(Integer)
    communication = Column(Integer)
    interest = Column(String(100))
    experience = Column(String(100))"""


class CareerDB(Base):
    __tablename__ = "careers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    description = Column(String(500))
    required_skills = Column(String(500))