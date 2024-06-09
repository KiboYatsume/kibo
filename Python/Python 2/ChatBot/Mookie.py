import pandas as pd
import random
import requests
from googletrans import Translator
import sympy as sp
import secrets
import string
import pyttsx3
import sys

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

Questions = [
    ("what is the weakest fundamental force ?", "gravity"),
    ("Name the largest country", "russia"),
    ("Smallest value of the cosine function", "-1"),
    ("The sun rises from the ?", "east"),
    ("Fructose is obtained from  ?", "glucose"),
    ("What is the chemical symbol for gold?", "Au"),
    ("Who wrote 'Romeo and Juliet'?", "William Shakespeare"),
    ("What is the capital of France?", "Paris"),
    ("What is the chemical formula for water?", "H2O"),
    ("What is the largest mammal in the world?", "blue whale"),
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
    
    if points <= 5:
        print(f"Nice try, {name}!")
    elif points <= 8:
        print(f"Congrats, {name}! Near perfect!")
    else:
        print(f"AMAZING WORK, {name}! Perfect score!")

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
        elif "let's play quiz" in user_message.lower():
            ask()
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


def check_user(username, password, df):
    if 'Usename' in df.columns:
        if username in df['Usename'].values:
            stored_password = df.loc[df['Usename'] == username, 'Password'].iloc[0]
            if str(password) == str(stored_password):  
                print("User authenticated successfully!")
                print(f"Welcome {username}")
                start_chat()
            else:
                print("Incorrect password!")
        else:
            print("User not found!")
    else:
        print("Usename column not found in the Excel file.")

def add_user(df):
    new_username = input("Enter a new username: ")
    # Check if the username already exists
    if new_username in df['Usename'].values:
        print("Username already exists. Please choose a different one.")
        return

    new_password = input("Enter a password: ")
    # Append the new user to the DataFrame
    new_user = pd.DataFrame({'Usename': [new_username], 'Password': [new_password]})
    df = pd.concat([df, new_user], ignore_index=True)
    df.to_excel("user_credentials.xlsx", index=False)
    print(f"User {new_username} added successfully!")

def Exit():
    while True:
            print("Are you sure (yes/no) ? \n")
            try:
                confirmation = input("")
                if confirmation == "yes":
                    sys.exit()
                elif confirmation == 'no':
                        user_entry_menu()
                else:
                    print("Invalid Input")
            except Exception as e :
                print(e) 

def main():
    # Load the Excel file into a DataFrame
    df = pd.read_excel("user_credentials.xlsx")
    
    # Get username and password from the user
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    # Check if the user exists and authenticate
    check_user(username, password, df)

def admin_powers(username, password, admin_users):
    df = pd.read_excel("user_credentials.xlsx")
    if 'Username' in admin_users.columns:
        if username in admin_users['Username'].values:
            stored_password = admin_users.loc[admin_users['Username'] == username, 'Password'].iloc[0]
            if str(password) == str(stored_password):
                print("Admin authenticated successfully!")
                print("Enter User Credentials")
                add_user(df)
            else:
                print("Incorrect password!")
        else:
            print("Admin user not found!")
    else:
        print("Username column not found in the admin Excel file.")

def check_admin():
    admin_users = pd.read_excel('admin.xlsx')
    username = input("Enter your Admin name: ")
    password = input("Enter your password: ")
    admin_powers(username, password, admin_users)

def user_entry_menu():
    try:
        df = pd.read_excel("user_credentials.xlsx")
        while True:
            print("***Entry Portal*** \n1. Enter User \n2. Login Existing User \n3. Exit")
            option = int(input("Enter your choice: "))
            if option == 1:
                check_admin()
            elif option == 2:
                main()
            elif option == 3:
                Exit()
    except Exception as e:
        print(e)

if __name__ == "__main__":
    user_entry_menu()
