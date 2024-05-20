import tensorflow as tf
import tensorflow_hub as hub
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import pandas as pd
import os
from sklearn.model_selection import train_test_split


dataset_dir = 'color_dataset'
image_files = [f for f in os.listdir(dataset_dir) if f.endswith('.png')]
labels = [f.split('_')[:3] for f in image_files]  

df = pd.DataFrame({'filename': image_files, 'label': labels})

train_df, valid_df = train_test_split(df, test_size=0.2, random_state=42)

input_size = (224, 224)
batch_size = 32

datagen = ImageDataGenerator(rescale=1./255)

train_generator = datagen.flow_from_dataframe(
    dataframe=train_df,
    directory=dataset_dir,
    x_col='filename',
    y_col='label',
    target_size=input_size,
    batch_size=batch_size,
    class_mode='categorical', 
    shuffle=True
)

valid_generator = datagen.flow_from_dataframe(
    dataframe=valid_df,
    directory=dataset_dir,
    x_col='filename',
    y_col='label',
    target_size=input_size,
    batch_size=batch_size,
    class_mode='categorical',
    shuffle=False
)

model_url = "https://tfhub.dev/google/tf2-preview/mobilenet_v2/classification/4"
model = tf.keras.Sequential([hub.KerasLayer(model_url)])

model.add(layers.Dense(494, activation='softmax'))

model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])

model.fit(
    train_generator,
    epochs=5,
    validation_data=valid_generator
)

model.save("tinyml_model")

converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

with open("tinyml_model.tflite", "wb") as f:
    f.write(tflite_model)
