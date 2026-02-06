def extract_skills(text: str) -> list:
    """
    Extracts predefined skills from text
    """
    skills_db = [
        "python", "machine learning", "deep learning", "nlp",
        "data analysis", "pandas", "numpy", "sql",
        "scikit-learn", "tensorflow", "streamlit"
    ]

    extracted = []

    for skill in skills_db:
        if skill in text:
            extracted.append(skill)

    return sorted(list(set(extracted)))
