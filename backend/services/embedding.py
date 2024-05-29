from sentence_transformers import SentenceTransformer
from typing import List

def get_embeddings(text: str, model_name="all-MiniLM-L6-v2") -> List[float]:
    model = SentenceTransformer(model_name)
    text_length = len(text)

    maxsplit = int(text_length/200) if text_length > 200 else 1

    texts = text.split(maxsplit=maxsplit)

    return model.encode(texts).tolist()