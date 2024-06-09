import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import pandas as pd
import random
import requests
from googletrans import Translator
import sympy as sp
import secrets
import string
import pyttsx3
import sys

# Download necessary NLTK datasets
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Initialize text-to-speech engine
engine = pyttsx3.init('sapi5')

# Initialize NLTK components
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

# Define conversation data filename
memory_file = 'conversation_data.csv'

# Text-to-Speech setup
def set_voice(language='en'):
    voices = {
        'en': 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0',
        'ja': 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_JA-JP_HARUKA_11.0',
        'ko': 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_KO-KR_HEAMI_11.0',
        'hi': 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_HI-IN_KALPANA_11.0'
    }
    engine.setProperty('voice', voices.get(language, voices['en']))

def speak(text, language='en'):
    set_voice(language)
    engine.say(text)
    engine.runAndWait()

# Save conversation data
def save_conversation(user_message, bot_response):
    with open(memory_file, 'a') as file:
        file.write(f"User: {user_message}\n")
        file.write(f"Mookie: {bot_response}\n")

def delete_user_data():
    with open(memory_file, 'w') as file:
        file.write("")

def read_conversation():
    try:
        with open(memory_file, 'r') as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("No conversation data found.")

creator = open('creator_data.txt','r')

# Generate password logic
def password_generator(pass_len, pass_type):
    return ''.join(secrets.choice(pass_type) for _ in range(pass_len))

def ask_len():
    try:
        return int(input("Mookie: What should be the length of your password? \n"))
    except ValueError:
        print("Please enter a valid number.")
        return ask_len()

def ask_type():
    return input("Mookie: What type of password do you want? \n").lower()

def passwords():
    password_type = ask_type()
    pass_len = ask_len()
    if password_type == "pincode":
        return password_generator(pass_len, string.digits)
    elif password_type == "alphanumeric":
        return password_generator(pass_len, string.ascii_letters + string.digits + string.punctuation)
    elif password_type == "alphabetic":
        return password_generator(pass_len, string.ascii_letters)
    else:
        print("Invalid password type.")
        return passwords()

# Quiz questions
Questions = [
    ("What is the weakest fundamental force?", "gravity"),
    ("Name the largest country", "russia"),
    ("Smallest value of the cosine function", "-1"),
    ("The sun rises from the?", "east"),
    ("Fructose is obtained from?", "glucose"),
    ("What is the chemical symbol for gold?", "Au"),
    ("Who wrote 'Romeo and Juliet'?", "William Shakespeare"),
    ("What is the capital of France?", "Paris"),
    ("What is the chemical formula for water?", "H2O"),
    ("What is the largest mammal in the world?", "blue whale")
]

def ask():
    points = 0
    for question, answer in Questions:
        user_input = input(question + "\n")
        if user_input.strip().lower() == answer.lower():
            print("BINGO!")
            points += 1
        else:
            print("aww that's not right!")
    
    name = input("Enter your name: ")
    feedback = {
        points <= 5: f"Nice try, {name}!",
        points <= 8: f"Congrats, {name}! Near perfect!",
        points > 8: f"AMAZING WORK, {name}! Perfect score!"
    }
    print(feedback[True])

translator = Translator()

def preprocess_text(text):
    tokens = word_tokenize(text)
    filtered_tokens = [lemmatizer.lemmatize(word.lower()) for word in tokens if word.lower() not in stop_words and word.isalnum()]
    return filtered_tokens

def get_response(user_message):
    processed_message = preprocess_text(user_message)
    greetings = ["hi", "hello", "hey"]
    farewells = ["bye", "goodbye"]
    gratitude = ["thank", "thanks"]
    
    if any(word in processed_message for word in greetings):
        return random.choice(["Hi there!", "Hello!", "Hey!"])
    elif any(word in processed_message for word in farewells):
        return "Goodbye! Have a great day!"
    elif any(word in processed_message for word in gratitude):
        return random.choice(["You're welcome!", "No problem!", "My pleasure!"])
    elif "password" in processed_message:
        return passwords()
    elif "quiz" in processed_message:
        ask()
    elif "translate" in processed_message:
        try:
            parts = user_message.split("to")
            content = parts[0][10:].strip()
            language = parts[1].strip()
            translated_content = translator.translate(content, dest=language)
            return f"{content} in {language} is {translated_content.text}"
        except Exception as e:
            return "Translation failed. Please try again."
    elif "creator" in processed_message:
        return creator.read()
    else:
        return "I didn't understand that. Can you please rephrase?"

def check_user(username, password, df):
    if 'Usename' in df.columns:
        user_row = df[df['Usename'] == username]
        if not user_row.empty and str(password) == str(user_row.iloc[0]['Password']):
            print("User authenticated successfully!")
            print(f"Welcome {username}")
            start_chat()
        else:
            print("Incorrect username or password!")
    else:
        print("Usename column not found in the Excel file.")

def add_user(df):
    new_username = input("Enter a new username: ")
    if new_username in df['Usename'].values:
        print("Username already exists. Please choose a different one.")
    else:
        new_password = input("Enter a password: ")
        new_user = pd.DataFrame({'Usename': [new_username], 'Password': [new_password]})
        df = pd.concat([df, new_user], ignore_index=True)
        df.to_excel("user_credentials.xlsx", index=False)
        print(f"User {new_username} added successfully!")

def start_chat():
    print("Welcome, I am Mookie ChatBot")
    while True:
        user_message = input("You: ")  # Get user input
        if user_message.lower() == "bye":
            break  # Exit the loop if user says "bye"
        elif user_message.lower() == "delete my data":
            delete_user_data()  # Call function to delete user data
            print("Mookie: Your data has been deleted.")
        else:
            response = get_response(user_message)  # Generate bot response
            print("Mookie: " + response)  # Print bot's response
            save_conversation(user_message, response)  # Save conversation data

def main():
    df = pd.read_excel("user_credentials.xlsx")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    check_user(username, password, df)

def admin_powers(username, password, admin_users):
    if 'Username' in admin_users.columns:
        admin_row = admin_users[admin_users['Username'] == username]
        if not admin_row.empty and str(password) == str(admin_row.iloc[0]['Password']):
            print("Admin authenticated successfully!")
            df = pd.read_excel("user_credentials.xlsx")
            add_user(df)
        else:
            print("Incorrect admin username or password!")
    else:
        print("Username column not found in the admin Excel file.")
