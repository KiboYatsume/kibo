import random
import requests
from googletrans import Translator
import sympy as sp

def Mookie_Bot():
    memory = {}
    
    def start_chat():
        print("Welcome, I am Mookie ChatBot")
        while True:
            user_message = input("You: ")
            response = get_response(user_message)
            print("Mookie: " + response)
            if user_message.lower() == "bye":
                break

    def get_response(user_message):
        greetings = ["Hi there!", "Hello!", "Hey!", "What's up?", "Yo!"]
        how_are_you = ["I'm just a bot, but thanks for asking!", "I am doing great! Thank you!", "My code is running great so I am fine ^^", "I am a program, but sweet of you to ask still .?", "I am fine thanks for asking!"]
        thankyou_response = ["np!", "Welcome!", "No Problem!", "Your Welcome", "Mention Not!"]
        i_am_fine = ["that's wonderful to hear", "gtk ^^", "that's great!", "nice!"]
        translator = Translator()

        if any(word in user_message.lower() for word in ["i am fine", "doing great", "been great"]):
            return random.choice(i_am_fine)
        elif any(word in user_message.lower() for word in ["hello", "yoohoo", "hey"]):
            return random.choice(greetings)
        elif any(word in user_message.lower() for word in ["how are you", "how you doing", "hru", "how are you doing", "what's up", "how you doin"]):
            return random.choice(how_are_you)
        elif "bye" in user_message.lower():
            return "Goodbye! Have a great day!"
        elif any(word in user_message.lower() for word in ["thank you!", "ty", "tysm", "thanks"]):
            return random.choice(thankyou_response)
        elif user_message.lower().startswith("i am "):
            name = user_message[5:]
            memory["name"] = name
            return f"Nice to meet you, {name}!"
        elif user_message.lower().startswith("my name is "):
            name = user_message[11:]
            memory["name"] = name
            return f"Nice to meet you, {name}!"
        elif "who are you" in user_message.lower():
            return "I am Mookie ChatBot"
        elif "who is your creator" in user_message.lower():
            return "Kibo"
        elif user_message.lower().startswith("i like "):
            item = user_message.split("like")[1].strip()
            memory["preference"] = item
            return f"Noted! You like {item}."
        elif "who am i" in user_message.lower():
            return f"You are {memory.get('name', 'unknown')}"
        elif "what is my name" in user_message.lower():
            return f"Your name is {memory.get('name', 'unknown')}"
        elif "what do i like" in user_message.lower():
            return f"You like {memory.get('preference', 'unknown')}"
        elif "what do you think about me" in user_message.lower():
            return "you are a human, dummy!"
        elif user_message.lower().startswith("tell me about "):
            topic = extract_topic(user_message)
            summary = get_summary(topic)
            return summary
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

    start_chat()

if __name__ == "__main__":
    Mookie_Bot()
