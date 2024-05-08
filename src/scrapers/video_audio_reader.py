# -*- coding: utf-8 -*-


import vosk
import subprocess
def extract_text_from_vid(vid_path):
    text = ""
    
    cmd = ['vosk-transcriber', '-n', 'vosk-model-en-us-0.22', '-i', str(vid_path), '-o', 'transcription.txt']
    #! vosk-transcriber -n vosk-model-en-us-0.22 -i audio_vid.mp3 -o transcription.txt
    subprocess.call(cmd)
    doc = open("transcription.txt",'r')
    text = doc.read()
    doc.close()

    return text
