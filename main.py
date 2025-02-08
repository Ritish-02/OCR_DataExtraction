import json
import os
from ocr import extract_text_from_image,extract_text_from_pdf
from extract_data import extract_fields
from database import insert_data
def process_file(file_path):
    if file_path.lower().endswith('.pdf'):
        raw_text = extract_text_from_pdf(file_path)
    else:
        raw_text = extract_text_from_image(file_path)
    structured_data = extract_fields(raw_text)
    json_output = json.dumps(structured_data,indent=4)
    with open("output.json","w") as f:
        f.write(json_output)
    print("Data extracted and saved to output.json")
    insert_data(structured_data)
    print("Data inserted into MYSQL database")
if __name__ == "__main__":
    file_path = r"D:\OCR\sample_data\form_sample.jpg"
    process_file(file_path)