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
> https://drive.google.com/drive/folders/1iKdOs4slf3XvNWkeSfsszhPRggfJ2qEd?usp=sharing
>
> refer this link for dataset

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

## Addons
## Dockerization and Deployment

Dockerized the Streamlit app and deployed it on an Amazon EC2 instance running Amazon Linux.  Configured security groups to expose port 8501 and accessed the app via the instance's public IP.

To ensure platform-independent and scalable deployment, the Streamlit app was containerized using Docker and deployed on an AWS EC2 instance (Amazon Linux) using SSH.

### Steps Followed:
 
#### Step-1️ SSH into AWS EC2 Instance
 
Connected securely to the EC2 instance using a private key:
```bash
ssh -i "C:/path/to/your/.pem file" ec2-user@<your-ec2-public-ip>
```
 
#### Step-2 Transferred Project Files
 
Used SCP to transfer necessary project files (model, app, Dockerfile, etc.) from local machine to EC2:
```bash
scp -i "C:/path/to/your/.pem file" -r \
"C:/path/to/your/streamilt .py file" \
"C:/path/to/Dockerfile file" \
"C:/path/to/models folder" \
"C:/path/to/best_model folder" \
"C:/path/to/utils folder" \
"C:/path/to/requirements.txt file" \
ec2-user@<your-ec2-public-ip>
```
 
#### Step-3 Built Docker Image on EC2
 
Navigated into the app directory and built the image:
```bash
docker build -t fish-image-streamlit-app .
 
```
 
#### Step-4 Ran Docker Container
 
Exposed the app on port 8501 (Streamlit’s default port):
```bash
docker run -d -p 8501:8501 fish-image-streamlit-app .
```
 
Checked container status using:
```bash
docker ps
```
 
#### Step-5 Access the Web App
 
The deployed Streamlit app was accessible via:
```bash
http://<your-ec2-public-ip>:8501
 
```


