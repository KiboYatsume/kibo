from nltk.chat.util import Chat

# Define NLTK chat pairs
pairs = [
    [
        r"(.*)hello|hi|hey(.*)",
        ["Hello!", "Hi there!", "Hey! How can I help you today?"]
    ],
    [
        r"(.*)your name(.*)",
        ["I'm a chatbot. You can call me NLTK Bot."]
    ],
    [
        r"(.*)your favorite color(.*)",
        ["I don't have a favorite color. I'm just a program."]
    ],
    [
        r"(.*)quit|exit|bye(.*)",
        ["Goodbye!", "See you later!"]
    ],
    [
    r"how are you(.*)",
    ["I'm just a program, so I don't have feelings, but thanks for asking!", "I'm here to assist you, what can I help you with today?"]
    ],
    [
        r"(.*)help(.*)",
        ["Sure, I'd be happy to help. What do you need assistance with?", "What specific assistance do you require?"]
    ],
    [
        r"(.*)age(.*)",
        ["I'm just a program, so I don't have an age.", "I don't age like humans do."]
    ],
    [
        r"(.*)weather(.*)",
        ["I'm sorry, I don't have access to weather information.", "You can check the weather forecast online or on your phone."]
    ],
    [
        r"(.*)favorite anime(.*)",
        ["I don't have personal preferences, but I can recommend some popular anime if you're interested!"]
    ],
    [
        r"(.*)favorite k-drama(.*)",
        ["As a chatbot, I don't have personal preferences, but I can suggest some popular K-dramas if you'd like."]
    ],
    [
        r"(.*)play guitar(.*)",
        ["That's awesome! Playing guitar is a great skill. How's your practice going?", "How do you like learning to play the guitar?"]
    ],
    [
        r"(.*)learning Japanese(.*)",
        ["Learning Japanese is exciting! Are you enjoying the process?", "How's your Japanese learning journey going?"]
    ]

]

# Create an NLTK chat
chat = Chat(pairs)

# Define a function to interact with the chatbot
def run_chat():
    print("NLTK Bot: Hi there! How can I help you today?")
    while True:
        user_input = input("You: ")
        response = chat.respond(user_input)
        print("NLTK Bot:", response)
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("NLTK Bot: Goodbye!")
            break

# Run the chatbot
if __name__ == "__main__":
    run_chat()
