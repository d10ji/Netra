"""
This file contains code for sampling caption using the model built (default: sample_model.h5)
It will first convert all the images from the sample_images folder into a set of VGG16 features,
and then pass the features to the trained deep-learning model and tokenizer,
and return the captions.
"""

import os
import keras
import numpy as np
import matplotlib.pyplot as plt
from pickle import load, dump
from keras.applications.vgg16 import VGG16
from PIL import *
from keras.models import Model, load_model
from os import listdir
from pickle import dump
from keras.applications.vgg16 import VGG16
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.vgg16 import preprocess_input
from keras.models import Model
import string
from numpy import array
from pickle import load
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.utils.np_utils import to_categorical
from tensorflow.keras.utils import plot_model
from keras.models import Model
from keras.layers import Input
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Embedding
from keras.layers import Dropout
from keras.layers.merge import add
from keras.callbacks import ModelCheckpoint


def feature_extractions(filename):
    """
    Input: directory of images
    Return: A dictionary of features extracted by VGG-16, size 4096.
    """

    model = keras.applications.vgg16.VGG16()
    model = keras.models.Model(inputs=model.input, outputs=model.layers[-2].output)  # Remove the final layer





    image = keras.preprocessing.image.load_img(filename, target_size=(224, 224))
    arr = keras.preprocessing.image.img_to_array(image, dtype=np.float32)
    arr = arr.reshape((1, arr.shape[0], arr.shape[1], arr.shape[2]))
    arr = keras.applications.vgg16.preprocess_input(arr)

    feature = model.predict(arr, verbose=0)



    return (feature)


def sample_caption1(model, tokenizer, max_length, vocab_size, feature):
    """
    Input: model, photo feature: shape=[1,4096]
    Return: A generated caption of that photo feature. Remove the startseq and endseq token.
    """

    caption = "startseq"
    while 1:
        # Prepare input to model
        encoded = tokenizer.texts_to_sequences([caption])[0]
        padded = keras.preprocessing.sequence.pad_sequences([encoded], maxlen=max_length, padding='pre')[0]
        padded = padded.reshape((1, max_length))

        pred_Y = model.predict([feature, padded])[0, -1, :]
        # print(type(pred_Y))
        # input("hello")
        next_word = tokenizer.index_word[pred_Y.argmax()]

        # Update caption
        caption = caption + ' ' + next_word

        # Terminate condition: caption length reaches maximum / reach endseq
        if next_word == 'endseq' or len(caption.split()) >= max_length:
            break

    # Remove the (startseq, endseq)
    caption = caption.replace('startseq ', '')
    caption = caption.replace(' endseq', '')

    return (caption)


# Load tokenizer
with open("captioning2/tokenizer8k.pkl", "rb") as f:
    tokenizer = load(f)

model = keras.models.load_model('captioning2/model 2.h5')  # Load model
# model = keras.models.load_model("highaccuracymodel/chnaged_model_2_concat34_epch.h5") #Load model
vocab_size = tokenizer.num_words  # The number of vocabulary
max_length = 33  # Maximum length of caption sequence

# sampling




def generate_caption(filename):
    feature=feature_extractions(filename)
    caption = sample_caption1(model, tokenizer, max_length, vocab_size,feature)
    return caption

