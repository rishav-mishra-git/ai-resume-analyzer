def match_skills(resume_text: str, user_skills: list):
    matched = []
    missing = []

    for skill in user_skills:
        skill_clean = skill.lower().strip()
        if skill_clean in resume_text:
            matched.append(skill_clean)
        else:
            missing.append(skill_clean)

    accuracy = (len(matched) / len(user_skills)) * 100 if user_skills else 0

    return round(accuracy, 2), matched, missing

