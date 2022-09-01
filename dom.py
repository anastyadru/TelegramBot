# 5415297269:AAHAGN0uex8dZdcRFmqZf0fr6Hp6qCLvqa8

import telebot
from telebot import types

token='5415297269:AAHAGN0uex8dZdcRFmqZf0fr6Hp6qCLvqa8'
bot = telebot.TeleBot(token)


def create_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    primer_btn = types.InlineKeyboardButton(text="Вывести решенный пример", callback_data='1')
    stix_btn = types.InlineKeyboardButton(text="Вывести отрывок стиха", callback_data='2')
    kartina_btn = types.InlineKeyboardButton(text="Вывести картинку гор", callback_data='3')
    keyboard.add(primer_btn)
    keyboard.add(stix_btn)
    keyboard.add(kartina_btn)
    return keyboard

@bot.message_handler(commands=['start'])
def start_bot(message):
    keyboard=create_keyboard()
    bot.send_message(
        message.chat.id,
        "Здравствуйте! Какую следующую функцию вы хотите, чтобы я выполнил?",
        reply_markup=keyboard
    )

@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
    keyboard = create_keyboard()
    if call.message:
        if call.data=='1':
            primer = '2+2=4'
            bot.send_message(
                chat_id=call.message.chat.id,
                text=primer,
                reply_markup=keyboard)
            text.close()
        if call.data=='2':
            stix = 'Буря мглою небо кроет, Вихри снежные крутя..'
            bot.send_message(
                chat_id=call.message.chat.id,
                text=stix,
                reply_markup=keyboard)
            text.close()
        if call.data=='3':
            img = open('Moench_2339.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="Картинка горы",
                reply_markup=keyboard)
            img.close()

if __name__=="__main__":
    bot.polling(none_stop=True)