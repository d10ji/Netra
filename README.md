# NETRA: An Image Descriptor

Automatically generating a natural language description of an image is a **major challenging task** in the field of artificial intelligence. Generating a description of an image brings together the fields: **Natural Language Processing** and **Computer Vision**. There are two types of approaches i.e. top-down and bottom-up. In this project, we followed a top-down approach starting from extracting image features and finally generating meaningful textual description (caption) into speech form. 

In our model, firstly the fixed size of the image is passed to the pre-trained model of **Convolutional Neural Network** named (**VGG-16**) encoder that extracts the features present in the image which are then fed to **LSTM**, finally generating the meaningful captions. The model is successful in generating realistic image captions with **model accuracy** of **60.07%** and **validation accuracy** of **42.51%**.

To evaluate the model performance, we used **BLEU** (*Bilingual Evaluation Understudy*) score and matched predicted words to the original caption. Our model scored **BLEU-1**, **BLEU-2**, **BLEU-3**, **BLEU-4** as **0.43**, **0.25**, **0.18**, **0.09** respectively.

**Keywords:** <span style="color:blue">Natural Language Processing</span>, <span style="color:green">Computer Vision</span>, <span style="color:red">Convolutional Neural Network</span>, <span style="color:orange">Recurrent Neural Network</span>, <span style="color:purple">LSTM</span>, <span style="color:brown">BLEU</span>.
