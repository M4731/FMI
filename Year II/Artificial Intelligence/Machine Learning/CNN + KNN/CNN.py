import numpy as np
import pandas as pd
from tensorflow import keras
from matplotlib.image import imread
from sklearn.metrics import confusion_matrix

import os
os.environ['TF_FORCE_GPU_ALLOW_GROWTH'] = 'true'

f = open("train.txt", 'r')
v_imagini = []
v_indici = [] #label

for i in f:
    image = imread(f"train/{i.split(',')[0]}")
    image = list(image)
    indice = int(i.split(',')[1].split()[0])
    v_imagini.append(image)
    v_indici.append(indice)
    # print(type(image))
f.close()
v_indici = keras.utils.to_categorical(v_indici)

f = open("validation.txt", 'r')
v_imagini_validare = []
v_indici_validare = [] #label

for i in f:
    image = imread(f"validation/{i.split(',')[0]}")
    indice = int(i.split(',')[1].split()[0])
    v_imagini_validare.append(image)
    v_indici_validare.append(indice)
f.close()
pentru_matrice = v_indici_validare.copy()
v_indici_validare = keras.utils.to_categorical(v_indici_validare)

v_imagini = np.asarray(v_imagini)
v_imagini = v_imagini.reshape(v_imagini.shape[0], 32, 32, 1)

v_imagini_validare = np.asarray(v_imagini_validare)
v_imagini_validare = v_imagini_validare.reshape(v_imagini_validare.shape[0], 32, 32, 1)

model = keras.models.Sequential() #creem obiectul model 
model.add(keras.layers.Input((32, 32, 1))) #instantiem modelul cu un input de 32x32 pixeli si greyscale
model.add(keras.layers.BatchNormalization()) #normalizam modelul pe batch

model.add(keras.layers.Conv2D(600, 5, activation='relu'))
model.add(keras.layers.Conv2D(600, 5, activation='relu'))
model.add(keras.layers.MaxPool2D())
model.add(keras.layers.Dropout(0.4))

model.add(keras.layers.Flatten())
model.add(keras.layers.Dense(350, activation='relu'))
model.add(keras.layers.Dense(350, activation='relu'))

model.add(keras.layers.Dropout(0.4))

model.add(keras.layers.Dense(9, activation='softmax'))

model.compile(optimizer="adamax", loss="categorical_crossentropy", metrics=["acc"])

# print(v_imagini.shape)
# print(model.summary())

model.fit(v_imagini, v_indici, epochs=30, verbose=2, validation_data=(
    v_imagini_validare, v_indici_validare), use_multiprocessing=True, batch_size=64)

    
f = open("test.txt", 'r')
v_imagini_test = []
v_path = []

for i in f:
    image = imread(f"test/{i.split()[0]}")
    image = list(image)
    v_imagini_test.append(image)
    v_path.append(i.split()[0])
f.close()

v_imagini_test = np.asarray(v_imagini_test)
v_imagini_test = v_imagini_test.reshape(v_imagini_test.shape[0], 32, 32, 1)

predictii = model.predict_classes(v_imagini_test)

# print(len(v_path))
# print(len(predictii))

# print(predictii)
o = {"id" : v_path,'label' : predictii}
output = pd.DataFrame(data=o)

output = output.set_index("id")
# print(output)

output.to_csv("output_final.csv")


predictii_cm = model.predict_classes(v_imagini_validare)
cm = confusion_matrix(pentru_matrice, predictii_cm)
print(cm)