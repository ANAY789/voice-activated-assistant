import speech_recognition as sr
import pyttsx3
from datetime import datetime
def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate',150)
    engine.say(text)
    engine.runAndWait()
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(" speak now...")
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio)
            print(f"you said{command}")
            return command.lower()
        except sr.UnknownValueError:
            print("could not understand")
        except sr.RequestError as e:
            print(f"api error:{e}")
    return ""
def respond_to_command(command):
    if "hello" in command:
        speak("hi there! how can i help you today")
    elif "time" in command:
        now = datetime.now().strftime("%H:%H")
        speak(f"the time is {now}")
    elif "exit" in command or "stop" in command:
        speak("goodbye")
        return False
    else:
        speak("i am not sure how to help with that")
    return True
def main():
    speak("voices assistant activated. say something")
    while True:
        command = get_audio()
        if command and not respond_to_command(command):
            break
if __name__=="__main__":
    main()