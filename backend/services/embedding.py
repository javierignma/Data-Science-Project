from sentence_transformers import SentenceTransformer
import numpy as np

def get_embeddings(text: str) -> np.ndarray:
    embedding_fn = SentenceTransformer(
        model_name_or_path='all-MiniLM-L6-v2',
        device='cpu' # Change it to cpu if anything goes wrong.
    )
    return np.array(embedding_fn.encode(sentences=text))