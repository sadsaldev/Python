import pytesseract # Para extraer el texto de la imagen
from PIL import Image # Para abrir y manipular la imagen
import os

def extract_text_from_image(image_path):
    try:
        img = Image.open(image_path)
        # Usar Tesseract para extraer el texto de la imagen
        text = pytesseract.image_to_string(img)
        
        return text
    except Exception as e:
        return f'Error: {e}'
    
if __name__ == '__main__':
    while True:
        image_path = input('Introduce la ruta de la imagen de la cual quieres extraer el texto. (O escribe "salir" para terminar):')
        if image_path.lower() == 'salir':
            print('Saliendo del programa...')
            break
        
        if not os.path.isfile(image_path):
            print('La ruta de la imagen no es válida. Verifica que esté escrita correctamente o proporciona una diferente.')
            continue
        
        extracted_text = extract_text_from_image(image_path)
        print('Texto extraído de la imagen:')
        print(extracted_text)