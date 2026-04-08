import numpy as np
import random

classes = ["normal", "moderate", "severe"]

def predict_image(img_path):
    # Dummy prediction (for deployment/demo)
    result = random.choice(classes)

    # Fake probabilities
    prob = np.array([0.2, 0.5, 0.3])

    return result, prob
