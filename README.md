# SDS GHS Pictogram Extraction and Classification System

This project develops a **computer vision pipeline** to automatically **extract** and **classify** GHS (Globally Harmonized System) safety pictograms from Safety Data Sheets (SDS).

---

## 🚀 Project Overview

- Utilizes **YOLOv8** and **OpenCV** to detect and extract pictograms from complex PDF documents with high accuracy.
- Designed and trained a **Convolutional Neural Network (CNN)** using TensorFlow/Keras to classify extracted pictograms into their respective GHS categories.
- Integrated the full pipeline into an interactive **Streamlit** web interface that allows easy upload of SDS documents and visualization of results.

This system aims to improve efficiency and accuracy in **safety compliance workflows**, automating hazard identification in industrial environments.

---

## 🧠 Approach

1. **PDF Processing**  
   Converts SDS PDFs into images using PyMuPDF (`fitz`).

2. **Pictogram Extraction**  
   Uses OpenCV-based image processing and YOLOv8 object detection to locate and extract pictograms from the SDS pages.

3. **Classification**  
   Applies a CNN model to classify each extracted pictogram into standard GHS hazard categories.

4. **User Interface**  
   Streamlit app for uploading SDS PDFs and visualizing detection and classification results interactively.

---

## 📁 Repository Structure
