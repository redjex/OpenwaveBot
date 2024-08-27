import telebot
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import random
from urllib.request import urlopen
# Указываем токен вашего бота
API_TOKEN = 'YOUR_TOKEN'
bot = telebot.TeleBot(API_TOKEN)



Anwens = ["Мой разработчик не говорил что говорить >_<", "Слушай я не знаю", "Подумай еще, я тебя не понимаю", "Думаю тебе самому нужно поискать ответ *_-", "Все понимаю, но кроме этого"]



# Команда /start - приветствие и предложение выбора
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = InlineKeyboardMarkup()
    # Создаем кнопки
    btn1 = InlineKeyboardButton("Профиль", callback_data="option_1")
    btn2 = InlineKeyboardButton("Товары", callback_data="option_2")
    btn3 = InlineKeyboardButton("Статистика продавца", callback_data="option_3")
    btn4 = InlineKeyboardButton("<3", callback_data="option_4")
    # Добавляем кнопки в разметку
    markup.add(btn1, btn2)
    markup.add(btn3, btn4)
    bot.send_photo(message.chat.id, "https://upload.wikimedia.org/wikipedia/commons/f/f5/Pic-vk-allaboutme-ava-2.jpg",)
    bot.send_message(message.chat.id, f"Привет {message.from_user.username}!\n\nВыберите один из вариантов:", reply_markup=markup)
@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text == ".ыефке":
        bot.send_message(message.chat.id, "Напиши нормально и не позорься.")
    else:
        bot.send_message(message.chat.id, random.choice(Anwens))

lvl1_2 = 0
lvl3_4 = 0
lvl5_6 = 0
lvl7_8 = 0
lvl9_10 = 0


# Обработчик нажатий на кнопки
def increase_lvl1_2():
    global lvl1_2  # Объявляем, что мы хотим использовать глобальную переменную
    lvl1_2 += 1  # Увеличиваем значение переменной на 1
def increase_lvl3_4():
    global lvl3_4
    lvl3_4 += 1
def increase_lvl5_6():
    global lvl5_6
    lvl5_6 += 1
def increase_lvl7_8():
    global lvl7_8
    lvl7_8 += 1
def increase_lvl9_10():
    global lvl9_10
    lvl9_10 += 1

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "option_1":

        markup = InlineKeyboardMarkup()
        btn1 = InlineKeyboardButton("Оценить💗", callback_data="grade")
        btn2 = InlineKeyboardButton("Назад⬅", callback_data="back")
        btn3 = InlineKeyboardButton("VK", url="vk.com/redjex")
        btn4 = InlineKeyboardButton("Telegram", url="t.me/redjexs")
        # Добавляем кнопки в разметку
        markup.add(btn3, btn4)
        markup.add(btn1, btn2)
        bot.send_message(call.message.chat.id, "Если сильно интересно то можешь посетить мои страницы в соц.сетях:\nVk - vk.com/redjex\nt.me/redjexs\n\nИ даже оценить их по шкале от 1 до 10", reply_markup=markup)
    elif call.data == "option_2":
        print("hello")
    elif call.data == "option_3":
        markup = InlineKeyboardMarkup()
        btn1 = InlineKeyboardButton("Назад⬅", callback_data="back")
        markup.add(btn1)
        bot.send_message(call.message.chat.id, f"Оценки пользователей:\n\n10-9 = {lvl9_10}.\n8-7 = {lvl7_8}.\n6-5 = {lvl5_6}.\n4-3 = {lvl3_4}.\n2-1 = {lvl1_2}.",reply_markup=markup)
        print(lvl1_2,lvl3_4,lvl5_6,lvl7_8,lvl9_10)
    elif call.data == "option_4":
        bot.send_message(call.message.chat.id, "I love you x2")
    elif call.data == "back":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        markup = InlineKeyboardMarkup()
        # Создаем кнопки
        btn1 = InlineKeyboardButton("Профиль", callback_data="option_1")
        btn2 = InlineKeyboardButton("Товары", callback_data="option_2")
        btn3 = InlineKeyboardButton("Статистика продавца", callback_data="option_3")
        btn4 = InlineKeyboardButton("<3", callback_data="option_4")
        # Добавляем кнопки в разметку
        markup.add(btn1, btn2)
        markup.add(btn3, btn4)
        bot.send_message(message.chat.id, f"Привет {message.from_user.username}\n\nВыберите один из вариантов:",reply_markup=markup)
    elif call.data == "grade":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        markup = InlineKeyboardMarkup()
        # Создаем кнопки
        btn1 = InlineKeyboardButton("1-2", callback_data="1-2")
        btn2 = InlineKeyboardButton("3-4", callback_data="3-4")
        btn3 = InlineKeyboardButton("5-6", callback_data="5-6")
        btn4 = InlineKeyboardButton("7-8", callback_data="7-8")
        btn5 = InlineKeyboardButton("9-10", callback_data="9-10")
        btn6 = InlineKeyboardButton("Назад⬅", callback_data="back")
        # Добавляем кнопки в разметку
        markup.add(btn1, btn2)
        markup.add(btn3, btn4)
        markup.add(btn5, btn6)
        bot.send_message(call.message.chat.id, "Выбери параметр оценки.", reply_markup=markup)
    elif call.data == "1-2":
        markup = InlineKeyboardMarkup()
        btn6 = InlineKeyboardButton("Назад⬅", callback_data="option_1")
        markup.add(btn6)
        bot.send_message(call.message.chat.id, "Ваш ответ записан!", reply_markup=markup)
        increase_lvl1_2()
    elif call.data == "3-4":
        markup = InlineKeyboardMarkup()
        btn6 = InlineKeyboardButton("Назад⬅", callback_data="option_1")
        markup.add(btn6)
        bot.send_message(call.message.chat.id, "Ваш ответ записан!", reply_markup=markup)
        increase_lvl3_4()
    elif call.data == "5-6":
        markup = InlineKeyboardMarkup()
        btn6 = InlineKeyboardButton("Назад⬅", callback_data="option_1")
        markup.add(btn6)
        bot.send_message(call.message.chat.id, "Ваш ответ записан!", reply_markup=markup)
        increase_lvl5_6()
    elif call.data == "7-8":
        markup = InlineKeyboardMarkup()
        btn6 = InlineKeyboardButton("Назад⬅", callback_data="option_1")
        markup.add(btn6)
        bot.send_message(call.message.chat.id, "Ваш ответ записан!", reply_markup=markup)
        increase_lvl7_8()
    elif call.data == "9-10":
        markup = InlineKeyboardMarkup()
        btn6 = InlineKeyboardButton("Назад⬅", callback_data="option_1")
        markup.add(btn6)
        bot.send_message(call.message.chat.id, "Ваш ответ записан!", reply_markup=markup)
        increase_lvl9_10()
    else:
        bot.send_message(call.message.chat.id, "Неизвестный выбор")


# Запуск бота
bot.polling(none_stop=True)
