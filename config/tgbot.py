import telebot
from telebot import types
import re
import os

bot = telebot.TeleBot("7001654449:AAFMPCM2AMiXOMWIcuFXLSCbSpUy7gfmhfY")
print('in progress...')

dir_path = ''
url = ""  # Инициализируем глобальные переменные
keys = ""
geo = ""
Type = ""
items = ''
# users = ['', '']

@bot.message_handler(commands=['start'])
def start_message(message):
    # if message.from_user.id == users:
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Создать новый запрос", callback_data='name')
    markup.add(item1)
    bot.send_message(message.chat.id, 'Нажмите на кнопку, чтобы добавить запрос', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "name")
def get_url(call):
    bot.send_message(call.message.chat.id, 'Дайте имя объекту')
    bot.register_next_step_handler(call.message, dsm_or_dst)

@bot.callback_query_handler(func=lambda call: call.data == "dsm_or_dst")
def dsm_or_dst(call):
    global dir_path
    dir_path = call.text
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("ДСМ", callback_data='DSM')
    item2 = types.InlineKeyboardButton("ДСТ", callback_data='DST')
    markup.add(item1, item2)
    bot.send_message(call.chat.id, f'Имя объкта "{dir_path}" записано!\n\nИщем технику или материалы (ДСТ или ДСМ) ?', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "DSM")
def dst(call):
    global Type
    global items
    Type = "ДСМ"
    items = ["Асфальтоукладчик", "Каток дорожный", "Бульдозер", "Грейдер", "Экскаватор", "Погрузчик", "Автокран"]
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Далее", callback_data='new_request')
    item2 = types.InlineKeyboardButton("Назад", callback_data='name')
    markup.add(item1, item2)
    bot.send_message(call.chat.id, 'Ищем ДСМ', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "DST")
def dst(call):
    global Type
    global items
    Type = "ДСТ"
    items = ["Асфальтоукладчик", "Каток дорожный", "Бульдозер", "Грейдер", "Экскаватор", "Погрузчик", "Автокран"]
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Далее", callback_data='new_request')
    item2 = types.InlineKeyboardButton("Назад", callback_data='name')
    markup.add(item1, item2)
    bot.send_message(call.message.chat.id, 'Ищем ДСТ', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "new_request")
def new_request(call):
    bot.send_message(call.message.chat.id, "Введите ссылку (страницу с Авито, выбрав соответсвующий раздел и геопозицию)")
    bot.register_next_step_handler(call.message, get_url)

def get_url(message):
    global url
    pattern = r"(https?://)([a-zA-Z0-9_-]+\.)+[a-zA-Z0-9_-]+"
    if re.match(pattern, message.text):
        url = message.text
        bot.send_message(message.chat.id, "Где ищем? - Список населенных пунктов для поиска через запятую.\nПример: Малиновка,Желябино,Павловская Слобода")
        bot.register_next_step_handler(message, get_geo)
    else:
        bot.send_message(message.chat.id, "Ссылка введена некорректно, попробуйте ещё раз:")

def get_geo(message):
    global geo
    geo = message.text
    template = f"""Имя: {dir_path}\nСсылка: {url}\nГеопозиция: {geo}\nКатегория: {Type}"""
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Все верно", callback_data='files')
    item2 = types.InlineKeyboardButton("Не верно", callback_data='name')
    markup.add(item1, item2)
    bot.send_message(message.chat.id, f"Проверьте, все ли верно?\n{template}", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "files")
def new_request(call):
    global geo
    global dir_path
    global url
    global Type
    key=''
    dir_path = f"config/{dir_path.replace(' ', '_') + Type}"
    # Шаблон содержимого файла без строки "keys = "
    template = """[Avito]
    url = {url}
    num_ads = 3
    freq = 1
    keys = {key}
    max_price = 100000
    min_price = 0
    geo = {geo}
    Type = {Type}
    """
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    # Создание файлов
    for index, item in enumerate(items):
        filename = dir_path + f"/config_{index + 1}.ini"  # Даем каждому файлу уникальное имя
        print(filename)
        with open(filename, 'w', encoding='utf-8') as file:
            content = template.format(url=url, key=item, geo=geo, Type=Type)
            file.write(content)

bot.polling()
