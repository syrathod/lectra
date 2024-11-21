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
    def transcribe(log_created_at):
        data_dir = os.path.join("./data")

        recognizer = sr.Recognizer()

        log_file =  open(f"./logs/{log_created_at}.txt", "x")
        f_transcript = ""
        f_counter = 0
        file_count = len([file_count for file_count in os.listdir(data_dir)])

        with open(log_file.name, "a") as f:
            for file_name in os.listdir(data_dir):   
                f_counter += 1   
                
                if f_counter == file_count:
                    break 

                # else:
                file = os.path.join(data_dir, file_name)
                with sr.AudioFile(file) as source:
                    audio = recognizer.record(source)
                    f_transcript = recognizer.recognize_whisper(audio)
                    f.write(f_transcript)
                    # print(f_counter)
                
        print("[+] Log created gracefully.")

        return log_file

        # print(file_count)





