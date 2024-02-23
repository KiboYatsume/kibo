from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
chatbot = ChatBot('MyChatBot')
trainer = ChatterBotCorpusTrainer(chatbot)
# Train the chatbot on English language data
trainer.train('chatterbot.corpus.english')
