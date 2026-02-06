from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def match_resume(resume_text: str, job_text: str) -> float:
    """
    Calculates similarity score between resume and job description
    """
    vectorizer = TfidfVectorizer()

    vectors = vectorizer.fit_transform([resume_text, job_text])

    similarity_score = cosine_similarity(vectors[0], vectors[1])[0][0]

    return round(similarity_score * 100, 2)
