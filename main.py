import telebot
import constants
from telebot import types

bot = telebot.TeleBot(constants.API_TOKEN)

counterQuestion = 0


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет ✌️, ты готов?")


@bot.message_handler(commands=['start_question'])
def send_start(message):
    bot.send_message(message.chat.id, "Тогда погнали!")
    send_question(message)


def send_question(message):
    global counterQuestion
    key = list(constants.questions)[counterQuestion]
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("1")
    item2 = types.KeyboardButton("2")
    item3 = types.KeyboardButton("3")
    item4 = types.KeyboardButton("4")
    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, key, reply_markup=markup)


@bot.message_handler(content_types='text')
def check_answer(message):
    global counterQuestion
    answer = list(constants.questions.values())[counterQuestion]

    if message.text == answer:
        bot.send_message(message.chat.id, "И это правильный ответ!")
    else:
        bot.send_message(message.chat.id, "К сожалению вы проиграли")
    if counterQuestion != 5:
        counterQuestion += 1
        send_question(message)
    else:
        counterQuestion = 0
        bot.send_message(message.chat.id, "Поздравляю, вы победитель!")


bot.infinity_polling()
