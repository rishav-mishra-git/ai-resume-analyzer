import streamlit as st
from preprocess import clean_text
from skills import extract_skills
from matcher import match_resume

# Page configuration
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="centered"
)

st.title("📄 AI Resume Analyzer & Job Match Predictor")
st.write("Analyze your resume against a job description using NLP and ML.")

# Inputs
resume_text = st.text_area("📌 Paste Resume Text", height=200)
job_text = st.text_area("📌 Paste Job Description", height=200)

# Button
if st.button("🔍 Analyze Resume"):
    if resume_text.strip() == "" or job_text.strip() == "":
        st.warning("⚠️ Please provide both Resume and Job Description.")
    else:
        # Preprocessing
        clean_resume = clean_text(resume_text)
        clean_job = clean_text(job_text)

        # Matching score
        score = match_resume(clean_resume, clean_job)

        # Skill extraction
        resume_skills = extract_skills(clean_resume)
        job_skills = extract_skills(clean_job)

        matched_skills = list(set(resume_skills) & set(job_skills))
        missing_skills = list(set(job_skills) - set(resume_skills))

        # Output
        st.subheader("📊 Results")
        st.metric(label="Resume Match Score", value=f"{score}%")

        col1, col2 = st.columns(2)

        with col1:
            st.write("### ✅ Matched Skills")
            if matched_skills:
                st.write(matched_skills)
            else:
                st.write("No matched skills found")

        with col2:
            st.write("### ❌ Missing Skills")
            if missing_skills:
                st.write(missing_skills)
            else:
                st.write("No missing skills 🎉")
