# Multiclass Fish Image Classification

This project focuses on classifying fish images into multiple categories using deep learning. A custom CNN model and five transfer learning architectures were implemented, evaluated, and compared. The best-performing model was deployed using Streamlit for real-time fish species prediction.

---

## Project Highlights

- Image classification of fish species using CNN and transfer learning.
- Models used: **CNN**, **VGG16**, **ResNet50**, **MobileNetV2**, **InceptionV3**, **EfficientNetB0**.
- Metrics evaluated: Accuracy, Precision, Recall, F1-Score.
- Data imbalance handled via **targeted augmentation** (e.g., for `animal fish bass`).
- **Streamlit App** for user-friendly real-time prediction.

---

## Dataset

- Fish images categorized by species.
- Train, Validation, and Test sets organized in folders.
- Loaded using `ImageDataGenerator` with strong data augmentation.

> 📌 **Note:**  
> To access the dataset used in this project, refer to the file:  
> `requirements_docs/Multiclass_Image_Classification.pdf`  or `requirements_docs/Multiclass_Image_Classification.docx`

> This document contains the dataset download link and related instructions.

---

## Methodology

### Data Preprocessing & Augmentation
- Applied rescaling, flipping, rotation, brightness adjustments, etc.
- Targeted augmentation applied to minority class `animal fish bass`.

### Model Development
- Built a custom CNN using Keras.
- Implemented 5 transfer learning models with fine-tuning.
- Trained using early stopping and class weights for balance.

### Evaluation
- Metrics: Accuracy, Precision, Recall, F1-Score, Confusion Matrix.
- Plotted training/validation accuracy & loss graphs.
- Best model selected using **F1-Score**.

### Model Comparison

| Model             | Accuracy | Precision | Recall   | F1-Score |
|------------------|----------|-----------|----------|----------|
| **MobileNetV2**     | 0.995921 | 0.995804  | 0.995921 | 0.995755 |
| **InceptionV3**     | 0.994980 | 0.995512  | 0.994980 | 0.995149 |
| **VGG16**           | 0.976467 | 0.977326  | 0.976467 | 0.976737 |
| **CNN (Scratch)**   | 0.974584 | 0.975916  | 0.974584 | 0.974480 |
| **ResNet50**        | 0.325698 | 0.379563  | 0.325698 | 0.292473 |
| **EfficientNetB0**  | 0.004079 | 0.000017  | 0.004079 | 0.000033 |


> MobileNetV2 showed the highest performance across all metrics and was selected as the best model for deployment.  
> InceptionV3 and VGG16 also performed strongly.  
> ResNet50 and EfficientNetB0 struggled with this dataset and may require further tuning or preprocessing adjustments.

---

## Streamlit App

1. **Upload** a fish image (JPG, JPEG, PNG).
2. Click **Predict** to view the species and confidence score.
3. Click **Reset** to clear results and upload a new image.

![image](https://github.com/user-attachments/assets/d7a96ae7-ce01-46f4-9567-b5f5de80ed0d)

---

