import telebot
from telebot import types

API_TOKEN = '6265892037:AAFv23erM049NbdhczXU4aPe8ZcbqGZgF_o'

bot = telebot.TeleBot(API_TOKEN)

counterQuestion = 0
questions = {
    'Какой национальный цветок Японии? 1.Сакура 2.Ромашка 3.Роза 4.Лилия': '1',
    'Сколько дней нужно, чтобы Земля совершила оборот вокруг Солнца? 1.364 2.367 3.365 4.370': '3',
    'Сколько полос на флаге США? 1.9 2.10 3.13 4.15': '3',
    'Какое животное можно увидеть на логотипе Porsche? 1.Леопард 2.Кенгуру 3.Слон 4.Лошадь': '4',
    'Сколько элементов в периодической таблице? 1.118 2.120 3.116 4.121': '1',
}


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет ✌️, ты готов?")


@bot.message_handler(commands=['start_question'])
def send_start(message):
    bot.send_message(message.chat.id, "Тогда погнали!")
    send_question(message)


def send_question(message):
    global counterQuestion
    key = list(questions)[counterQuestion]
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
    answer = list(questions.values())[counterQuestion]

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
