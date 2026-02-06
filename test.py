import struct
import pvporcupine
import pyaudio
import pyautogui as pag
import time

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

if __name__ == "__main__":
    hotword()