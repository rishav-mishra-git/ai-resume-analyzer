import streamlit as st
from pdf_reader import extract_text_from_pdf
from preprocess import clean_text
from matcher import match_skills

st.set_page_config(
    page_title="Skill-Based Resume Matcher",
    page_icon="📄",
    layout="centered"
)

st.title("📄 Skill-Based Resume Matching System")
st.write("Upload a resume PDF and enter required skills to check matching accuracy.")

# Upload PDF
uploaded_pdf = st.file_uploader("📎 Upload Resume (PDF)", type=["pdf"])

# Skill input
skills_input = st.text_input(
    "🛠 Enter required skills (comma-separated)",
    placeholder="python, machine learning, nlp, pandas"
)

if st.button("🔍 Analyze Resume"):
    if uploaded_pdf is None or not skills_input.strip():
        st.warning("⚠️ Please upload a PDF and enter skills.")
    else:
        # Extract and clean resume text
        raw_text = extract_text_from_pdf(uploaded_pdf)
        clean_resume = clean_text(raw_text)

        # Process user skills
        user_skills = [skill.strip() for skill in skills_input.split(",")]

        # Match skills
        accuracy, matched_skills, missing_skills = match_skills(
            clean_resume, user_skills
        )

        # Display results
        st.subheader("📊 Matching Results")
        st.metric("Skill Match Accuracy", f"{accuracy}%")

        col1, col2 = st.columns(2)

        with col1:
            st.write("### ✅ Matched Skills")
            st.write(matched_skills if matched_skills else "None")

        with col2:
            st.write("### ❌ Missing Skills")
            st.write(missing_skills if missing_skills else "None 🎉")
