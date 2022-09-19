import telebot
from telebot import types
import binance_script

bot=telebot.TeleBot("1597496144:AAGukHlg_wigl2YA7-JYk1Ys_0Ai6Dx8Eq8")
markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
btn1 = types.KeyboardButton('Новости')
btn2 = types.KeyboardButton('Курс валют')
btn3 = types.KeyboardButton('Помощь')
btn4 = types.KeyboardButton('Стакан объём')
markup1.add(btn1, btn2, btn3, btn4)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!', parse_mode='html',reply_markup=markup1)

@bot.message_handler(content_types=['text'])
def mess(message):
    get_message_bot = message.text.strip().lower()
    if (get_message_bot == "помощь"):
        help(message)
    elif(get_message_bot == "стакан объём"):
        cup(message)
    else:
        bot.send_message(message.chat.id, 'Я не совсем Вас понимаю. Попробуйте использовать кнопки ниже')

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id,"С помощью этого бота вы сможете:\nУзнавать курс ключевых криптовалют\nКонтролировать состояние своего портфеля\nБыть в курсе всех ноостей мира криптовалют", parse_mode='html', reply_markup=markup1)

def cup(message):
    bot.send_message(message.chat.id, "Введите название монеты", parse_mode='html')
    bot.register_next_step_handler(message)
    token=binance_script.Start_interface(message.text)
    bot.send_message(message.chat.id, token.check())


bot.polling(none_stop=True)