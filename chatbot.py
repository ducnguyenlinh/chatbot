from chatterbot import ChatBot

chatbot = ChatBot(
  'CoronaBot',
  storage_adapter='chatterbot.storage.SQLStorageAdapter',
  logic_adapters=[
    'chatterbot.logic.MathematicalEvaluation',
    'chatterbot.logic.TimeLogicAdapter',
    'chatterbot.logic.BestMatch',
    {
      'import_path': 'chatterbot.logic.BestMatch',
      'default_response': 'I am sorry, but I do not understand. I am still learning.',
      'maximum_similarity_threshold': 0.90
    }
  ]
)

# Training With Own Questions
from chatterbot.trainers import ListTrainer

trainer = ListTrainer(chatbot)
training_data_question_answer = open('training_data/question_answer.txt').read().splitlines()
training_data_personal_answer = open('training_data/personal_answer.txt').read().splitlines()
trainer.train(training_data_question_answer + training_data_personal_answer)
