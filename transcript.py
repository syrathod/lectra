import whisper
import speech_recognition as sr
import numpy as np
import io
import soundfile as sf
import warnings
import os
import datetime

warnings.simplefilter(action='ignore', category=FutureWarning)

class transcriber:
    def transcribe():
        data_dir = os.path.join("./data")
        log_dir = os.path.join("./logs")

        model = whisper.load_model("small.en")
        recognizer = sr.Recognizer()

        log_created_at = datetime.datetime.now().strftime("%d-%m-%Y--%H-%M-%S")
        log_file =  open(f"./logs/{log_created_at}.txt", "x")
        f_transcript = ""

        with open(log_file.name, "a") as f:
            for file_name in os.listdir(data_dir):   
                file = os.path.join(data_dir, file_name)
                with sr.AudioFile(file) as source:
                    audio = recognizer.record(source)
                    f_transcript = recognizer.recognize_whisper(audio)
                    f.write(f_transcript)
        print("Log created gracefully.")

        return log_created_at, log_file






