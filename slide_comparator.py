from sentence_transformers import SentenceTransformer
import numpy as np
from numpy.linalg import norm

def cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / (norm(vec1) * norm(vec2))

class SlideComparator:
    def __init__(self, first_slide, second_slide):
        self.first_slide = first_slide
        self.second_slide = second_slide

    def compare_images(self):
        # Compute Hamming distance (lower = more similar)
        difference = self.first_slide.phash - self.second_slide.phash

        # Define a similarity threshold (e.g., 10)
        if difference < 10:
            return f"Hamming Distance: {difference}\n\nSimilar Slide"
        else:
            return f"Hamming Distance: {difference}\n\nDifferent Slide"
        
    def compare_content(self):
        model = SentenceTransformer("all-MiniLM-L6-v2")  # Small, fast model
        array1 = model.encode(self.first_slide.content, normalize_embeddings=True)  # Returns a NumPy array
        array2 = model.encode(self.second_slide.content, normalize_embeddings=True)  # Returns a NumPy array

        # Example embeddings
        vec1 = np.array(array1)
        vec2 = np.array(array2)

        similarity = cosine_similarity(vec1, vec2)
        return similarity