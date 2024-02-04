import smtplib
import os
import webbrowser
import wikipedia
import pyttsx3
import speech_recognition as sr
import datetime
import random as r
import subprocess
import pyjokes
import googletrans 
from gtts import gTTS
from googletrans import Translator

translator = Translator() 
engine = pyttsx3.init('sapi5')
vocies = engine.getProperty("voices")
print("Initializing Artrimus")
# Allows Artrimus to Talk
def speak(text, language='en'):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Set the voice based on the specified language
    if language.lower() == 'en':
        engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0')
    elif language.lower() == 'ja':
        engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_JA-JP_HARUKA_11.0')
    elif language.lower() == 'ko':
        engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_KO-KR_HEAMI_11.0')
    elif language.lower() == 'hi':
         engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_HI-IN_KALPANA_11.0')
    else:
        print(f"No voice available for language: {language}")
        return

    # Convert text to speech and play
    engine.say(text)
    engine.runAndWait()


# Facts collection

Fact_lib =[
     "Fact 1 : Though less common than earthquakes, the moon actually has moonquakes, too.",
        "Fact 2 : You actually lose a large percentage of your taste buds while on an airplane. This might explain a lot about those less-than-stellar in-flight meals, or why you find yourself craving the saltiest foods while in the sky.",
        "Fact 3 : Although it may sound counterintuitive, your small intestine is actually the largest (internal) organ in your body.",
        "Fact 4 : You probably know that snails are petty slow creatures, but did you know that they also take the longest naps? One nap can last up to three years!",
        "Fact 5 : You may be jealous of a bird's ability to fly, but it may soothe your envy to learn they can't live in space because they need gravity to swallow.",
        "Fact 6 : Bees can sting other bees — usually if they feel threatened or are protecting their territory. In other words, you're not the only one who's scared of getting stung.",
        "Fact 7 : Whether you've seen a tiger in real life or in a photo, you know that they have striped fur. But they actually have striped skin, as well.",
        "Fact 8 : If you're a cat lover, then you may be surprised by this interesting fact: Cats can't taste anything that's sweet. That's probably why they can't get enough of their favorite salty snack.",
        "Fact 9 : Most people know dolphins have incredible sonar abilities. But did you know they were studied as war tools during the Cold War? They really are as smart as people say they are.",
        "Fact 10 : Not only are sea lions totally adorable, but they're also very musical. They are the only animal that can clap to a beat.",
        "Fact 11 : Like humans, koalas actually have unique individual fingerprints. If you place a koala and human finger print side by side, they're actually pretty hard to differentiate. ",
        "Fact 12 : You may know that everyone's fingerprints are different, but did you know that the same is true of everyone's tongue print?",
        "Fact 13 : Your brain uses 10 watts of energy to think, but it can't feel pain. You know what they say: Mind over matter.",
        "Fact 14 : Brendan Fraser almost died while filming The Mummy (he passed out while filming a scene). Pretty scary, right?",
        "Fact 15 : In a group of 23 people, there is a 50 percent chance that two will share the same birthday.",
        "Fact 16 : Will Ferrell consumed so much sugar while filming Elf that he actually became physically ill. If you've seen the famous spaghetti scene, then you can probably understand why.",
        "Fact 17 : It may feel a lot longer in the moment, but the average person spends two weeks of their life sitting at traffic lights.",
        "Fact 18 : The Hollywood sign in Los Angeles once said Hollywoodland, but was changed in 1949",
        "Fact 19 : The most expensive film ever made was Pirates of the Caribbean: On Stranger Tides, which cost 378 million dollars to create. For reference, the average budget for a big studio movie is around $65 million.",
        "Fact 20 : If E.T. is one of your favorite movies of all time, then you'll be interested to know that someone squished their hands in jelly to make the sound effect for E.T. walking around"
    ] 
    

# Artrimus Wishes Me
def wishMe():
    L = ["Greetings","Hello","Welcome Back", "Welcome","Hey There","Hello There"]
    speak(r.choice(L)+"Kibo")
    hour = int(datetime.datetime.now().hour)
    print(hour)

    if hour>=0 and hour <12:
        speak("Good Morning",language='en')
    elif hour>12 and hour<18:
        speak("Good Aftertoon",language='en')
    else :
        speak("Good Evening",language='en')
    speak('How may i help you ?',language='en')   
def Wish_User():
    wishMe()
# take command from user via a microphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source :
        print("Listening...")
        audio = r.listen(source)
    try :
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"user said {query}\n")
    except Exception as e :
        speak("Say That Again Please",language='en')
        query = None
    return query
fact = r.choice(Fact_lib)
def Input():
    query = takeCommand()
    # execute tasks as per user query
    spotify_path = ''
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    if 'according to wikipedia' in query.lower():
        speak('Searching wikipedia',language='en')
        query = query.replace('according to wikipedia','')
        results = wikipedia.summary(query,sentences = 4)
        speak(results,language='en')
    elif "tell me a fact" in query.lower():
        speak(fact)
    elif 'search on google' in query.lower():
        speak("What do you want to search for on Google?",language='en')
        search_query = takeCommand().lower()
        google_search_url = f"https://www.google.com/search?q={search_query}"
        speak("Searching on Google...",language='en')
        webbrowser.get(chrome_path).open(google_search_url)
    elif 'open wikipedia' in query.lower():
        speak("opening Wikipedia...",language='en')
        url = 'wikipedia.com'
        webbrowser.get(chrome_path).open(url)
    elif 'open youtube' in query.lower():
        speak("opening Youtube...",language='en')
        url = 'youtube.com'
        webbrowser.get(chrome_path).open(url)
    elif 'open spotify' in query.lower():
        speak("opening Spotify...",language='en')
        os.system('start spotify://')
    elif 'play music' in query.lower():
        song_dir = "C:\\Users\\tatha\\Music\\Music"
        song = os.listdir(song_dir)
        os.startfile(os.path.join(song_dir,song[0]))
    elif 'time' in query.lower():
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        time_parts = current_time.split(':')
        hours = time_parts[0]
        minutes_period = time_parts[1].split()
        minutes = minutes_period[0]
        period = minutes_period[1]
        speak("It's currently " + hours + " " + minutes + " " + period,language='en')
    elif 'translater' or 'translator' in query.lower():
        speak("which language do you want to translate to or from ?",language='en')
        language_query = takeCommand().lower()
        if 'from japanese' in language_query.lower():
            r = sr.Recognizer()
            with sr.Microphone() as source :
                print("Listening...")
                speak("What do you want to tanslate ?",language='en')
                audio = r.listen(source)
                japanese_text = r.recognize_google(audio, language = 'ja-JP')
                english_translation = translator.translate(japanese_text, src='ja', dest='en')
                speak("The English translation is: " + english_translation.text,language='en')
        elif 'from korean' in language_query.lower():
            r = sr.Recognizer()
            with sr.Microphone() as source :
                print("Listening...")
                speak("What do you want to tanslate ?",language='en')
                audio = r.listen(source)
                Korean_text = r.recognize_google(audio, language = 'ko-KR')
                english_translation = translator.translate(Korean_text, src='ko', dest='en')
                speak("The English translation is: " + english_translation.text,language='en')
        elif 'from hindi' in language_query.lower():
            r = sr.Recognizer()
            with sr.Microphone() as source :
                print("Listening...")
                speak("What do you want to tanslate ?",language='en')
                audio = r.listen(source)
                Hindi_text = r.recognize_google(audio, language = 'hi-IN')
                english_translation = translator.translate(Hindi_text, src='hi', dest='en')
                speak("The English translation is: " + english_translation.text,language='en')
        elif 'to japanese' in language_query.lower():
             r = sr.Recognizer()
             with sr.Microphone() as source :
                print("Listening...")
                speak("What do you want to tanslate ?",language='en')
                audio = r.listen(source)
                english_text = r.recognize_google(audio, language = 'en-IN')
                japanese_translation = translator.translate(english_text, src='en', dest='ja')
                speak(japanese_translation.text,language='ja')
        elif 'to korean' in language_query.lower():
            r = sr.Recognizer()
            with sr.Microphone() as source :
                print("Listening...")
                speak("What do you want to tanslate ?",language='en')
                audio = r.listen(source)
                english_text = r.recognize_google(audio, language = 'en-IN')
                korean_translation = translator.translate(english_text, src='en', dest='ko')
                speak(korean_translation.text,language='ko')
        elif 'to hindi' in language_query.lower():
            r = sr.Recognizer()
            with sr.Microphone() as source :
                print("Listening...")
                speak("What do you want to tanslate ?",language='en')
                audio = r.listen(source)
                english_text = r.recognize_google(audio, language = 'en-IN')
                hindi_translation = translator.translate(english_text, src='en', dest='hi')
                speak(hindi_translation.text,language='hi')
