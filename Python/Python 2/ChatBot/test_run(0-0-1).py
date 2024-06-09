import pandas as pd
import random
import requests
from googletrans import Translator
import sympy as sp
import secrets
import string
import pyttsx3

#Mookie can talk 
engine = pyttsx3.init('sapi5')
voices = engine.getProperty("voices")

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

# Define the filename for the conversation data CSV
memory_file = 'conversation_data.csv'

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

def save_conversation(user_message, bot_response):
    # Create or append to the CSV file with the conversation data
    with open(memory_file, 'a') as file:
        file.write(f"User: {user_message}\n")  # Write user's message
        file.write(f"Mookie: {bot_response}\n")  # Write bot's response

def delete_user_data():
    # Open the file in write mode to clear its contents
    with open(memory_file, 'w') as file:
        file.write("")  # Write an empty string to clear the file

def read_conversation():
    try:
        # Read and print the contents of the conversation data CSV
        with open(memory_file, 'r') as file:
            for line in file:
                print(line.strip())  # Strip newline characters and print each line
    except FileNotFoundError:
        print("No conversation data found.")

creator = open('creator_data.txt','r')


#generate password logic
def Password_Generator(pass_len,pass_type):
    password = ""
    password +="".join(secrets.choice(pass_type)for i in range (pass_len))
    return password

#Ask For PassWord Length

def ask_len():
    lenght = int(input("Mookie: What Should be the lenght of your password ? \n"))
    return lenght

#Ask password type
def ask_type():
    pass_type = input("Mookie: what type of password do you want ? \n")
    final_pass_type = pass_type.lower()
    return final_pass_type

#generate password

def passwords():
    password_type = ask_type()
    pass_len = ask_len()
    if password_type == "pincode":
        Generated_Pasword = Password_Generator(pass_len,string.digits)
        return f"The generated password is {Generated_Pasword}"
    elif password_type == "alphanumeric":
          Generated_Pasword = Password_Generator(pass_len,string.ascii_letters+string.digits+string.punctuation)
          return f"The generated password is {Generated_Pasword}"
    elif password_type == "alphabetic":
        Generated_Pasword = Password_Generator(pass_len,string.ascii_letters)
        return f"The generated password is {Generated_Pasword}"

def get_response(user_message):
        greetings = ["Hi there!", "Hello!", "Hey!", "What's up?", "Yo!"]
        how_are_you = ["I'm just a bot, but thanks for asking!", "I am doing great! Thank you!", "My code is running great so I am fine ^^", "I am a program, but sweet of you to ask still ", "I am fine thanks for asking!"]
        thankyou_response = ["np!", "Welcome!", "No Problem!", "Your Welcome", "Mention Not!"]
        i_am_fine = ["that's wonderful to hear", "gtk ^^", "that's great!", "nice!"]
        translator = Translator()

        if any(word in user_message.lower() for word in ["i am fine", "doing great", "been great"]):
            return random.choice(i_am_fine)
        elif "share about your creator" in user_message:
            data = creator.read()
            return data
        elif any(word in user_message.lower() for word in ["hello", "yoohoo", "hey"]):
            return random.choice(greetings)
        elif any(word in user_message.lower() for word in ["how are you", "how you doing", "hru", "how are you doing", "what's up", "how you doin"]):
            return random.choice(how_are_you)
        elif "bye" in user_message.lower():
            return "Goodbye! Have a great day!"
        elif any(word in user_message.lower() for word in ["password"]):
            answer = passwords()
            return answer
        elif any(word in user_message.lower() for word in ["thank you!", "ty", "tysm", "thanks"]):
            return random.choice(thankyou_response)
        elif "what do you think about me" in user_message.lower():
            return "you are a human, dummy!"
        elif user_message.lower().startswith("tell me about "):
            topic = extract_topic(user_message)
            summary = get_summary(topic)
            return summary
        elif user_message.lower().startswith(("speak ")):
            message = user_message.split("speak ")[1].strip()
            speak(message)
            return message
        elif user_message.lower().startswith(("integral of ", "differential of ")):
            function = user_message.split("of ")[1].strip()
            if user_message.lower().startswith("integral"):
                result = sp.integrate(function)
                return f"The integral of {function} is {result}"
            else:
                result = sp.diff(function)
                return f"The differential of {function} is {result}"
        elif user_message.lower().startswith("translate"):
            try:
                parts = user_message.split("to")
                content = parts[0][10:].strip()
                language = parts[1].strip()
                translated_content = translator.translate(content, dest=language)
                return f"{content} in {language} is {translated_content.text}"
            except Exception as e:
                return "Translation failed. Please try again."
        else:
            try:
                parts = user_message.split()
                if len(parts) == 3 and any(op in parts[1] for op in ['+', '-', '*', '/']):
                    num1, operator, num2 = parts
                    num1, num2 = float(num1), float(num2)
                    if operator == '+':
                        result = num1 + num2
                    elif operator == '-':
                        result = num1 - num2
                    elif operator == '*':
                        result = num1 * num2
                    elif operator == '/' and num2 != 0:
                        result = num1 / num2
                    else:
                        return "Cannot divide by zero!"
                    return f"The result is {result}"
                else:
                    return "Invalid input format!"
            except ValueError:
                return "Invalid input format!"

def extract_topic(user_input):
    return ' '.join(user_input.split()[3:])

def get_summary(topic):
        api_url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{topic}"
        try:
            response = requests.get(api_url)
            data = response.json()
            return data['extract']
        except requests.exceptions.RequestException as e:
            return "Error: Topic not found."

if __name__ == "__main__":
    start_chat()  # Start the chatbot interaction
