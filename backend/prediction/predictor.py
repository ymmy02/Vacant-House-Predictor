from typing import Tuple
from django.conf import settings
import PIL
import numpy as np
from keras.models import load_model

def predict(house_image: PIL.Image.Image) -> Tuple[float, float]:
    np_image = convert_pilimage_to_nparray(house_image)
    (occupied_pct, vacant_pct) = predict_by_cnn_keras(np_image)
    return occupied_pct, vacant_pct

def convert_pilimage_to_nparray(pil_image: PIL.Image.Image) -> np.array:
    NUM_RGB = 3
    IMG_WIDTH, IMG_HEIGHT = 150, 150
    SCALE = 255
    np_image = np.array(pil_image.resize((IMG_WIDTH, IMG_HEIGHT))) / SCALE
    return np_image.reshape((1, IMG_WIDTH, IMG_HEIGHT, NUM_RGB))

def predict_by_cnn_keras(np_image) -> Tuple[float, float]:
    model = load_model(settings.MLMODEL_ROOT + '/cnn_keras.h5')
    vacant_rate = model.predict_proba(np_image)[0][0]
    vacant_pct = vacant_rate * 100
    occupied_pct = 100 - vacant_pct
    return occupied_pct, vacant_pct

