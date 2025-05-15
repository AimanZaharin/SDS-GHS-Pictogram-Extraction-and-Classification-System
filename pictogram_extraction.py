import os
import fitz
import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator # type: ignore
from ultralytics import YOLO
    
def pdf_to_images(pdf_path, output_folder="pdf_to_images/"):
    os.makedirs(output_folder, exist_ok=True)
    pdf_document = fitz.open(pdf_path)

    for i, page in enumerate(pdf_document):
        pix = page.get_pixmap(matrix = fitz.Matrix(5, 5))
        img_path = os.path.join(output_folder, f"page_{i+1}.png")
        pix.save(img_path)

def extract_sds_pictograms(output_folder="extracted_pictograms/", image_folder="pdf_to_images/"):

    cnn_model = tf.keras.models.load_model(r"creation of models notebook - training\training_cnn\sds_pictogram_cnn_classifier_model.h5")
    dataset_path = r"creation of models notebook - training\training_cnn\sds_pictogram_dataset"

    datagen = ImageDataGenerator(
    rescale=1./255
    )
    
    train_generator = datagen.flow_from_directory(
        dataset_path,
        target_size=(128, 128), 
        batch_size=32,
        class_mode="categorical",
        subset="training"
    )
    
    yolo_model = YOLO(r'creation of models notebook - training\training_yolo\runs\detect\train2\weights\best.pt')

    min_width, min_height = 20, 20
    max_width, max_height = 500, 500

    image_files = [f for f in os.listdir(image_folder) if f.endswith(".png")]

    for image_file in image_files:
        image_path = os.path.join(image_folder, image_file)
        image = cv2.imread(image_path)

        results = yolo_model(image_path)
        seen_classes = set()

        for i, box in enumerate(results[0].boxes):
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            width = x2 - x1
            height = y2 - y1

            if width < min_width or height < min_height:
                continue
            if width > max_width or height > max_height:
                continue

            cropped_pictogram = image[y1:y2, x1:x2]

            img_array = cv2.resize(cropped_pictogram, (128, 128)).astype('float32') / 255.0
            img_array = np.expand_dims(img_array, axis=0)  

            prediction = cnn_model.predict(img_array)
            confidence_score = np.max(prediction)
            class_idx = np.argmax(prediction)
            class_label = list(train_generator.class_indices.keys())[class_idx]

            if class_label != "unknown" and confidence_score >= 0.5 and class_label not in seen_classes:
                base_name = os.path.splitext(image_file)[0]
                output_path = os.path.join(output_folder, f"{base_name}_pictogram_{i}.png")
                cv2.imwrite(output_path, cropped_pictogram)
                seen_classes.add(class_label)

def classify_pictogram(img_path):
    
    dataset_path = r"creation of models notebook - training\training_cnn\sds_pictogram_dataset"  
    model = tf.keras.models.load_model(r"creation of models notebook - training\training_cnn\sds_pictogram_cnn_classifier_model.h5")
    
    datagen = ImageDataGenerator(
    rescale=1./255
    )
    
    train_generator = datagen.flow_from_directory(
        dataset_path,
        target_size=(128, 128), 
        batch_size=32,
        class_mode="categorical",
        subset="training"
    )
    
    img = cv2.imread(img_path) 
    img = cv2.resize(img, (128, 128)).astype('float32') / 255.0 
    img_array = np.expand_dims(img, axis=0)  

    prediction = model.predict(img_array)
    class_idx = np.argmax(prediction)
    class_label = list(train_generator.class_indices.keys())[class_idx]
    
    return class_label
