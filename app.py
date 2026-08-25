import streamlit as st

from modules.resume_parser import extract_text_from_pdf
from modules.skill_extractor import extract_skills
from modules.matcher import (
    extract_job_skills,
    calculate_match_score,
    get_matched_skills,
    get_missing_skills
)


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AI Resume Analyzer & Job Matcher",
    page_icon="📄",
    layout="wide"
)


# ============================================================
# HEADER
# ============================================================

st.title("📄 AI Resume Analyzer & Job Matcher")

st.write(
    "Upload your resume and enter a job description "
    "to find your job compatibility score."
)

st.divider()


# ============================================================
# STEP 1 - UPLOAD RESUME
# ============================================================

st.header("1️⃣ Upload Your Resume")

uploaded_file = st.file_uploader(
    "Choose your resume",
    type=["pdf"]
)


# Create resume_text before using it
resume_text = ""


if uploaded_file is not None:

    try:

        resume_text = extract_text_from_pdf(uploaded_file)

        st.success(
            f"✅ Resume uploaded: {uploaded_file.name}"
        )

    except Exception as e:

        st.error(
            f"❌ Could not read the resume: {e}"
        )

else:

    st.info(
        "📌 Please upload your PDF resume."
    )


# ============================================================
# STEP 2 - JOB DESCRIPTION
# ============================================================

job_description = st.text_area(
    "Paste the complete job description here",
    height=300,
    placeholder="..."
)

# LinkedIn Job Search
st.subheader("🔗 LinkedIn Job Search")

linkedin_job_url = st.text_input(
    "Paste LinkedIn Job Link",
    placeholder="https://www.linkedin.com/jobs/view/..."
)

if linkedin_job_url:
    if "linkedin.com/jobs" in linkedin_job_url:
        st.success("✅ LinkedIn job link added")

        st.markdown(
            f"[🔗 Open LinkedIn Job]({linkedin_job_url})"
        )

        st.info(
            "Copy the job description from LinkedIn and paste it below."
        )

    else:
        st.warning("⚠️ Please enter a valid LinkedIn job link.")

We are looking for a Junior Data Analyst / Software Developer Intern.

Responsibilities:
- Analyze and clean data using Python.
- Create reports and dashboards.
- Work with databases and SQL queries.
- Develop simple web applications.
- Collaborate with the development team.

Requirements:
- Python
- Java
- C
- HTML
- CSS
- JavaScript
- SQL
- RDBMS
- Data Analytics
- Pandas
- NumPy
- Git
- GitHub

Preferred Skills:
- Machine Learning
- MongoDB
- REST API
- React
- Streamlit
"""
)


# ============================================================
# EXTRACT RESUME SKILLS
# ============================================================

resume_skills = []


if resume_text:

    try:

        resume_skills = extract_skills(resume_text)

    except Exception as e:

        st.error(
            f"❌ Skill extraction error: {e}"
        )


# ============================================================
# DISPLAY EXTRACTED RESUME
# ============================================================

if resume_text:

    st.divider()

    st.header("📄 Extracted Resume Text")

    st.text_area(
        "Resume Content",
        resume_text,
        height=300
    )


# ============================================================
# DISPLAY RESUME SKILLS
# ============================================================

if resume_text:

    st.header("🛠️ Detected Resume Skills")

    if resume_skills:

        st.success(
            f"Found {len(resume_skills)} technical skills"
        )

        st.write(
            ", ".join(resume_skills)
        )

    else:

        st.warning(
            "No technical skills detected."
        )


# ============================================================
# STEP 3 - ANALYZE JOB MATCH
# ============================================================

st.divider()

st.header("3️⃣ Analyze Resume Against Job")

analyze_button = st.button(
    "🔍 Analyze Job Match",
    type="primary"
)


if analyze_button:

    # --------------------------------------------------------
    # CHECK RESUME
    # --------------------------------------------------------

    if not resume_text:

        st.error(
            "❌ Please upload your resume first."
        )

    # --------------------------------------------------------
    # CHECK JOB DESCRIPTION
    # --------------------------------------------------------

    elif not job_description.strip():

        st.error(
            "❌ Please enter a job description."
        )

    else:

        try:

            # ------------------------------------------------
            # EXTRACT JOB SKILLS
            # ------------------------------------------------

            job_skills = extract_job_skills(
                job_description
            )


            # ------------------------------------------------
            # CALCULATE MATCH SCORE
            # ------------------------------------------------

            score = calculate_match_score(
                resume_skills,
                job_skills
            )


            # ------------------------------------------------
            # GET MATCHED SKILLS
            # ------------------------------------------------

            matched_skills = get_matched_skills(
                resume_skills,
                job_skills
            )


            # ------------------------------------------------
            # GET MISSING SKILLS
            # ------------------------------------------------

            missing_skills = get_missing_skills(
                resume_skills,
                job_skills
            )


            # =================================================
            # DISPLAY SCORE
            # =================================================

            st.divider()

            st.subheader(
                "🎯 Resume-Job Match Score"
            )

            st.metric(
                "Job Compatibility",
                f"{score}%"
            )

            st.progress(
                min(max(score / 100, 0.0), 1.0)
            )


            # =================================================
            # SCORE MESSAGE
            # =================================================

            if score >= 80:

                st.success(
                    "🌟 Excellent match! Your resume strongly "
                    "matches this job."
                )

            elif score >= 60:

                st.success(
                    "👍 Good match! You have many of the "
                    "required skills."
                )

            elif score >= 40:

                st.warning(
                    "⚠️ Moderate match. Consider adding "
                    "some missing skills."
                )

            else:

                st.error(
                    "❌ Low match. Your resume needs more "
                    "relevant technical skills."
                )


            # =================================================
            # JOB SKILLS
            # =================================================

            st.subheader(
                "💼 Skills Required by Job"
            )

            if job_skills:

                st.write(
                    ", ".join(job_skills)
                )

            else:

                st.warning(
                    "No technical skills detected in "
                    "the job description."
                )


            # =================================================
            # MATCHED SKILLS
            # =================================================

            st.subheader(
                "✅ Matched Skills"
            )

            if matched_skills:

                st.success(
                    ", ".join(
                        skill.title()
                        for skill in matched_skills
                    )
                )

            else:

                st.warning(
                    "No matching skills found."
                )


            # =================================================
            # MISSING SKILLS
            # =================================================

            st.subheader(
                "❌ Missing Skills"
            )

            if missing_skills:

                st.error(
                    ", ".join(
                        skill.title()
                        for skill in missing_skills
                    )
                )

            else:

                st.success(
                    "🎉 No missing technical skills!"
                )


            # =================================================
            # RECOMMENDATIONS
            # =================================================

            st.subheader(
                "💡 Skills You Should Consider Learning"
            )

            if missing_skills:

                for skill in missing_skills:

                    st.write(
                        f"📚 {skill.title()}"
                    )

            else:

                st.success(
                    "Your technical skills match the "
                    "job requirements very well!"
                )


            # =================================================
            # JOB ROLE SUGGESTION
            # =================================================

            st.subheader(
                "💼 Suggested Job Roles"
            )

            detected = [
                skill.lower()
                for skill in resume_skills
            ]

            if (
                "python" in detected
                or "data analytics" in detected
                or "pandas" in detected
                or "numpy" in detected
            ):

                st.write("🔹 Python Developer")
                st.write("🔹 Data Analyst")
                st.write("🔹 Junior Data Scientist")

            elif (
                "java" in detected
                or "sql" in detected
            ):

                st.write("🔹 Java Developer")
                st.write("🔹 Software Developer")
                st.write("🔹 Database Developer")

            elif (
                "html" in detected
                or "css" in detected
                or "javascript" in detected
            ):

                st.write("🔹 Web Developer")
                st.write("🔹 Front-End Developer")
                st.write("🔹 Full-Stack Developer")

            else:

                st.write(
                    "🔹 Software Developer Intern"
                )
                st.write(
                    "🔹 IT Support Intern"
                )


        except Exception as e:

            st.error(
                f"❌ Error while analyzing the job: {e}"
            )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "AI Resume Analyzer & Job Matcher | Python + Streamlit"
)
