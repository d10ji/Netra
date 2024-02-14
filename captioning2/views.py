from django.shortcuts import render
from captioning2.models import image
import pyttsx3
import numpy as np
import keras
from keras.applications.vgg16 import VGG16
# Create your views here.
import tensorflow
from netra.settings import modelv,model,tokenizer

vocab_size = tokenizer.num_words  # The number of vocabulary
max_length = 33

def index_page(request):

    return render(request,'index.html',)

def clicking_on_predict_caption(request):
    form=image()
    form.IMAGE=request.FILES['input_file']
    form.save()
    a=image.objects.get(id=form.id)
    print(a.IMAGE.url)



    ###################################################







    print("="*50)
    print("IMAGE SAVED")



    imagename=str(a.IMAGE.url)[1:]
    #input(a.IMAGE.url.split("/")[-1].split(".")[0])
    img = keras.preprocessing.image.load_img(imagename, target_size=(224, 224))
    arr = keras.preprocessing.image.img_to_array(img, dtype=np.float32)
    arr = arr.reshape((1, arr.shape[0], arr.shape[1], arr.shape[2]))
    arr = tensorflow.keras.applications.vgg16.preprocess_input(arr)

    feature = modelv.predict(arr, verbose=0)

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
    #caption= generate_caption(imagename)
    print(caption,"caption2")


    mp3_name="static/{imagefilename}.mp3".format(imagefilename=a.IMAGE.url.split("/")[-1].split(".")[0])
    #tts.save(mp3_name)
    ####################################################


    # Create a string
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("rate", 150)
    engine.setProperty("voice", voices[0].id)
    engine.save_to_file(caption, mp3_name)
    engine.runAndWait()



    print("bhuwan")
    print(form.IMAGE)
    context={
        'a':a,
        'mp3':mp3_name,
        "caption":caption
    }
    return render(request,'caption.html',context)




