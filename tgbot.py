import telebot
from telebot import types
import os

# Создаем бота
bot = telebot.TeleBot("7001654449:AAFMPCM2AMiXOMWIcuFXLSCbSpUy7gfmhfY")
print('in progress...')

url = ""  # Инициализируем глобальные переменные
keys = ""
geo = ""
# users = ['', '']

@bot.message_handler(commands=['start'])
def start_message(message):
    # if message.from_user.id == users:
        markup = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("Создать новый запрос", callback_data='new_request')
        markup.add(item1)
        bot.send_message(message.chat.id, 'Нажмите на кнопку, чтобы добавить запрос', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "new_request")
def new_request(call):
    bot.send_message(call.message.chat.id, "Введите URL (страницу с авито)")
    bot.register_next_step_handler(call.message, get_url)

# Добавить проверку регексом
def get_url(message):
    global url  # Определяем переменные как глобальные
    url = message.text
    bot.send_message(message.chat.id, "Что именно ищем (ключевое слово):")
    bot.register_next_step_handler(message, get_keys)

def get_keys(message):
    global keys
    keys = message.text
    bot.send_message(message.chat.id, "Где ищем? - Населенный пункт для поиска. Если несколько, то через запятую:")
    bot.register_next_step_handler(message, get_geo)

config_dir = os.path.join(os.getcwd(), "config")
count = len(os.listdir(config_dir)) + 1

def get_geo(message):
    global geo
    geo = message.text
    with open(f"/config/{count}.txt", "w", encoding='utf-8') as f:
        f.write("[Avito]\n")
        f.write(f"url = {url}\n")
        f.write("num_ads = 3\n")
        f.write("freq = 1\n")
        f.write(f"keys = {keys}\n")
        f.write("max_price = 100000\n")
        f.write("min_price = 0\n")
        f.write(f"geo = {geo}\n")
    bot.send_message(message.chat.id, "Запрос успешно создан!")


# Запускаем бота
bot.polling()
