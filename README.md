# Conversational Image Recognition Chatbot

An AI-powered conversational image recognition application built with Python and Streamlit. The application allows users to upload an image or diagram, automatically generate an image description, and ask questions about the uploaded image using natural language.

## Features

- Upload images in JPG, JPEG, and PNG formats
- Automatically generate image descriptions
- Ask natural-language questions about uploaded images
- Generate AI-powered answers based on the image content
- Simple and interactive Streamlit interface
- Supports image understanding and conversational interaction

## Technologies Used

- **Python** – Core programming language
- **Streamlit** – Interactive web application framework
- **Hugging Face Transformers** – AI model integration
- **BLIP** – Image captioning and image description
- **FLAN-T5 Large** – Natural language question answering
- **Pillow (PIL)** – Image processing and handling

## How It Works

1. The user uploads an image or diagram.
2. The **BLIP image captioning model** analyzes the image and generates a description.
3. The user enters a question related to the uploaded image.
4. The **FLAN-T5 Large model** processes the image description along with the user's question.
5. The application generates and displays an AI-powered answer.

## Project Structure

```text
Conversational-Image-Recognition-Chatbot/
│
├── mvc_explainer_app.py
├── requirements.txt
├── README.md
├── .gitignore
├── .gitattributes
└── venv/
