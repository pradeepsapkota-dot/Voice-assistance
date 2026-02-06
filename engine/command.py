import pyttsx3
import speech_recognition as sr
import eel
import time




def speak(text):
    text = str(text)
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices') 
    engine.setProperty('voice', voices[0].id) 
    engine.setProperty('rate', 174) 
    eel.DisplayMessage(text)
    engine.say(text)
    eel.receiverText(text)
    engine.runAndWait()


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        eel.DisplayMessage("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source,10,10)
    try:
        print("Recognizing...")
        eel.DisplayMessage("Recognizing...")
        query = r.recognize_google(audio, language='en-in')

        print(f"User said: {query}")
        eel.DisplayMessage( query)
        time.sleep(2)
      



    except Exception as e:
            print("Say that again please...")
            eel.DisplayMessage("Say that again please...")
            speak("I didnot catch your words. Please say that again.")
            eel.ShowHood()
    return query.lower()


@eel.expose
def allcommands(message = 1):
    if message == 1:
        query = takecommand()
        print (query)
        eel.senderText(query)
    else:
        query = message
        eel.senderText(query)
        print("Text command received: " + query)
        



    try:
        if "open" in query:
            from engine.feature import openCommand
            openCommand(query)

        elif "on youtube"  in query:
            from engine.feature import PlayYoutube
            PlayYoutube(query)

      
# create whatsapp command

        elif "send message" in query or "phone call" in query or "video call" in query:
            from engine.feature import findContact, whatsApp
            flag = ""
            contact_no, name = findContact(query)
            if(contact_no != 0):

                if "send message" in query:
                    flag = 'message'  # flag is being used to identify message sending
                    speak("what message to send")
                    query = takecommand()
                    
                elif "phone call" in query:
                    flag = 'call'
                else:
                    flag = 'video call'

                whatsApp(contact_no, query, flag, name)

        else:
            from engine.feature import chatBot
            response = chatBot(query)
            print("Chatbot response: " + response)
    except Exception as e:
        print(f"Error occurred: {e}") # This will tell you EXACTLY what is failing


    eel.ShowHood()




"""import pyttsx3
import speech_recognition as sr
import eel
import time

# Initialize TTS Engine Once to avoid lag
engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[0].id) 
engine.setProperty('rate', 174) 

def speak(text):
    text = str(text)
    # 1. Update the "Ask me anything" text on screen
    eel.DisplayMessage(text)
    # 2. Add the bubble to the chat canvas (visual history)
    eel.receiverText(text)
    # 3. Voice output
    engine.say(text)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        eel.DisplayMessage("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source, 10, 10)
    try:
        print("Recognizing...")
        eel.DisplayMessage("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        
        # Display user text in UI (Visual history)
        eel.senderText(query)
        return query.lower()
    except Exception:
        return ""

@eel.expose
def allcommands(message=1):
    if message == 1:
        query = takecommand()
    else:
        query = message
        # Display typed text in UI
        eel.senderText(query)

    if query == "":
        eel.ShowHood()
        return

    try:
        if "open" in query:
            from engine.feature import openCommand
            openCommand(query)
        elif "on youtube" in query:
            from engine.feature import PlayYoutube
            PlayYoutube(query)

        elif "send message" in query or "phone call" in query or "video call" in query:
            from engine.feature import findContact, whatsApp
            contact_no, name = findContact(query)
            if contact_no != 0:
                flag = 'message' if "send message" in query else ('call' if "phone call" in query else 'video call')
                if flag == 'message':
                    speak("what message to send")
                    msg_query = takecommand()
                    whatsApp(contact_no, msg_query, flag, name)
                else:
                    whatsApp(contact_no, "", flag, name)
        else:
            from engine.feature import chatBot
            response = chatBot(query)
            speak(response)
    except Exception as e:
        print(f"Error occurred: {e}")

    eel.ShowHood()"""