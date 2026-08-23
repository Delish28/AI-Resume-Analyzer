import re


# Skills used by the resume analyzer
SKILLS = [
    "Python",
    "Java",
    "C",
    "C++",
    "C#",
    "JavaScript",
    "TypeScript",
    "HTML",
    "CSS",
    "React",
    "Angular",
    "Node.js",
    "PHP",
    "SQL",
    "MySQL",
    "MongoDB",
    "PostgreSQL",
    "RDBMS",
    "Pandas",
    "NumPy",
    "Scikit-learn",
    "TensorFlow",
    "PyTorch",
    "Machine Learning",
    "Deep Learning",
    "Artificial Intelligence",
    "NLP",
    "Computer Vision",
    "Data Science",
    "Data Analytics",
    "Power BI",
    "Tableau",
    "Excel",
    "Git",
    "GitHub",
    "Docker",
    "Kubernetes",
    "AWS",
    "Azure",
    "FastAPI",
    "Flask",
    "Django",
    "Streamlit"
]


def extract_skills(text):
    """
    Extract technical skills from text.
    Returns a list of detected skills.
    """

    if not text:
        return []

    text_lower = text.lower()

    found_skills = []

    for skill in SKILLS:

        # Escape special characters such as C++, C#, Node.js
        pattern = r"(?<!\w)" + re.escape(skill.lower()) + r"(?!\w)"

        if re.search(pattern, text_lower):
            found_skills.append(skill)

    return sorted(found_skills)