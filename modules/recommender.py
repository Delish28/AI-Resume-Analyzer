def generate_recommendations(missing_skills):
    recommendations = []

    for skill in sorted(missing_skills):
        recommendations.append(
            f"Consider learning or adding {skill} to your resume."
        )

    return recommendations


def suggest_job_roles(skills):
    skills = [skill.lower() for skill in skills]

    roles = []

    if "python" in skills:
        roles.append("Python Developer")

    if "data analytics" in skills or "pandas" in skills:
        roles.append("Data Analyst")

    if "java" in skills:
        roles.append("Java Developer")

    if "html" in skills and "css" in skills:
        roles.append("Web Developer")

    if "machine learning" in skills:
        roles.append("Machine Learning Engineer")

    if "sql" in skills or "rdbms" in skills:
        roles.append("Database / SQL Developer")

    if not roles:
        roles.append("Entry-Level Software Developer")

    return roles