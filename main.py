# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 15:46:16 2023

@author: ShreyashUpadhyaya
"""

import streamlit as st
import time
# Set page title
st.set_page_config(page_title="YouTube Video Summarization", page_icon="📜", layout="wide")

# Set title
st.title("YouTube Video Summarization", anchor=False)
st.header("Summarize YouTube videos with AI", anchor=False)

from download import download_audio_from_url
from summarize import summarize_transcript
from transcribe import transcribe_audio

# (... code continuation ...)

# Input URL
start = time.time()
st.divider()
url = st.text_input("Enter YouTube URL", value="")

# Download audio
st.divider()
if url:
    with st.status("Processing...", state="running", expanded=True) as status:
        to = time.time()
        
        st.write("Downloading audio file from YouTube...")
        audio_file, length = download_audio_from_url(url)
        st.write('audio file downloading done: ',time.time()-to)
        
        t1 = time.time()
        st.write("Transcribing audio file...")
        transcript = transcribe_audio(audio_file)
        st.write('Transcribing audio file done: ',time.time()-t1)
        
        t2 = time.time()
        st.write("Summarizing transcript...")
        with open("transcript.txt", "w") as f:
            f.write(transcript)
        summary = summarize_transcript("transcript.txt")
        status.update(label="Finished", state="complete")
        st.write('Transcribing audio file done: ',time.time()-t2)
        
    # Play Audio
    st.divider()
    st.audio(audio_file, format='audio/mp3')

    # Show Summary
    st.subheader("Summary:", anchor=False)
    st.write(summary)
    
    st.write('All process done: ',time.time()-start)