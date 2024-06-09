import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty("voices")
Owner = "Kibo"

# Set the voice based on the specified language
def set_voice(language='en'):
    if language.lower() == 'en':
        engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
    elif language.lower() == 'ja':
        engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_JA-JP_HARUKA_11.0')
    elif language.lower() == 'ko':
        engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_KO-KR_HEAMI_11.0')
    elif language.lower() == 'hi':
         engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_HI-IN_KALPANA_11.0')
    else:
        print(f"No voice available for language: {language}")

# Allow Friday to talk
def speak(text, language='en'):
    set_voice(language)
    engine.say(text)
    engine.runAndWait()

speak("Stabilizing net framework")
speak(" System is now online")

# Allow Friday to listen to the user
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
            return query
        except Exception as e:
            print(f"Recognition error: {e}")
            speak("Say that again, please", language='en')
            return None

# self destruct

def self_destruct():
    try :
        query = takeCommand()
        if query.lower() == "clearance level omega code 8525":
            speak(f"Master {Owner} identified !")
            speak("self destruct active and engaged")
            speak("self destructing in t minus ten seconds")
            for i in range (10, 0 , -1):
                speak(str(i))
            quit()
        elif query.lower() == "abort command code 10":
            speak("self destruct aborted")
        else :
            speak("Acess Denied")
    except Exception as e:
        speak(e)
# Process query
def user_input_handler():
    query = takeCommand()
    if query:
        command = query.lower()
        if command == "execute order 66":
            speak("All jedis are enemies of the republic!")
        elif query.lower() == "activate self destruct":
            speak("please state the master code")
            self_destruct()

user_input_handler()
