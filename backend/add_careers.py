from database import SessionLocal
from models.db_models import CareerDB


careers = [
    {
        "name": "ML Engineer",
        "description": "Builds and deploys machine learning models and AI systems.",
        "required_skills": "Python, Machine Learning, SQL"
    },
    {
        "name": "Data Scientist",
        "description": "Analyzes data and develops machine learning models to solve problems.",
        "required_skills": "Python, Machine Learning, Data Analysis"
    },
    {
        "name": "Data Analyst",
        "description": "Analyzes data and creates reports to support business decisions.",
        "required_skills": "Python, SQL, Data Analysis"
    },
    {
        "name": "Business Analyst",
        "description": "Analyzes business requirements and data to support organizational decisions.",
        "required_skills": "Data Analysis, Communication, MS Office"
    },
    {
        "name": "Financial Analyst",
        "description": "Analyzes financial data and prepares financial reports and forecasts.",
        "required_skills": "Financial Analysis, Accounting, Excel"
    },
    {
        "name": "Junior Accountant",
        "description": "Maintains financial records and assists with accounting activities.",
        "required_skills": "Accounting, Financial Analysis, MS Office"
    },
    {
        "name": "Marketing Executive",
        "description": "Plans and executes marketing activities to promote products and services.",
        "required_skills": "Marketing, Communication, MS Office"
    },
    {
        "name": "Sales Assistant",
        "description": "Assists customers and supports sales activities and operations.",
        "required_skills": "Communication, MS Office"
    },
    {
        "name": "School Counselor",
        "description": "Provides guidance and counseling support to students.",
        "required_skills": "Counseling, Communication"
    },
    {
        "name": "Professor",
        "description": "Teaches students and conducts academic and research activities.",
        "required_skills": "Communication, Research"
    },
    {
        "name": "Research Scientist",
        "description": "Conducts research and develops solutions using scientific and technical methods.",
        "required_skills": "Machine Learning, Data Analysis, Python, Research"
    },
    {
        "name": "Clerk",
        "description": "Performs administrative, record-keeping, and office-related tasks.",
        "required_skills": "MS Office, Communication"
    },
    {
        "name": "Data Entry Operator",
        "description": "Enters, updates, and maintains information in computer systems.",
        "required_skills": "MS Office, Communication"
    }
]


db = SessionLocal()

for career in careers:

    existing = db.query(CareerDB).filter(
        CareerDB.name == career["name"]
    ).first()

    if existing:
        print(f"Already exists: {career['name']}")
        continue

    new_career = CareerDB(
        name=career["name"],
        description=career["description"],
        required_skills=career["required_skills"]
    )

    db.add(new_career)

db.commit()
db.close()

print("\nAll careers added successfully!")