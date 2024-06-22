from persistence.milvus_manager import MilvusManager
from services.doc_to_text import describe_doc

prefix = "documents/Criptografia/"

milvus_manager = MilvusManager("Criptografia_Prompt03", "IP")

documents = [
    {
        "doc_name": "Pauta Control1 2022-2.pdf",
        "content": describe_doc(f"{prefix}Pauta Control1 2022-2.pdf"),
        "link_ref": "https://drive.google.com/file/d/1vHb4055RxSw4kALVTqTivuft01dZLCeR/view"
    },
    {
        "doc_name": "Pauta Control1 2023-1.pdf",
        "content": describe_doc(f"{prefix}Pauta Control1 2023-1.pdf"),
        "link_ref": "https://drive.google.com/file/d/1n77L1-ETOVIWESuiQJfElgHejOISBl8w/view"
    },
    {
        "doc_name": "Pauta Control2 2022-2.pdf", 
        "content": describe_doc(f"{prefix}Pauta Control2 2022-2.pdf"), 
        "link_ref": "https://drive.google.com/file/d/1YEBX0-VAFEcSWiNWbNktcHC4je1s6OPF/view"
    },
    {
        "doc_name": "Pauta Control2 2023-1.pdf", 
        "content": describe_doc(f"{prefix}Pauta Control2 2023-1.pdf"), 
        "link_ref": "https://drive.google.com/file/d/1VGbvmrQCIyM0AdfXYMMjr48anhVYLqZz/view"
    },
    {
        "doc_name": "Pauta Control4 2022-2.pdf", 
        "content": describe_doc(f"{prefix}Pauta Control4 2022-2.pdf"), 
        "link_ref": "https://drive.google.com/file/d/1j_wYy6RZBZS16t77Ho7Mb79fLCskmT99/view"
    },
    {
        "doc_name": "Pauta Examen 2023-1 (1)[1].pdf", 
        "content": describe_doc(f"{prefix}Pauta Examen 2023-1 (1)[1].pdf"), 
        "link_ref": "https://drive.google.com/file/d/1K1VCIz2vsE79fusiYv3lCkjY_GVMMxYN/view"
    },
    {
        "doc_name": "Pauta Solemne1 2022-2.pdf", 
        "content": describe_doc(f"{prefix}Pauta Solemne1 2022-2.pdf"), 
        "link_ref": "https://drive.google.com/file/d/1a1sJ4g5MfFNa7I2HcXTABZ1l5JRqgx2n/view"
    },
    {
        "doc_name": "Pauta Solemne1 2023-1.pdf", 
        "content": describe_doc(f"{prefix}Pauta Solemne1 2023-1.pdf"), 
        "link_ref": "https://drive.google.com/file/d/1Rj5DUfszNlowjb43RLJSiVk9grmDbcx0/view"
    },
    {
        "doc_name": "Pauta Solemne2 2023-1.pdf", 
        "content": describe_doc(f"{prefix}Pauta Solemne2 2023-1.pdf"), 
        "link_ref": "https://drive.google.com/file/d/1eXfngoojJjMjiBAaU8AkRNdxQSBQGGpS/view"
    },
    {
        "doc_name": "Pauta_Examen_2022-2[1].pdf", 
        "content": describe_doc(f"{prefix}Pauta_Examen_2022-2[1].pdf"), 
        "link_ref": "https://drive.google.com/file/d/1H0-SlRlL6hPUqNCUwDO_BlQdNqwYSvoC/view"
    },
    {
        "doc_name": "Pauta_Solemne2_2023-2[1].pdf", 
        "content": describe_doc(f"{prefix}Pauta_Solemne2_2023-2[1].pdf"), 
        "link_ref": "https://drive.google.com/file/d/1wrYzFhybGXNxMSfe0YMnV5N1tKY94yG8/view"
    },
    {
        "doc_name": "Pauta+Examen[1].pdf", 
        "content": describe_doc(f"{prefix}Pauta+Examen[1].pdf"), 
        "link_ref": "https://drive.google.com/file/d/1-l63of_CviUDOTwY8E4LtH8RrcdYi-R2/view"
    },
]

milvus_manager.insert_data(documents)