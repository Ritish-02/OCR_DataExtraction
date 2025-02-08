import cv2
import pytesseract
import pdf2image
from preprocess import preprocess_image
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
def extract_text_from_image(image_path):
    image = preprocess_image(image_path)
    text = pytesseract.image_to_string(image)
    return text
def extract_text_from_pdf(pdf_path):
    images = pdf2image.convert_from_path(pdf_path)
    extracted_text = ""
    for img in images:
        img.save("temp.jpg","JPEG")
        extracted_text+=extract_text_from_image("temp.jpg")
    return extracted_text
