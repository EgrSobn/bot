import telebot
from telebot.types import Chat

token = #'TOKEN'
bot = telebot.TeleBot(token)
chat_id = #CHAT_ID

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, text=f'Привет, <b>{message.from_user.first_name} {message.from_user.last_name}</b>! Я твой помошник по связи с "Лавандой". Ты можешь мне предложить любую книгу, а я передам твои пожелания автору подкаста)', parse_mode='html')

@bot.message_handler(func=lambda messege: True)
def echo_messege(message):
    bot.send_message(chat_id=chat_id, text=f'Аккаунт {message.from_user.first_name} {message.from_user.last_name} написал: <b>{message.text}</b>', parse_mode='html')
    bot.send_message(message.chat.id, text=f'Спасибо {message.from_user.first_name} {message.from_user.last_name}, мы тебя очень любим :3', parse_mode='html')

bot.polling()
