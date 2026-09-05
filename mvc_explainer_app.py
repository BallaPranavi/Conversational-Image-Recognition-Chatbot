import os
import streamlit as st
from PIL import Image
from dotenv import load_dotenv
from transformers import pipeline
from transformers import BlipProcessor, BlipForConditionalGeneration

# Load environment variables
load_dotenv()
HF_API_KEY = os.getenv("HUGGINGFACE_API_KEY")

# ✅ Set page config
st.set_page_config(page_title="🧠 Image Explainer and Q&A", layout="centered")

st.title("🧠 Image Explainer and  Q&A")
st.write("Upload an diagram and ask any related question.")

# ✅ Load captioning model (BLIP)
@st.cache_resource
def load_caption_model():
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    return processor, model

# ✅ Load Hugging Face FLAN-T5 pipeline
@st.cache_resource
def load_flan_pipeline():
    return pipeline(
        "text2text-generation",
        model="google/flan-t5-large",
        tokenizer="google/flan-t5-large"
    )

processor, blip_model = load_caption_model()
flan_pipeline = load_flan_pipeline()

# 📤 Upload image
uploaded = st.file_uploader("📤 Upload an  diagram", type=["jpg", "jpeg", "png"])
if uploaded:
    image = Image.open(uploaded).convert("RGB")
    st.image(image, caption="Uploaded Diagram", use_container_width=True)

    # Generate caption from image
    with st.spinner("Analyzing diagram..."):
        inputs = processor(images=image, return_tensors="pt")
        out = blip_model.generate(**inputs)
        caption = processor.decode(out[0], skip_special_tokens=True)

    st.success("📋 Diagram Summary:")
    st.write(caption)

    # Ask a question
    st.markdown("### 🤖 Ask a question about the diagram:")
    user_question = st.text_input("Your question")

    if user_question:
        with st.spinner("💡 Thinking..."):
            prompt = f"Here is a diagram caption: {caption}. Question: {user_question}"
            response = flan_pipeline(prompt, max_new_tokens=200)[0]['generated_text']
        st.markdown(f"**Answer:** {response}")
