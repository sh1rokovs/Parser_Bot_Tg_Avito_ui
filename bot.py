import telebot
from telebot import types

bot = telebot.TeleBot('1106764268:AAGYI5tr6pWv_apqhEVq8hXAWZZQ_ie0zR8')


@bot.message_handler(commands=['website'])
def open_website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Перейти к оплате", url="https://www.free-kassa.ru"))
    bot.send_message(message.chat.id,
                     "Отличный выбор, нажмите на кнопку ниже и купите решение",
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['insta'])
def instagram(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Перейти в Инстаграм", url="https://www.instagram.com"))
    bot.send_message(message.chat.id, "Нажмите на кнопку ниже и посмотрите отзывы в инсте", parse_mode='html',
                     reply_markup=markup)


@bot.message_handler(commands=['vk'])
def vk(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Посетить группу Вк", url="https://vk.com"))
    bot.send_message(message.chat.id, "Нажмите на кнопку ниже и посмотрите отзывы в вк", parse_mode='html',
                     reply_markup=markup)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    btn1 = types.KeyboardButton('Купить решение')
    btn2 = types.KeyboardButton('Инста')
    btn3 = types.KeyboardButton('Вк')
    markup.add(btn1, btn2, btn3)
    send_mess = f"<b>Привет {message.from_user.first_name} {message.from_user.last_name}</b>!\n" \
                f" Отличная способ заработать денюшку, играя в игру!\n" \
                f" Все максимально просто и честно!\n" \
                f" Вывод средств момементально, любым способом!\n" \
                f" 1. Вложить в биткоин\n" \
                f" 2. Купить схему\n" \
                f" 3. Начать зарабатывать\n" \
                f" Какое решение тебя интересует?\n"
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def mess(message):
    get_message_bot = message.text.strip().lower()

    if get_message_bot == "купить решение":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Купить решение')
        btn2 = types.KeyboardButton('Инста')
        btn3 = types.KeyboardButton('Вк')
        markup.add(btn1, btn2, btn3)
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Купить решение", url="https://www.free-kassa.ru"))

        final_message = "Вы можете купить разные решения на <a href='https://www.free-kassa.ru'>Сайте</a>\n" \
                        "по кнопке ниже"
    elif get_message_bot == "инста":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Купить решение')
        btn2 = types.KeyboardButton('Инста')
        btn3 = types.KeyboardButton('Вк')
        markup.add(btn1, btn2, btn3)
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Посмотреть отзывы", url="https://www.instagram.com"))

        final_message = "Вы можете также посмотреть наши отзывы в <a href='https://www.instagram.ru'>Inste</a>\n" \
                        "по кнопке ниже"
    elif get_message_bot == "вк":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Купить решение')
        btn2 = types.KeyboardButton('Инста')
        btn3 = types.KeyboardButton('Вк')
        markup.add(btn1, btn2, btn3)
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Посмотреть отзывы", url="https://www.vk.com"))

        final_message = "Вы можете также посмотреть наши отзывы в <a href='https://www.vk.com'>Вк</a>\n" \
                        "по кнопке ниже"
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Купить решение')
        btn2 = types.KeyboardButton('Инста')
        btn3 = types.KeyboardButton('Вк')
        markup.add(btn1, btn2, btn3)
        final_message = "Вы можете также посмотреть наши отзывы в <a href='https://www.vk.com'>Вк</a>\n" \
                        "по кнопке ниже"
    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)


bot.polling(none_stop=True)
