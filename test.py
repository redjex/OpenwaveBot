import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import random
# Указываем токен вашего бота
API_TOKEN = 'YOU_TOKEN'
bot = telebot.TeleBot(API_TOKEN)



Anwens = ["Мой разработчик не говорил что говорить >_<", "Слушай я не знаю", "Подумай еще, я тебя не понимаю", "Думаю тебе самому нужно поискать ответ *_-", "Все понимаю, но кроме этого"]



# Команда /start - приветствие и предложение выбора
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = InlineKeyboardMarkup()

    # Создаем кнопки
    btn1 = InlineKeyboardButton("<3", callback_data="option_1")
    btn2 = InlineKeyboardButton("<3", callback_data="option_2")
    btn3 = InlineKeyboardButton("<3", callback_data="option_3")
    btn4 = InlineKeyboardButton("<3", callback_data="option_4")
    # Добавляем кнопки в разметку
    markup.add(btn1, btn2)
    markup.add(btn3, btn4)
    bot.send_message(message.chat.id, "Привет! Выберите один из вариантов:", reply_markup=markup)

@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text == ".ыефке":
        bot.send_message(message.chat.id, "Напиши нормально и не позорься.")
    else:
        bot.send_message(message.chat.id, random.choice(Anwens))



# Обработчик нажатий на кнопки

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "option_1":
        bot.send_message(call.message.chat.id, "Люблю тебя")
    elif call.data == "option_2":
        bot.send_message(call.message.chat.id, "I love you")
    elif call.data == "option_3":
        bot.send_message(call.message.chat.id, "Артем точно гей")
    elif call.data == "option_4":
        bot.send_message(call.message.chat.id, "I love you x2")
    else:
        bot.send_message(call.message.chat.id, "Неизвестный выбор")


# Запуск бота
bot.polling(none_stop=True)
