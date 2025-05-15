import os
import streamlit as st
from pictogram_extraction import pdf_to_images, extract_sds_pictograms, classify_pictogram

# Streamlit UI
st.set_page_config(
    page_title="Pictogram Detector",
    page_icon='⚠️',
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        'About': "Created by *Aiman Zaharin*"
    }
)

st.title("⚠️ Pictogram Detection")

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if not uploaded_file:
    submit_button = st.button("Detect Pictograms", type="primary", disabled=True)

else:
    submit_button = st.button("Detect Pictograms", type="primary")

if submit_button:
    if not os.path.exists("uploads"):
        os.makedirs("uploads")

    # Delete any existing files in the "uploads" folder
    for file in os.listdir("uploads"):
        file_path = os.path.join("uploads", file)
        if os.path.isfile(file_path):
            os.remove(file_path)
    
    # Delete any existing files in the "pdf_to_images" folder
    if os.path.exists("pdf_to_images"):
        for file in os.listdir("pdf_to_images"):
            file_path = os.path.join("pdf_to_images", file)
            if os.path.isfile(file_path):
                os.remove(file_path)
            
    # Delete any existing files in the "extracted_pictograms" folder
    if os.path.exists("extracted_pictograms"):
        for file in os.listdir("extracted_pictograms"):
            file_path = os.path.join("extracted_pictograms", file)
            if os.path.isfile(file_path):
                os.remove(file_path)
    
    with open(f"uploads/{uploaded_file.name}", "wb") as f:
        f.write(uploaded_file.read())

    upload_path = f"uploads/{uploaded_file.name}"

    #TODO
    # Convert the PDFs to images
    # Extract the pictograms from the images
    try:
        pdf_to_images(upload_path)
        extract_sds_pictograms()
    except ValueError as e:
        st.error(e)

    # Identify pictograms in extracted images
    extracted_images_folder = "extracted_pictograms/"
    table_gap = [0.5, 2] 

    img_1, label = st.columns(table_gap)

    with img_1:
        st.write("#### **Extracted Image**")

    with label:
        st.write("#### **Warning Label**")

    for img_file in os.listdir(extracted_images_folder):
        if img_file.endswith((".png", ".jpg")):
            img_path = os.path.join(extracted_images_folder, img_file)
            result = classify_pictogram(img_path)  # ✅ fixed typo here

            col1, col2 = st.columns([0.5, 2])  # You can tweak the ratio

            with col1:
                st.image(img_path, width=150)

            with col2:
                st.write(f"**{result}**")
