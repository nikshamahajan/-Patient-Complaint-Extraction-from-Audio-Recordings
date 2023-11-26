#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:





# In[ ]:





# In[4]:





# In[5]:





# In[ ]:





# In[24]:


get_ipython().system('pip install spacy')


# In[25]:


get_ipython().system('pip install SpeechRecognition==3.8.1')


# In[31]:


import speech_recognition as sr
import spacy

def transcribe_audio(audio_path):
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_path) as source:
        audio_data = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio_data)
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

def extract_complaints(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

    # Extract key phrases indicating patient problems
    key_phrases = [chunk.text for chunk in doc.noun_chunks]

    return key_phrases

if __name__ == "__main__":
    # Replace with the actual path to your audio file
    audio_file_path = "voicebooking-speech.wav"

    # Transcribe audio to text
    transcribed_text = transcribe_audio(audio_file_path)
    print("Transcribed Text:")
    print(transcribed_text)

    # Extract patient complaints
    complaints = extract_complaints(transcribed_text)
    print("\nExtracted Complaints:")
    print(complaints)


# In[ ]:





# In[ ]:





# In[ ]:




