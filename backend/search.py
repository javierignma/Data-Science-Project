from persistence.milvus_manager import MilvusManager

milvus_manager = MilvusManager("Criptografia_Prompt03", "IP")

response = milvus_manager.search_collection(
    input("Busca algún documento.")
)

for res in response:
    print(f"Document: {res["doc_name"]}")
    print(f"Link: {res["link_ref"]}")
    print(f"Similarity percentage: {res["similarity_percentage"]}%")
    print("------------------------------------------------------------")