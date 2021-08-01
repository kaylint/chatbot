#imports
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

#create instance
bot = ChatBot(
    "Bob",
    preprocessors=['chatterbot.preprocessors.clean_whitespace'])

#set up sql database
bot = ChatBot(
    'Bob',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
            {
            "import_path": "chatterbot.logic.BestMatch",
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.30
        },
        'chatterbot.logic.MathematicalEvaluation',
        #'chatterbot.logic.TimeLogicAdapter'
    ],
    database_uri='sqlite:///database.sqlite3'
)

#train bot - premeditated responses
trainer = ListTrainer(bot)
with open('conversation.txt') as f:
    lines = f.read()
lines = lines.splitlines()
for i in lines:
    trainer.train(i)
f.close()

#train bot - english corpus
trainer = ChatterBotCorpusTrainer(bot)

trainer.train(
    "chatterbot.corpus.english"
)

name=input("Enter Your Name: ")
print("Welcome to the Bot Service! Let me know how can I help you?")

while True:
    request=input(name+':')
    if request=='Bye' or request =='bye':
        print('Bot: Bye')
        break
    else:
        response=bot.get_response(request)
        print('Bot:',response)