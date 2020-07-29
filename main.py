import telebot

bot = telebot.TeleBot('1106764268:AAGYI5tr6pWv_apqhEVq8hXAWZZQ_ie0zR8')


@bot.message_handler(commands=['start'])
def start(message):
    send_mess = f"<b>Привет {message.from_user.first_name} {message.from_user.last_name}</b>!\nКакое направление тебя интересует?"
    bot.send_message(message.chat.id, send_mess, parse_mode='html')


bot.polling(none_stop=True)

