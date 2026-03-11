import os
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.optimizers import Adam

# ============================
# Dataset Path
# ============================

dataset_path = r"C:\Users\thipp\OneDrive\Documents\insect_damage_detection\dataset"

# ============================
# Image Parameters
# ============================

IMG_SIZE = (224, 224)
BATCH_SIZE = 16
EPOCHS = 10

# ============================
# Data Generator
# ============================

datagen = ImageDataGenerator(
    rescale=1./255,
    validation_split=0.2,
    rotation_range=20,
    zoom_range=0.2,
    horizontal_flip=True
)

train_data = datagen.flow_from_directory(
    dataset_path,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='categorical',
    subset='training'
)

val_data = datagen.flow_from_directory(
    dataset_path,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='categorical',
    subset='validation'
)

# ============================
# Load Pretrained Model
# ============================

base_model = MobileNetV2(
    weights='imagenet',
    include_top=False,
    input_shape=(224, 224, 3)
)

# Freeze base layers
for layer in base_model.layers:
    layer.trainable = False

# ============================
# Custom Classification Layers
# ============================

x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(128, activation='relu')(x)
predictions = Dense(3, activation='softmax')(x)

model = Model(inputs=base_model.input, outputs=predictions)

# ============================
# Compile Model
# ============================

model.compile(
    optimizer=Adam(learning_rate=0.0001),
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# ============================
# Train Model
# ============================

print("Training started...")

history = model.fit(
    train_data,
    validation_data=val_data,
    epochs=EPOCHS
)

# ============================
# Save Model
# ============================

model_path = "models/insect_damage_model.h5"
model.save(model_path)

print("Training completed!")
print("Model saved at:", model_path)