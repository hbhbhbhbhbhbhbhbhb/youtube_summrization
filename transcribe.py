# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 17:16:43 2023

@author: ShreyashUpadhyaya
"""

from decouple import config
from deepgram import Deepgram

# DEEPGRAM_API_KEY = config('f93c6043b972f3239a88f04c36794f3d4453d11d')

def transcribe_audio(filename):
    dg_client = Deepgram('f93c6043b972f3239a88f04c36794f3d4453d11d')
    with open(filename, 'rb') as audio:
        source = {'buffer': audio, 'mimetype': 'audio/mp3'}
        response = dg_client.transcription.sync_prerecorded(source,
                                                            model='nova-2-ea',
                                                            smart_format=True)
        transcript = response['results']['channels'][0]['alternatives'][0]['transcript']
        return transcript