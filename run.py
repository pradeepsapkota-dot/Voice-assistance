import subprocess
import multiprocessing
import os

def stratLuffy():
    print("Starting Luffy Assistant...")
    from main import start
    start()

def listenHotword():
    print("Listening for hotword...")
    from engine.feature import hotword
    hotword()

def setupDevice():
    # Calling the batch file in its own process
    subprocess.Popen([r'device.bat'], shell=True)

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=stratLuffy)
    p2 = multiprocessing.Process(target=setupDevice)
    p3 = multiprocessing.Process(target=listenHotword)

    p1.start()
    p2.start()
    p3.start()
    
    p1.join()

    # Cleanup
    if p2.is_alive():
        p2.terminate()
        p2.join()
    if p3.is_alive():
        p3.terminate()
        p3.join()
        
    print("System Stop")