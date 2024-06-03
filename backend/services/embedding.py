from sentence_transformers import SentenceTransformer
from typing import List
import numpy as np

def split_string(string, chunk_size=400):
    chunks = []
    while len(string) > chunk_size:
        space_index = string.rfind(".", 0, chunk_size)  # Find the last space within the chunk size limit
        if space_index == -1:
            # If no space is found, split at chunk_size
            chunks.append(string[:chunk_size])
            string = string[chunk_size:]
        else:
            # Split at the last space before the chunk size limit
            chunks.append(string[:space_index])
            string = string[space_index+1:]  # Skip the space
    chunks.append(string)  # Append the remaining string
    return chunks


def get_embeddings(text: str) -> np.ndarray:
    embedding_fn = SentenceTransformer(
        model_name_or_path='all-MiniLM-L6-v2',
        device='cpu' # Change it to cpu if anything goes wrong.
    )
    return np.array(embedding_fn.encode(sentences=text))