from modules.skill_extractor import extract_skills


def analyze_job_description(job_description):
    """
    Extract required skills from the job description.
    """

    if not job_description:
        return []

    return extract_skills(job_description)