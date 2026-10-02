function Recommendation() {
  const recommendation = {
    career: "Software Developer",
    score: "92%",
    description:
      "Develops software applications, websites, and enterprise solutions using programming languages and modern technologies.",
    skills: ["Java", "Python", "SQL", "Problem Solving"],
  };

  return (
    <div className="page-container">
      <div className="card">
        <h1>🎯 Career Recommendation</h1>

        <div className="career-box">
          <h2>{recommendation.career}</h2>
          <h3>Match Score: {recommendation.score}</h3>

          <p>{recommendation.description}</p>

          <h4>Required Skills</h4>

          <div className="skill-container">
            {recommendation.skills.map((skill, index) => (
              <span key={index} className="skill-badge">
                {skill}
              </span>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}

export default Recommendation;