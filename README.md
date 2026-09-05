# Conversational Image Recognition Chatbot

A Streamlit-based AI application that allows users to upload a diagram or image, automatically generate a description of the image, and ask questions about it using natural language.

## Features

- Upload images in JPG, JPEG, and PNG formats
- Generate an automatic image description
- Ask questions related to the uploaded image
- Get AI-generated answers based on the image description
- Simple and interactive Streamlit interface

## Technologies Used

- Python
- Streamlit
- Hugging Face Transformers
- BLIP Image Captioning Model
- FLAN-T5 Large
- Pillow (PIL)

## How It Works

1. The user uploads an image or diagram.
2. The BLIP model analyzes the image and generates a description.
3. The user enters a question about the uploaded image.
4. FLAN-T5 processes the image description and question.
5. The application displays the generated answer.

## Project Structure

```text
Conversational-Image-Recognition-Chatbot/
│
├── mvc_explainer_app.py
├── requirements.txt
├── README.md
└── .gitignore