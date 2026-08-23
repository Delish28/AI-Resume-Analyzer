# 🤖 AI Resume Analyzer & Job Matcher

An AI-powered Resume Analyzer and Job Matching System built with Python and Streamlit.

## 📌 Project Overview

This application analyzes a candidate's resume and compares it with a given job description. It extracts technical skills, calculates a resume-job compatibility score, identifies matched and missing skills, and recommends skills and suitable job roles.

## 🚀 Features

- 📄 Upload Resume in PDF format
- 🔍 Extract text from resumes
- 🛠️ Detect technical skills automatically
- 💼 Analyze job descriptions
- 📊 Calculate Resume-Job Match Score
- ✅ Display matched skills
- ❌ Identify missing skills
- 💡 Recommend skills to learn
- 🎯 Suggest suitable job roles
- 🌐 Interactive Streamlit interface

## 🛠️ Technologies Used

- Python
- Streamlit
- PyPDF
- Pandas
- NumPy
- Scikit-learn
- Regex
- Joblib

## 📂 Project Structure

```text
AI-Resume-Analyzer/
│
├── app.py
├── requirements.txt
│
├── data/
│   └── skills.csv
│
└── modules/
    ├── job_analyzer.py
    ├── matcher.py
    ├── recommender.py
    ├── resume_parser.py
    └── skill_extractor.py
