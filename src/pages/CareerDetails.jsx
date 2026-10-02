function CareerDetails() {
  return (
    <div className="page-container">
      <div className="card">
        <h1>💻 Software Developer</h1>

        <p>
          Software Developers design, build and maintain software
          applications for businesses and users.
        </p>

        <h3>Required Skills</h3>

        <div className="skill-container">
          <span className="skill-badge">Java</span>
          <span className="skill-badge">Python</span>
          <span className="skill-badge">SQL</span>
          <span className="skill-badge">Problem Solving</span>
          <span className="skill-badge">Communication</span>
        </div>

        <h3>Career Growth</h3>

        <p>
          Junior Developer → Software Developer → Senior Developer →
          Tech Lead → Software Architect
        </p>
      </div>
    </div>
  );
}

export default CareerDetails;