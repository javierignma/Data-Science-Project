from persistence.milvus_manager import MilvusManager
from services.doc_to_text import describe_doc

prefix = "documents/IA/IA/"

milvus_manager = MilvusManager("IA", "COSINE")

documents = [
    {
        "doc_name": "Clase 2 - Logica.pdf",
        "content": describe_doc(f"{prefix}Clase 2 - Logica.pdf"),
        "link_ref": "https://drive.google.com/file/d/1_lG9I4ve0fKwGx2KCnPDRohxlL5RzioQ/view"
    },
    {
        "doc_name": "Clase 3 - Bayes.pdf",
        "content": describe_doc(f"{prefix}Clase 3 - Bayes.pdf"),
        "link_ref": "https://drive.google.com/file/d/1DbykRHzKIQseQFMbxuffcOfTh5D6lV9N/view"
    },
    {
        "doc_name": "Clase 4 - Markov-HMM.pdf", 
        "content": describe_doc(f"{prefix}Clase 4 - Markov-HMM.pdf"), 
        "link_ref": "https://drive.google.com/file/d/1bjQxBH3tllIVmJOhEyBVNssRqq7GyRNB/view"
    },
    {
        "doc_name": "Clase 5 - BackwardForward-Viterbi.pdf", 
        "content": describe_doc(f"{prefix}Clase 5 - BackwardForward-Viterbi.pdf"), 
        "link_ref": "https://drive.google.com/file/d/155JyUOoWvyH6DcQ6FnzV7yF7kQ11l8V0/view"
    },
    {
        "doc_name": "Clase 6 - Monte Carlo y FdP.pdf", 
        "content": describe_doc(f"{prefix}Clase 6 - Monte Carlo y FdP.pdf"), 
        "link_ref": "https://drive.google.com/file/d/1h4D31Ynz6iGVh6xvzyZQi4bhPgw5wJTE/view"
    },
    {
        "doc_name": "Clase 7 - FdK.pdf", 
        "content": describe_doc(f"{prefix}Clase 7 - FdK.pdf"), 
        "link_ref": "https://drive.google.com/file/d/17KJONPyEONgthmUKpO9GqblMUqZBneDB/view"
    },
    {
        "doc_name": "Clase 8 - MLE.pdf", 
        "content": describe_doc(f"{prefix}Clase 8 - MLE.pdf"), 
        "link_ref": "https://drive.google.com/file/d/1DWjKaROvWzb3CCvf0vdGFcuRajTozIFz/view"
    },
    {
        "doc_name": "Clase 9 - EM.pdf", 
        "content": describe_doc(f"{prefix}Clase 9 - EM.pdf"), 
        "link_ref": "https://drive.google.com/file/d/1BOIDFkRrAbDXsteBKhiDRuWXc7y_DGMh/view"
    },
    {
        "doc_name": "Clase 10 - Tipos de IA.pdf", 
        "content": describe_doc(f"{prefix}Clase 10 - Tipos de IA.pdf"), 
        "link_ref": "https://drive.google.com/file/d/1F_pG-DUPl-avSSjVg2CT8PTqmzgzk_54/view"
    },
    {
        "doc_name": "Clase 11 - Clustering.pdf", 
        "content": describe_doc(f"{prefix}Clase 11 - Clustering.pdf"), 
        "link_ref": "https://drive.google.com/file/d/14nq39HQJUUlD4tTrjNIINiMbIdbNUzs4/view"
    },
    {
        "doc_name": "Clase 12 - RegresionLineal.pdf", 
        "content": describe_doc(f"{prefix}Clase 12 - RegresionLineal.pdf"), 
        "link_ref": "https://drive.google.com/file/d/1iy3cl1SdI1vXx4QeOtZAeXVYwsdL8ibz/view"
    },
    {
        "doc_name": "Clase 13 - RegresionLogistica.pdf", 
        "content": describe_doc(f"{prefix}Clase 13 - RegresionLogistica.pdf"), 
        "link_ref": "https://drive.google.com/file/d/1B6wktIU1E_0zNFL5l2AoBnu5bejpAIDk/view"
    },
    {
        "doc_name": "Clase 14 - KNN y SVM.pdf", 
        "content": describe_doc(f"{prefix}Clase 14 - KNN y SVM.pdf"), 
        "link_ref": "https://drive.google.com/file/d/1sGUhMd1W2hEFoPs_JNQWEy9UbsOVf5Lr/view"
    },
    {
        "doc_name": "Clase 15 - Regularizacion.pdf", 
        "content": describe_doc(f"{prefix}Clase 15 - Regularizacion.pdf"), 
        "link_ref": "https://drive.google.com/file/d/16gBdFYVnMx_J180bQ5oyFuzxjah-JYgi/view"
    },
    {
        "doc_name": "Clase 16 - ANN1.pdf", 
        "content": describe_doc(f"{prefix}Clase 16 - ANN1.pdf"), 
        "link_ref": "https://drive.google.com/file/d/1zWt47_q0jEO2Bt8zIdsE3s1vmbzpBUHV/view"
    },
    {
        "doc_name": "Clase 17 - ANN2.pdf", 
        "content": describe_doc(f"{prefix}Clase 17 - ANN2.pdf"), 
        "link_ref": "https://drive.google.com/file/d/1P0U5tuGwTzPXR5zb82yNsoMNCTJW7DzD/view"
    },
    {
        "doc_name": "Clase 18 - ANN3.pdf", 
        "content": describe_doc(f"{prefix}Clase 18 - ANN3.pdf"), 
        "link_ref": "https://drive.google.com/file/d/1q8MVh6zgXdSrLsZhrHRxFlf7RmyGPyKL/view"
    },
    {
        "doc_name": "Clase 19 - AlgGeneticos.pdf", 
        "content": describe_doc(f"{prefix}Clase 19 - AlgGeneticos.pdf"), 
        "link_ref": "https://drive.google.com/file/d/102U4p5T2scpqPYr3oo1xgTsvXRIvKyWh/view"
    },
]

milvus_manager.insert_data(documents)