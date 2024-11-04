from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
import pytesseract
from PIL import Image
import re
from io import BytesIO
import datetime

app = Flask(__name__)
CORS(app)  # Enable CORS for the whole app

# Set the Tesseract OCR path (adjust based on installation location)
pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"

# Home route for testing
@app.route('/')
def home():
    return "Welcome to the Document Data Extraction API. Use the /upload endpoint to upload a document image."

# Function to extract data from the document
def extract_document_data(image):
    # Convert the image to grayscale for better OCR accuracy
    image = image.convert('L')
    image = image.point(lambda x: 0 if x < 128 else 255, '1')  # Increase contrast
    
    # OCR processing
    text = pytesseract.image_to_string(image)
    print("OCR Output:\n", text)  # Print OCR output for debugging purposes

    # Generalized regex patterns for name, document number, and expiration date
    name_pattern = r'\bName:\s*([A-Z]+(?:\s[A-Z]+)*)'
    doc_number_pattern = r'([A-Z]{2}\d{2} \d{11})'
    date_pattern = r'\b(\d{1,2}-\d{1,2}-\d{4})\b'
    
    # Extracting data using regex
    name = re.search(name_pattern, text)
    document_number = re.search(doc_number_pattern, text)

    # Extract all date matches
    date_matches = re.findall(date_pattern, text)
    dates = []

    # Convert each date match to a datetime object, if possible
    for date_str in date_matches:
        try:
            date_obj = datetime.datetime.strptime(date_str, "%d-%m-%Y")
            dates.append(date_obj)
        except ValueError:
            continue

    # Find the most futuristic date if dates were found
    expiration_date = max(dates).strftime("%d-%m-%Y") if dates else None

    clean_name = name.group(1).strip() if name else None
    if clean_name:
        # Remove any non-uppercase letters and spaces
        clean_name = re.sub(r'[^A-Z\s]', '', clean_name)
        # Remove trailing whitespace followed by a single letter
        clean_name = re.sub(r'\s+[A-Z]$', '', clean_name)

    return {
        "name": clean_name,
        "document_number": document_number.group(1).strip() if document_number else None,
        "expiration_date": expiration_date
    }

# API endpoint for uploading and processing the document image
@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    image = Image.open(BytesIO(file.read()))

    data = extract_document_data(image)

    # Check for incomplete extraction
    if not all(data.values()):
        return jsonify({"warning": "Some fields could not be extracted", "data": data}), 206

    return jsonify(data), 200

if __name__ == '__main__':
    app.run(debug=True)
