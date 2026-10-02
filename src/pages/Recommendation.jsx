import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import API from "../services/api";
import "./Recommendation.css";

function Recommendation() {
  const navigate = useNavigate();

  const [recommendation, setRecommendation] = useState(null);
  const [careers, setCareers] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const storedResult = sessionStorage.getItem("recommendationResult");

    if (!storedResult) {
      navigate("/");
      return;
    }

    const result = JSON.parse(storedResult);
    setRecommendation(result);

    const fetchCareers = async () => {
      try {
        const response = await API.get("/careers");
        setCareers(response.data);
      } catch (error) {
        console.error("Failed to load career data:", error);
      } finally {
        setLoading(false);
      }
    };

    fetchCareers();
  }, [navigate]);

  if (!recommendation || loading) {
    return (
      <div className="recommendation-loading">
        <div className="loading-card">
          <div className="loading-spinner"></div>
          <h2>Preparing Your Career Result</h2>
          <p>Please wait while we load your recommendation.</p>
        </div>
      </div>
    );
  }

  const recommendedCareer = recommendation.recommended_career;
  const careerScores = recommendation.career_scores || {};

  const careerDetails = careers.find(
    (career) => career.name === recommendedCareer
  );

  const scoreEntries = Object.entries(careerScores)
  .sort(([, scoreA], [, scoreB]) => Number(scoreB) - Number(scoreA))
  .slice(0, 4);
  const maximumScore = Math.max(
    ...Object.values(careerScores).map(Number),
    1
  );

  const requiredSkills = careerDetails?.required_skills
    ? careerDetails.required_skills
        .split(",")
        .map((skill) => skill.trim())
        .filter(Boolean)
    : [];

  const description =
    careerDetails?.description ||
    "This career recommendation is based on your submitted education, skills, interests, and profile information.";

  const handleBackToForm = () => {
    navigate("/");
  };

  const handleExploreCareer = () => {
    if (careerDetails?.id) {
      navigate(`/careers/${careerDetails.id}`);
    } else {
      navigate("/careers");
    }
  };

  return (
    <div className="recommendation-page">
      <nav className="recommendation-navbar">
        <div className="brand-section">
          <div className="brand-icon">🎓</div>
          <span>AI Career Recommendation System</span>
        </div>

        <div className="nav-links">
          <button className="nav-link active" onClick={handleBackToForm}>
            Home
          </button>

          <button
            className="nav-link"
            onClick={() => navigate("/careers")}
          >
            Career Explorer
          </button>

          <button className="nav-link">
            About
          </button>

          <div className="user-icon">👤</div>
        </div>
      </nav>

      <main className="recommendation-container">
        <section className="result-header">
          <span className="result-label">YOUR CAREER RESULT</span>

          <h1>
            Your Career <span>Result</span>
          </h1>

          <p>
            Based on your education, skills, interests, and profile,
            we identified a career path that matches your current profile.
          </p>
        </section>

        <section className="recommended-card">
  <div className="recommended-career-icon">
    <svg viewBox="0 0 64 64" aria-hidden="true">
      <rect x="10" y="38" width="10" height="16" rx="2"></rect>
      <rect x="27" y="28" width="10" height="26" rx="2"></rect>
      <rect x="44" y="16" width="10" height="38" rx="2"></rect>
    </svg>
  </div>

  <div className="recommended-content">
    <div className="recommendation-badge">
      ✦ Recommended Career
    </div>

    <h2>{recommendedCareer}</h2>

    <p>{description}</p>

    
  </div>

  <div className="career-illustration">
    <img
      src="/images/career-analytics-illustration.png"
      alt="Career analytics illustration"
    />
  </div>
</section>

        <section className="why-career-card">
          <div className="why-icon" aria-hidden="true">
            <svg viewBox="0 0 24 24">
                <path d="M9 18h6" />
                <path d="M10 21h4" />
                <path d="M8.5 14.5C7.55 13.65 7 12.42 7 11a5 5 0 0 1 10 0c0 1.42-.55 2.65-1.5 3.5-.7.63-1.1 1.18-1.25 2H9.75c-.15-.82-.55-1.37-1.25-2Z" />
                <path d="M12 2v1" />
                <path d="M4.93 4.93l.7.7" />
                <path d="M19.07 4.93l-.7.7" />
            </svg>
            </div>

            <div>
            <h3>Why this career?</h3>
            <p>
              This career received the highest score from the
              recommendation engine based on your submitted profile.
            </p>

            <div className="skill-chips">
              {requiredSkills.length > 0 ? (
                requiredSkills.map((skill) => (
                <span className="skill-chip" key={skill}>
                    {skill}
                </span>
                ))
              ) : (
                <span className="skill-chip">
                  Career skills available in Career Explorer
                </span>
              )}
            </div>
          </div>
        </section>

        <section className="scores-section">
          <div className="section-heading">
            <div className="score-title-group">
                <div className="score-title-icon" aria-hidden="true">
                <svg viewBox="0 0 24 24">
                    <rect x="3" y="13" width="4" height="8" rx="1" />
                    <rect x="10" y="9" width="4" height="12" rx="1" />
                    <rect x="17" y="4" width="4" height="17" rx="1" />
                </svg>
                </div>

                <div>
                <h2>Career Match Scores</h2>
                <p>Top career options based on your profile:</p>
                </div>
            </div>

            <span className="score-note">
                Based on your profile
            </span>
            </div>

          <div className="scores-card">
            {scoreEntries.map(([career, score]) => {
              const numericScore = Number(score);
              const percentage =
                maximumScore > 0
                  ? Math.round((numericScore / maximumScore) * 100)
                  : 0;

              return (
                <div className="score-row" key={career}>
                  <div className="score-info">
                    <span className="career-name">{career}</span>
                    <strong>{numericScore}</strong>
                  </div>

                  <div className="score-bar">
                    <div
                      className={`score-fill ${
                        career === recommendedCareer ? "highlight" : ""
                      }`}
                      style={{ width: `${percentage}%` }}
                    ></div>
                  </div>

                  <span className="score-percentage">
                    {percentage}%
                  </span>
                </div>
              );
            })}
          </div>
        </section>

        <section className="overview-section">
          <div className="section-heading">
            <div>
              <span className="section-label">CAREER INFORMATION</span>
              <h2>Career Overview</h2>
            </div>
          </div>

          <div className="overview-grid">
            <div className="overview-card">
              <div className="overview-icon">
                <svg viewBox="0 0 24 24" aria-hidden="true">
                    <circle cx="12" cy="12" r="8"></circle>
                    <circle cx="12" cy="12" r="3"></circle>
                    <path d="M12 4V2"></path>
                    <path d="M20 12h2"></path>
                </svg>
                </div>
              <h3>Key Responsibilities</h3>
              <p>{description}</p>
            </div>

            <div className="overview-card">
              <div className="overview-icon">
                <svg viewBox="0 0 24 24" aria-hidden="true">
                    <rect x="4" y="12" width="4" height="8" rx="1"></rect>
                    <rect x="10" y="8" width="4" height="12" rx="1"></rect>
                    <rect x="16" y="4" width="4" height="16" rx="1"></rect>
                </svg>
                </div>
              <h3>Required Skills</h3>

              {requiredSkills.length > 0 ? (
                <ul>
                  {requiredSkills.map((skill) => (
                    <li key={skill}>{skill}</li>
                  ))}
                </ul>
              ) : (
                <p>Skill information is available in Career Explorer.</p>
              )}
            </div>

            <div className="overview-card">
              <div className="overview-icon">
                <svg viewBox="0 0 24 24" aria-hidden="true">
                    <circle cx="8" cy="8" r="3"></circle>
                    <circle cx="16" cy="8" r="3"></circle>
                    <path d="M3 20c0-3 2-5 5-5s5 2 5 5"></path>
                    <path d="M11 20c0-3 2-5 5-5s5 2 5 5"></path>
                </svg>
                </div>
              <h3>Career Opportunities</h3>
              <p>
                Explore detailed career information and available
                opportunities through the Career Explorer.
              </p>
            </div>

            <div className="overview-card">
              <div className="overview-icon">
                <svg viewBox="0 0 24 24" aria-hidden="true">
                    <path d="M4 19V5"></path>
                    <path d="M4 19h16"></path>
                    <path d="M7 15l4-4 3 2 5-6"></path>
                    <path d="M15 7h4v4"></path>
                </svg>
                </div>
              <h3>Average Salary</h3>
              <p>
                Salary information is not provided by the current
                career recommendation API.
              </p>
            </div>
          </div>
        </section>

        <div className="bottom-actions">
          <button
            className="secondary-button"
            onClick={handleBackToForm}
          >
            ← Back to Form
          </button>

          <button
            className="primary-button"
            onClick={handleExploreCareer}
          >
            Explore Career Details
            <span>→</span>
          </button>
        </div>
      </main>
    </div>
  );
}

export default Recommendation;