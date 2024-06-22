from openai import OpenAI
import base64
import fitz
import requests
from io import BytesIO
from dotenv import load_dotenv
from os import getenv

load_dotenv()

# OpenAI API Key
api_key = getenv("OPENAI_API_KEY")

def pdf_to_base64_images(pdf_path):
    # Abre el archivo PDF
    pdf_file = fitz.open(pdf_path)

    num_pages =pdf_file.page_count
    print(f"This PDF has {num_pages} pages.")

    # Lista para almacenar las imágenes en base64
    base64_images = []

    # Itera sobre cada página del PDF
    for page_index in range(num_pages):
        # Selecciona la página (las páginas se numeran desde 0)
        page = pdf_file.load_page(page_index)
        
        # Crea una imagen a partir de la página
        image = page.get_pixmap()
        
        # Convierte la imagen a bytes
        img_bytes = image.tobytes()
        
        # Codifica los bytes en base64
        base64_image = base64.b64encode(img_bytes).decode('utf-8')
        
        # Agrega la imagen en base64 a la lista
        base64_images.append(base64_image)

    return base64_images

def describe_doc(doc_path) -> str:
    base64_images = pdf_to_base64_images(doc_path)

    text_description = []

    client = OpenAI(api_key=api_key)

    for image in base64_images:
        
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
              {
                "role": "user",
                "content": [
                  {
                    "type": "text",
                    "text": "Enlista detalladamente los temas que trata este documento."
                  },
                  {
                    "type": "image_url",
                    "image_url": {
                      "url": f"data:image/jpeg;base64,{image}"
                    }
                  }
                ]
              }
            ],
            max_tokens=600,
        )
        
        text_description.append(response.choices[0].message.content)

    str_text = ""

    for text_page in text_description:
        str_text += text_page
    
    print(f"FOR TEXT {doc_path}")
    print(str_text)
    print("------------------------")

    return str_text

'''
Prompt 01: Describe lo que dice y muestra la imagen.
Prompt 02: Describe la siguiente imagen haciendo énfasis en los puntos claves que toca.
Prompt 03: Enlista detalladamente los temas que trata este documento.
Prompt 04: Prepara este documento para que sea más útil para una búsqueda semántica.
Prompt 05: Enlista detalladamente los temas que trata este documento. Si encuentras algún término en otro idioma, escribelo de la siguiente manera (idioma original/traducido)
'''