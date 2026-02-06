import subprocess
from urllib.parse import quote
import struct
import webbrowser
import eel 
import os
import pvporcupine
import pyaudio
import pywhatkit as kit
import re
import sqlite3
import pyautogui as pag
import time
from playsound import playsound as ps
from engine.config import ASSISTANT_NAME
from engine.command import speak
from engine.helper import *
from hugchat import hugchat


conn = sqlite3.connect("luffy.db")
c = conn.cursor()

@eel.expose
#Playing assistance sound function
def playassisound():
    voice_path = "www\\assets\\audio\\start_sound.mp3"
    ps(voice_path)



def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query.lower()

    app_name = query.strip()
    if app_name != "" :

        try:
            c.execute("SELECT path FROM sys_command WHERE name IN (?)", (app_name,))
            results = c.fetchall()

            if len(results) != 0:
                speak(f"Opening {query}")
                os.startfile(results[0][0])
            elif len(results) == 0:
                c.execute("SELECT url FROM web_command WHERE name IN (?)", (app_name,))
                results = c.fetchall()
                if len(results) != 0:
                    speak(f"Opening {query}")
                    webbrowser.open(f"start {results[0][0]}") 
                else:
                    speak(f"Opening {query}")
                    try:
                        os.system(f"start {query}")
                    except:
                        speak(f"Sorry, I couldn't find the application or website named {query}.")
        except:
            speak(f"Something went wrong")

def PlayYoutube(query):
    search_term = extract_yt_term(query)
    speak("Playing "+search_term+" on YouTube")
    kit.playonyt(search_term)



def hotword():
    porcupine = None
    paud = None
    audio_stream = None
    
    try:
        # On v1.9.5, 'keywords' uses the built-in files already in the library
        # You cannot use 'Hitler', 'Luffy', or 'Goku' here unless you have 
        # specifically v1.9.5 compatible .ppn files for them.
        porcupine = pvporcupine.create(keywords=["jarvis", "alexa"])

        paud = pyaudio.PyAudio()
        audio_stream = paud.open(
            rate=porcupine.sample_rate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=porcupine.frame_length
        )

        print("Listening for 'Jarvis' or 'Alexa' (v1.9.5)...")

        while True:
            pcm = audio_stream.read(porcupine.frame_length)
            pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)
            
            word_index = porcupine.process(pcm)
            
            if word_index >= 0:
                print(f"Detected keyword index: {word_index}")
                # Action: Ctrl + L
                pag.keyDown("ctrl")
                pag.press("l")
                time.sleep(0.2)
                pag.keyUp("ctrl")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if paud is not None:
            paud.terminate() 

# Create find contacts number Function
def findContact(query):
    
    
    words_to_remove = [ASSISTANT_NAME, 'make', 'a', 'to', 'phone', 'call', 'send', 'message', 'wahtsapp', 'video']
    query = remove_words(query, words_to_remove)

    try:
        query = query.strip().lower()
        c.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
        results = c.fetchall()
        print(results[0][0])
        mobile_number_str = str(results[0][0])
        if not mobile_number_str.startswith('+'):
            mobile_number_str = '+358' + mobile_number_str

        return mobile_number_str, query
    except:
        speak('not exist in contacts')
        return 0, 0



"""#Create Whatsapp Function
def whatsApp(mobile_no, message, flag, name):
    if flag == 'message':
        target_tab = 2 # Adjusted for modern WhatsApp Web layout
        jarvis_message = f"Message sent successfully to {name}"
    elif flag == 'call':
        target_tab = 7
        message = ''
        jarvis_message = f"Calling {name}"
    else:
        target_tab = 11
        message = ''
        jarvis_message = f"Starting video call with {name}"

    encoded_message = quote(message)
    whatsapp_url = f"https://web.whatsapp.com/send?phone={mobile_no}&text={encoded_message}"

    # Use webbrowser instead of subprocess for better stability
    webbrowser.open(whatsapp_url)
    
    # Wait for the page to load (WhatsApp Web can be slow)
    time.sleep(10) 

    webbrowser.open(whatsapp_url)  # Reopen to ensure focus
    time.sleep(5)  # Additional wait time to ensure the page is fully loaded

    if flag == 'message':
        # Just press enter to send the message
        pag.press('enter')
    else:
        # Logic for calls using tabs
        for i in range(target_tab):
            pag.press('tab')
        pag.press('enter')

    speak(jarvis_message)"""


# Updated WhatsApp Function in feature.py
def whatsApp(mobile_no, message, flag, name):
    if flag == 'message':
        jarvis_message = f"Message sent successfully to {name}"
    elif flag == 'call':
        jarvis_message = f"Calling {name}"
    else:
        jarvis_message = f"Starting video call with {name}"

    encoded_message = quote(message)
    # This URL pre-fills the message and target number
    whatsapp_url = f"https://web.whatsapp.com/send?phone={mobile_no}&text={encoded_message}"

    webbrowser.open(whatsapp_url)
    
    # WhatsApp Web takes time to load and find the contact
    # Increased sleep time is recommended for slower connections
    time.sleep(15) 

    if flag == 'message':
        # Once the page loads, the text is already in the box. 
        # Pressing 'Enter' is the most reliable way to send.
        pag.press('enter')
    
    elif flag == 'call':
        # Instead of tabs, use the shortcut for a voice call if supported
        # Or click based on screen coordinates if necessary
        for i in range(8): # Default tab count for voice call
            pag.press('tab')
        pag.press('enter')
        
    elif flag == 'video call':
        for i in range(9): # Default tab count for video call
            pag.press('tab')
        pag.press('enter')

    speak(jarvis_message)


# chat bot function
def chatBot(query):
    user_input = query.lower()
    chatbot = hugchat.ChatBot(cookie_path="engine/cookies.json")
    id = chatbot.new_conversation()
    chatbot.change_conversation(id)
    response = chatbot.chat(user_input)
    speak(response)
    return response 
