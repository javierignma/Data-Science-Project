from openai import OpenAI
client = OpenAI()

def get_embeddings(text: str, model="text-embedding-3-small"):
    text = text.replace("\n", " ")
    return client.embeddings.create(input=[text], model=model).data[0].embedding