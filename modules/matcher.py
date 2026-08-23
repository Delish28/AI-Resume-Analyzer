import re


def extract_job_skills(job_description):
    skills_database = [
        "python",
        "java",
        "c",
        "c++",
        "c#",
        "html",
        "css",
        "javascript",
        "react",
        "node.js",
        "node",
        "php",
        "sql",
        "mysql",
        "mongodb",
        "postgresql",
        "oracle",
        "rdbms",
        "pandas",
        "numpy",
        "matplotlib",
        "seaborn",
        "plotly",
        "scikit-learn",
        "machine learning",
        "deep learning",
        "tensorflow",
        "pytorch",
        "git",
        "github",
        "docker",
        "kubernetes",
        "fastapi",
        "flask",
        "django",
        "streamlit",
        "data analytics",
        "data science",
        "excel",
        "power bi",
        "tableau",
        "rest api",
        "api"
    ]

    job_text = job_description.lower()

    detected_skills = []

    for skill in skills_database:
        if re.search(r"\b" + re.escape(skill) + r"\b", job_text):
            detected_skills.append(skill)

    return detected_skills


def calculate_match_score(resume_skills, job_skills):

    if not job_skills:
        return 0

    resume_set = set(skill.lower() for skill in resume_skills)
    job_set = set(skill.lower() for skill in job_skills)

    matched_skills = resume_set.intersection(job_set)

    score = (len(matched_skills) / len(job_set)) * 100

    return round(score, 2)


def get_matched_skills(resume_skills, job_skills):

    resume_set = set(skill.lower() for skill in resume_skills)
    job_set = set(skill.lower() for skill in job_skills)

    return sorted(resume_set.intersection(job_set))


def get_missing_skills(resume_skills, job_skills):

    resume_set = set(skill.lower() for skill in resume_skills)
    job_set = set(skill.lower() for skill in job_skills)

    return sorted(job_set - resume_set)