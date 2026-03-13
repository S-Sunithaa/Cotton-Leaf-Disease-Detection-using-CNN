import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from django.conf import settings
import numpy as np  
from PIL import Image
import os

def predict(image_path):
    
    path=settings.MEDIA_ROOT + '//' +'leaf.h5'
    model_load =load_model(filepath=path)
    img_size = 64
    classes=["diseased_leaf","diseased_plant","fresh_leaf","fresh_plant"] 
    test_image=image.load_img(image_path, target_size =(img_size,img_size) )
    plt.imshow(test_image)
    test_image = np.expand_dims(test_image, axis = 0)
    preds=np.argmax(model_load.predict(test_image))
    return (f"The Leaf  is {classes[preds]}")