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

```yaml
├── training/
│ ├── training_yolo/ # YOLOv8 training configs and scripts
│ │ ├── README.md
│ │ └── model_training_yolo.ipynb
│ ├── training_cnn/ # CNN model training and dataset
│ │ ├── model_training_cnn.ipynb
│ │ └── sds_pictogram_dataset/
├── .streamlit/ # Streamlit app config
│ └── config.toml
├── .gitignore
├── main.py # Streamlit UI interface code
├── pictogram_extraction.py # Backend: PDF to image conversion, extraction, classification
├── requirements.txt # Project dependencies
└── README.md # ← You are here
```

---

## 🗂️ Dataset and Privacy

- The dataset used contains sensitive information and **is not included** in this repository.
- Dataset structure and configuration files are provided to enable training with your own data.

---

## 📦 Installation

1. Clone this repository:

```bash
git clone https://github.com/AimanZaharin/SDS-GHS-Pictogram-Extraction-and-Classification-System.git
cd SDS-GHS-Pictogram-Extraction-and-Classification-System
```

2. Create and activate a Python virtual environment (recommended):

- On macOS/Linux:
``
python3 -m venv venv-sds
source venv/bin/activate
``

- On Windows (PowerShell):
```powershell
python -m venv venv-sds
.\venv\Scripts\Activate.ps1
```

- On Windows (cmd):
```cmd
python -m venv venv-sds
.\venv\Scripts\activate.bat
```
3. Install the project dependencies:

``
pip install -r requirements.txt
``

## 🏁 Usage

- To train or fine-tune the YOLOv8 detection model, refer to "creation of models notebook - training\training_yolo\README.md". 
- To train or evaluate the CNN classifier, refer to "creation of models notebook - training\training_cnn\model_training_cnn".ipynb.
- To run the Streamlit web interface:
``
streamlit run main.py
``

## 📌 Key GHS Pictogram Classes

- Explosive
- Flammable
- Oxidizer
- Gas under pressure
- Corrosive
- Toxic
- Irritant
- Health Hazard
- Environmental Hazard
