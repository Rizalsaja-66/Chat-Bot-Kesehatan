import json
import numpy as np
from sentence_transformers import SentenceTransformer
from scipy.spatial.distance import cosine

class HealthChatbot:
    def __init__(self, dataset_path="dataset_kesehatan.json", model_name="paraphrase-multilingual-MiniLM-L12-v2"):
        # Load pre-trained multilingual model suitable for Indonesian
        self.model = SentenceTransformer(model_name)
        self.dataset = self.load_dataset(dataset_path)
        self.questions = [item['pertanyaan'] for item in self.dataset]
        self.answers = [item['jawaban'] for item in self.dataset]
        
        # Pre-compute embeddings for all questions in the dataset
        self.question_embeddings = self.model.encode(self.questions)

    def load_dataset(self, path):
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def get_response(self, user_query, threshold=0.4):
        # Embed user query
        query_embedding = self.model.encode([user_query])[0]
        
        # Calculate cosine similarity with all questions
        similarities = []
        for q_emb in self.question_embeddings:
            # scipy cosine is distance (0 is identical), similarity = 1 - distance
            sim = 1 - cosine(query_embedding, q_emb)
            similarities.append(sim)
            
        # Find best match
        best_idx = np.argmax(similarities)
        best_score = similarities[best_idx]
        
        if best_score >= threshold:
            return self.answers[best_idx]
        else:
            return "Maaf, saya tidak menemukan jawaban yang relevan di database saya. Pastikan Anda menanyakan seputar informasi kesehatan umum."
