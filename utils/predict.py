import os
import csv
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image

# Load model name from CSV
def get_best_model_name():
    csv_path = os.path.join('best_model', 'best_model_name.csv')
    with open(csv_path, mode='r') as file:
        reader = csv.reader(file)
        header = next(reader) 
        if len(header) < 2:
            raise ValueError("CSV file doesn't contain a model name in the expected format.")
        return header[1] 


# Class labels
class_names = [
    'animal fish',
    'animal fish bass',
    'fish sea_food black_sea_sprat', 
    'fish sea_food gilt_head_bream',
    'fish sea_food hourse_mackerel',
    'fish sea_food red_mullet',
    'fish sea_food red_sea_bream',
    'fish sea_food sea_bass',
    'fish sea_food shrimp',
    'fish sea_food striped_red_mullet',
    'fish sea_food trout'
]

# Prediction function
def load_model_and_predict(image: Image.Image):

    # Load the model dynamically
    model_name = get_best_model_name()
    print(f"Loading model: {model_name}")
    model_path = os.path.join('models', f'{model_name}_fish_model.h5')
    print(f"Model path: {model_path}")
    model = load_model(model_path)

    image = image.resize((224, 224))
    image = img_to_array(image)
    image = image / 255.0
    image = np.expand_dims(image, axis=0)
    
    predictions = model.predict(image)
    top_class = np.argmax(predictions)
    confidence = np.max(predictions)
    
    return class_names[top_class], confidence, model_name  
