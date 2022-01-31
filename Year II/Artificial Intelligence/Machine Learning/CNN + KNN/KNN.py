import numpy as np
import pandas as pd
from matplotlib.image import imread
from sklearn.neighbors import KNeighborsClassifier
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

f = open("validation.txt", 'r')
v_imagini_validare = []
v_indici_validare = [] #label

for i in f:
    image = imread(f"validation/{i.split(',')[0]}")
    indice = int(i.split(',')[1].split()[0])
    v_imagini_validare.append(image)
    v_indici_validare.append(indice)
f.close()

v_imagini = np.asarray(v_imagini)
v_imagini = v_imagini.reshape(v_imagini.shape[0], (32*32))

pentru_matrice = v_indici_validare.copy()
v_imagini_validare = np.asarray(v_imagini_validare)
v_imagini_validare = v_imagini_validare.reshape(v_imagini_validare.shape[0], (32*32))

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
v_imagini_test = v_imagini_test.reshape(v_imagini_test.shape[0], (32*32))

neigh = KNeighborsClassifier(n_neighbors = 9)
neigh.fit(v_imagini, v_indici)
print(neigh.score(v_imagini_validare,v_indici_validare))

predictii_cm = neigh.predict(v_imagini_validare)
cm = confusion_matrix(pentru_matrice, predictii_cm)
print("sdadssa")
print(cm)