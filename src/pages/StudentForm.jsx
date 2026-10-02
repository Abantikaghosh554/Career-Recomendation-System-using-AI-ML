import { useState } from "react";
import API from "../services/api";
import "./StudentForm.css";

const technicalSkillOptions = [
  "Java",
  "Python",
  "C",
  "C++",
  "JavaScript",
  "HTML & CSS",
  "React",
  "Angular",
  "SQL",
  "Data Analysis",
  "Machine Learning",
  "MS Excel",
  "Power BI",
  "Tableau",
  "Statistics",
  "Data Visualization",
  "Deep Learning",
  "Artificial Intelligence",
  "Database Management",
  "Cloud Computing",
  "Networking",
  "Cybersecurity",
  "DevOps",
  "Git & GitHub",
  "Data Structures & Algorithms",
];

const generalSkillOptions = [
  "Problem Solving",
  "Analytical Thinking",
  "Logical Reasoning",
  "Communication",
  "Teamwork",
  "Leadership",
  "Time Management",
  "Adaptability",
  "Creativity",
  "Decision Making",
];

function StudentForm() {
  const [formData, setFormData] = useState({
    name: "",
    education: "",
    cgpa: "",
    interest: "",
    experience: "",
  });

  const [technicalSkills, setTechnicalSkills] = useState([]);
  const [generalSkills, setGeneralSkills] = useState([]);

  const [selectedTechnicalSkill, setSelectedTechnicalSkill] = useState("");
  const [technicalRating, setTechnicalRating] = useState("");

  const [selectedGeneralSkill, setSelectedGeneralSkill] = useState("");
  const [generalRating, setGeneralRating] = useState("");

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const addTechnicalSkill = () => {
    if (!selectedTechnicalSkill || !technicalRating) {
      alert("Please select a technical skill and provide a rating.");
      return;
    }

    if (technicalSkills.length >= 7) {
      alert("You can add a maximum of 7 technical skills.");
      return;
    }

    if (
      technicalSkills.some(
        (skill) => skill.name === selectedTechnicalSkill
      )
    ) {
      alert("This technical skill has already been added.");
      return;
    }

    setTechnicalSkills([
      ...technicalSkills,
      {
        name: selectedTechnicalSkill,
        rating: Number(technicalRating),
      },
    ]);

    setSelectedTechnicalSkill("");
    setTechnicalRating("");
  };

  const addGeneralSkill = () => {
    if (!selectedGeneralSkill || !generalRating) {
      alert("Please select a general skill and provide a rating.");
      return;
    }

    if (generalSkills.length >= 5) {
      alert("You can add a maximum of 5 general skills.");
      return;
    }

    if (
      generalSkills.some(
        (skill) => skill.name === selectedGeneralSkill
      )
    ) {
      alert("This general skill has already been added.");
      return;
    }

    setGeneralSkills([
      ...generalSkills,
      {
        name: selectedGeneralSkill,
        rating: Number(generalRating),
      },
    ]);

    setSelectedGeneralSkill("");
    setGeneralRating("");
  };

  const removeTechnicalSkill = (skillName) => {
    setTechnicalSkills(
      technicalSkills.filter((skill) => skill.name !== skillName)
    );
  };

  const removeGeneralSkill = (skillName) => {
    setGeneralSkills(
      generalSkills.filter((skill) => skill.name !== skillName)
    );
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (technicalSkills.length < 3) {
      alert("Please add at least 3 technical skills.");
      return;
    }

    if (generalSkills.length < 2) {
      alert("Please add at least 2 general skills.");
      return;
    }

    const technicalData = {
      java_skill: 0,
      python_skill: 0,
      sql_skill: 0,
      web_development_skill: 0,
      data_analysis_skill: 0,
      machine_learning_skill: 0,
      database_management_skill: 0,
      cloud_computing_skill: 0,
      networking_cybersecurity_skill: 0,
      ms_excel_skill: 0,
      power_bi_skill: 0,
      tableau_skill: 0,
      statistics_skill: 0,
      data_visualization_skill: 0,

    };

    technicalSkills.forEach((skill) => {
      const rating = skill.rating;

      if (skill.name === "Java") {
        technicalData.java_skill = rating;
      }

      if (skill.name === "Python") {
        technicalData.python_skill = rating;
      }

      if (skill.name === "SQL") {
        technicalData.sql_skill = rating;
      }

      if (
        skill.name === "HTML & CSS" ||
        skill.name === "JavaScript" ||
        skill.name === "React" ||
        skill.name === "Angular" ||
        skill.name === "Web Development"
      ) {
        technicalData.web_development_skill = Math.max(
          technicalData.web_development_skill,
          rating
        );
      }

      if (skill.name === "Data Analysis") {
        technicalData.data_analysis_skill = rating;
      }
      if (skill.name === "MS Excel") {
        technicalData.ms_excel_skill = rating;
      }

      if (skill.name === "Power BI") {
        technicalData.power_bi_skill = rating;
      }

      if (skill.name === "Tableau") {
        technicalData.tableau_skill = rating;
      }

      if (skill.name === "Statistics") {
        technicalData.statistics_skill = rating;
      }

      if (skill.name === "Data Visualization") {
        technicalData.data_visualization_skill = rating;
      }

      if (
        skill.name === "Machine Learning" ||
        skill.name === "Deep Learning" ||
        skill.name === "Artificial Intelligence"
      ) {
        technicalData.machine_learning_skill = Math.max(
          technicalData.machine_learning_skill,
          rating
        );
      }

      if (skill.name === "Database Management") {
        technicalData.database_management_skill = rating;
      }

      if (skill.name === "Cloud Computing") {
        technicalData.cloud_computing_skill = rating;
      }

      if (
        skill.name === "Networking" ||
        skill.name === "Cybersecurity"
      ) {
        technicalData.networking_cybersecurity_skill = Math.max(
          technicalData.networking_cybersecurity_skill,
          rating
        );
      }
    });

    const generalData = {
      problem_solving: 0,
      analytical_thinking: 0,
      logical_reasoning: 0,
      communication: 0,
    };

    generalSkills.forEach((skill) => {
      if (skill.name === "Problem Solving") {
        generalData.problem_solving = skill.rating;
      }

      if (skill.name === "Analytical Thinking") {
        generalData.analytical_thinking = skill.rating;
      }

      if (skill.name === "Logical Reasoning") {
        generalData.logical_reasoning = skill.rating;
      }

      if (skill.name === "Communication") {
        generalData.communication = skill.rating;
      }
    });

    try {
      const response = await API.post("/recommend", {
        name: formData.name,
        education: formData.education,
        cgpa: Number(formData.cgpa),

        ...technicalData,
        ...generalData,

        interest: formData.interest,
        experience: formData.experience,
      });

      console.log("Recommendation Response:", response.data);
        sessionStorage.setItem(
      "recommendationResult",
      JSON.stringify(response.data)
    );

    window.location.href = "/recommendation";
    } catch (error) {
      console.error("API Error:", error);

      if (error.response) {
        console.error("Backend Error:", error.response.data);
        alert("Backend rejected the request.");
      } else if (error.request) {
        alert(
          "No response received from the backend. Please check if the FastAPI server is running."
        );
      } else {
        alert("Something went wrong. Please try again.");
      }
    }
  };

  return (
  <div className="student-page">
    <div className="student-wrapper">

      <div className="student-header">
        <h1>AI Career Recommendation System</h1>
        <p>
          Tell us about your education, skills, and experience to discover
          suitable career opportunities.
        </p>
      </div>

      <div className="form-card">
        <form onSubmit={handleSubmit}>

          {/* Basic Information */}
          <section className="form-section">
            <h2>Basic Information</h2>

            <div className="form-grid">

              <div className="form-group">
                <label>Full Name</label>
                <input
                  type="text"
                  name="name"
                  placeholder="Enter your full name"
                  value={formData.name}
                  onChange={handleChange}
                  required
                />
              </div>

              <div className="form-group">
                <label>Education</label>
                <input
                  type="text"
                  name="education"
                  placeholder="e.g. MCA, B.Tech, BCA"
                  value={formData.education}
                  onChange={handleChange}
                  required
                />
              </div>

              <div className="form-group">
                <label>CGPA</label>
                <input
                  type="number"
                  name="cgpa"
                  placeholder="Enter your CGPA"
                  min="0"
                  max="10"
                  step="0.01"
                  value={formData.cgpa}
                  onChange={handleChange}
                  required
                />
              </div>

              <div className="form-group">
                <label>Career Interest</label>
                <input
                  type="text"
                  name="interest"
                  placeholder="e.g. Data Analytics"
                  value={formData.interest}
                  onChange={handleChange}
                  required
                />
              </div>

              <div className="form-group full-width">
                <label>Experience</label>
                <input
                  type="text"
                  name="experience"
                  placeholder="e.g. Fresher, 1 year experience"
                  value={formData.experience}
                  onChange={handleChange}
                  required
                />
              </div>

            </div>
          </section>

          {/* Technical Skills */}
          <section className="form-section">
            <h2>Technical Skills</h2>

            <div className="skill-selector">

              <div className="form-group">
                <label>Skill</label>

                <select
                  value={selectedTechnicalSkill}
                  onChange={(e) =>
                    setSelectedTechnicalSkill(e.target.value)
                  }
                >
                  <option value="">Select a Technical Skill</option>

                  {technicalSkillOptions.map((skill) => (
                    <option
                      key={skill}
                      value={skill}
                      disabled={technicalSkills.some(
                        (item) => item.name === skill
                      )}
                    >
                      {skill}
                    </option>
                  ))}
                </select>
              </div>

              <div className="form-group">
                <label>Rating</label>

                <select
                  value={technicalRating}
                  onChange={(e) =>
                    setTechnicalRating(e.target.value)
                  }
                >
                  <option value="">Rating</option>

                  {Array.from({ length: 10 }, (_, index) => (
                    <option key={index + 1} value={index + 1}>
                      {index + 1}
                    </option>
                  ))}
                </select>
              </div>

              <button
                type="button"
                className="add-skill-btn"
                onClick={addTechnicalSkill}
              >
                Add Skill
              </button>

            </div>

            <p className="skill-count">
              Technical Skills: {technicalSkills.length}/7
            </p>

            <div className="skill-list">
              {technicalSkills.map((skill) => (
                <div className="skill-item" key={skill.name}>

                  <div>
                    <span className="skill-name">
                      {skill.name}
                    </span>

                    <span className="skill-rating">
                      {" "}• {skill.rating}/10
                    </span>
                  </div>

                  <button
                    type="button"
                    className="remove-btn"
                    onClick={() =>
                      removeTechnicalSkill(skill.name)
                    }
                  >
                    Remove
                  </button>

                </div>
              ))}
            </div>
          </section>

          {/* General Skills */}
          <section className="form-section">
            <h2>General Skills</h2>

            <div className="skill-selector">

              <div className="form-group">
                <label>Skill</label>

                <select
                  value={selectedGeneralSkill}
                  onChange={(e) =>
                    setSelectedGeneralSkill(e.target.value)
                  }
                >
                  <option value="">Select a General Skill</option>

                  {generalSkillOptions.map((skill) => (
                    <option
                      key={skill}
                      value={skill}
                      disabled={generalSkills.some(
                        (item) => item.name === skill
                      )}
                    >
                      {skill}
                    </option>
                  ))}
                </select>
              </div>

              <div className="form-group">
                <label>Rating</label>

                <select
                  value={generalRating}
                  onChange={(e) =>
                    setGeneralRating(e.target.value)
                  }
                >
                  <option value="">Rating</option>

                  {Array.from({ length: 10 }, (_, index) => (
                    <option key={index + 1} value={index + 1}>
                      {index + 1}
                    </option>
                  ))}
                </select>
              </div>

              <button
                type="button"
                className="add-skill-btn"
                onClick={addGeneralSkill}
              >
                Add Skill
              </button>

            </div>

            <p className="skill-count">
              General Skills: {generalSkills.length}/5
            </p>

            <div className="skill-list">
              {generalSkills.map((skill) => (
                <div className="skill-item" key={skill.name}>

                  <div>
                    <span className="skill-name">
                      {skill.name}
                    </span>

                    <span className="skill-rating">
                      {" "}• {skill.rating}/10
                    </span>
                  </div>

                  <button
                    type="button"
                    className="remove-btn"
                    onClick={() =>
                      removeGeneralSkill(skill.name)
                    }
                  >
                    Remove
                  </button>

                </div>
              ))}
            </div>
          </section>

          <button
            type="submit"
            className="submit-btn"
          >
            Get Career Recommendation
          </button>

        </form>
      </div>
    </div>
  </div>
);
}

export default StudentForm;