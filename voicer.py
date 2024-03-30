import gtts
import speech_recognition as sr
from gtts import gTTS
import os
from playsound import playsound
import time
from training import Trainer
import numpy
import random

main = Trainer()
def chat(data):
    results = main.model.predict([main.bag_of_words(data,main.words)])[0]
    results_index=numpy.argmax(results)
    print(f"Accuracy {results[results_index]}")
    if results[results_index] > main.threshold:
        tag = main.labels[results_index]
        for t in main.intents["intents"]:
            if t["tag"] == tag:
                responses= t["responses"]
        got = random.choice(responses)
        
    else:
        got = "I did not get that"
        tag = "opt"
    if tag == "time":
        got = time.strftime("%H:%M:%S", time.localtime())
    return got,tag
