import speech_recognition as sr
import pyttsx3
import webbrowser

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__== "__main__":
    '''speak("""Hey, how are you? I am Jarvis
           a virtual,Artificial assistant 
          just give me the command 
          and the work is done""")'''
    speak("speak jarvis whenever needed")
    with sr.Microphone() as source:
                print("Initializing Jarvis;)    ......")
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source, timeout=5)
                print("Recognizing the text :]    ........ ")
                command = recognizer.recognize_google(audio)
    while (command.upper()=="jarvis".upper()):
        try:
            with sr.Microphone() as source:
                print("keep on it started")
                print("Initializing Jarvis;)    ......")
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source, timeout=5)
                print("Recognizing the text :]    ........ ")
            
            command = recognizer.recognize_google(audio)
            print("You said:", command)
            if command.upper() == "jarvis open youtube".upper():#command for youtube
             webbrowser.open("https://www.youtube.com/")
            elif command.upper() == "jarvis open Google".upper():#command for google
             webbrowser.open("https://www.google.com")
            elif command.upper() == "jarvis open gpt".upper():#command for gpt
             webbrowser.open("https://chatgpt.com/")
            elif command.upper() == "jarvis sleep".upper():#command for shutting down
             break
            elif command.upper() == "open note".upper():#command for note making
              speak("it start from now") 
            with open("note.txt","r")as note:
               print(command)
               note.write(command)
        
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand that.")
        
        except sr.RequestError:
            print("Error occurred timeout crash")