﻿# Document Data Extraction Web Application
This project is a document data extraction web application built with Flask for the backend and React for the frontend. It extracts key information (name, document number, and expiration date) from uploaded document images, such as passports or driver’s licenses, using OCR (Optical Character Recognition) with the Tesseract engine. The app features a modern UI with animations, responsive feedback, and error handling.

Features
Document Upload: Users can upload an image of a document from the frontend.
OCR Data Extraction: Utilizes Tesseract OCR to read text from images.
Regex-Based Extraction: Extracts name, document number, and expiration date from the OCR output using flexible regex patterns.
User-Friendly UI: Includes animations, loading indicators, and error messages to enhance user experience.
Backend-Frontend Integration: Flask serves as the backend for OCR and data extraction, while React handles the frontend interface and API calls.
Tech Stack
Frontend: React, Framer Motion (for animations), Axios (for API calls)
Backend: Flask, Tesseract OCR, Python Imaging Library (Pillow)
Proxy: Configured in React to forward API requests to Flask backend
Styling: Custom CSS with gradient background, styled form elements, and responsive layout
Getting Started
Prerequisites
Node.js and npm installed on your machine.

Python 3 and pip installed.

Tesseract OCR installed on your computer.

Tesseract Installation Guide for different operating systems.
Make sure to add the Tesseract installation path to your system environment variables.

Access the App:

Open a web browser and go to http://localhost:3000 to interact with the frontend.
The Flask backend will run on http://127.0.0.1:5000.
Usage
Upload a Document:

Click "Upload Document" to choose an image file of a document (e.g., passport, driver’s license).
The file should contain text matching the expected format (name, document number, expiration date).
View Extracted Data:

Once the document is uploaded, OCR will extract the relevant fields, which will be displayed in the frontend.
Error Handling:

If any data cannot be extracted, an error or partial data message will be displayed.
Project Structure
Backend: The app.py file contains the Flask application for handling OCR processing and API requests.
Frontend: The App.js component in the frontend folder handles the UI, animations, and API requests.
Static Files: App.css contains the styling for the React frontend.
Dependencies:
Framer Motion is used for animations.
Axios is used for making HTTP requests.
Pillow and pytesseract handle image processing and OCR on the backend.
Troubleshooting
CORS Error: Make sure Flask-CORS is installed and properly configured to allow React to make requests to Flask.
Tesseract Path Error: Ensure the tesseract_cmd variable in app.py points to your Tesseract installation directory.
OCR Accuracy: OCR might struggle with low-quality images. Ensure images are clear and high-resolution for best results.
Future Improvements
Add support for more document types.
Enhance regex patterns to handle a wider variety of text formats.
Implement pagination and history of uploads in the frontend.
Add localization for better multi-language support.
License
This project is licensed under the MIT License. See the LICENSE file for details.
