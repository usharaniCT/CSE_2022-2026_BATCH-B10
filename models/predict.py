import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

model = load_model("models/insect_model.h5")

classes = ["normal", "moderate", "severe"]

def predict_image(img_path):

    img = image.load_img(img_path, target_size=(224,224))
    img = image.img_to_array(img)
    img = img/255.0
    img = np.expand_dims(img, axis=0)

    prediction = model.predict(img)

    result_index = np.argmax(prediction)

    result = classes[result_index]

    prob = prediction[0]   # <-- this gives 3 probabilities

    return result, prob
    send_detection_email(
    session["user"],
    path,
    result,
    suggestions
)