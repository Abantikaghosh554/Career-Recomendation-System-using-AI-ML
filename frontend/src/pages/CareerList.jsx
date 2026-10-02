function CareerList() {
  const careers = [
    "Software Developer",
    "Data Analyst",
    "Python Developer",
    "Java Developer",
    "AI Engineer",
    "Database Administrator",
  ];

  return (
    <div className="page-container">
      <h1>💼 Career Opportunities</h1>

      <div className="career-grid">
        {careers.map((career, index) => (
          <div key={index} className="career-card">
            <h3>{career}</h3>

            <button>View Details</button>
          </div>
        ))}
      </div>
    </div>
  );
}

export default CareerList;