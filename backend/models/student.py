from pydantic import BaseModel


class Student(BaseModel):
    name: str
    education: str
    cgpa: float

    java_skill: int
    python_skill: int
    sql_skill: int
    web_development_skill: int
    data_analysis_skill: int
    machine_learning_skill: int
    database_management_skill: int
    cloud_computing_skill: int
    networking_cybersecurity_skill: int
    ms_excel_skill: int
    power_bi_skill: int
    tableau_skill: int
    statistics_skill: int
    data_visualization_skill: int

    problem_solving: int
    analytical_thinking: int
    logical_reasoning: int
    communication: int

    interest: str
    experience: str