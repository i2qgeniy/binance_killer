import telebot
from telebot import types
import binance_script

bot=telebot.TeleBot("1597496144:AAGukHlg_wigl2YA7-JYk1Ys_0Ai6Dx8Eq8")
btn1 = types.KeyboardButton('Новости')
btn2 = types.KeyboardButton('Крут баланса')
btn3 = types.KeyboardButton('Помощь')
btn4 = types.KeyboardButton('Стакан объём')
btn5 = types.KeyboardButton('Показать весь объем')

user=0
@bot.message_handler(commands=['start'])
def start(message):
    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3, one_time_keyboard=True)
    markup1.add(btn1, btn2, btn3, btn4, btn5)
    global user
    user=binance_script.User(message.chat.id)
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!', parse_mode='html',reply_markup=markup1)

@bot.message_handler(content_types=['text'])
def mess(message):
    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3, one_time_keyboard=True)
    markup1.add(btn1, btn2, btn3, btn4, btn5)
    get_message_bot = message.text.strip().lower()
    if (get_message_bot == "помощь"):
        help(message)
    elif(get_message_bot == "стакан объём"):
        cup(message)
    elif(get_message_bot == "крут баланса"):
        crut(message)
    elif (get_message_bot == "показать весь объем"):
        volume(message)
    else:
        bot.send_message(message.chat.id, 'Я не совсем Вас понимаю. Попробуйте использовать кнопки ниже')

@bot.message_handler(commands=['help'])
def help(message):
    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3, one_time_keyboard=True)
    markup1.add(btn1, btn2, btn3, btn4, btn5)
    bot.send_message(message.chat.id,"С помощью этого бота вы сможете:\nУзнавать курс ключевых криптовалют\nКонтролировать состояние своего портфеля\nБыть в курсе всех ноостей мира криптовалют", parse_mode='html', reply_markup=markup1)

def cup(message):
    bot.send_message(message.chat.id, "Введите название монеты", parse_mode='html')
    bot.register_next_step_handler(message, out)

def out(message):
    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    markup1.add(btn1, btn2, btn3, btn4, btn5)
    try:
        token=binance_script.Start_interface(message.chat.id,message.text)
        bot.send_message(message.chat.id, str(token.info()))
        info=token.check()
        bot.send_message(message.chat.id, f'Продажа: {info[0]}\nОбъём: {info[1]}\nПокупка: {info[2]}\nОбъём покупки: {info[3]}\n',parse_mode='html',reply_markup=markup1)
    except BaseException:
        bot.send_message(message.chat.id, "Вы ввели неправильное название монеты")

def volume(message):
    bot.send_message(message.chat.id, "Введите название монеты", parse_mode='html')
    bot.register_next_step_handler(message, volume_2)

def volume_2(message):
    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    markup1.add(btn1, btn2, btn3, btn4, btn5)
    photo = open('graph.png', 'rb')
    bot.send_photo(message.chat.id, photo=photo)
    try:

        token=binance_script.Start_interface(message.chat.id,message.text)
        info=token.get_volume(2, 200)
        bot.send_message(message.chat.id, f'Объём продаж: {info[0]}\nОбъём покупок: {info[1]}\n',parse_mode='html',reply_markup=markup1)
    except BaseException:
        bot.send_message(message.chat.id, "Вы ввели неправильное название монеты")


def crut(message):
    global user
    if user.check_user()=='1':
        bot.send_message(message.chat.id, 'Work')
    else:
        bot.send_message(message.chat.id, 'Зарегистриуйтесь, введя апи кей и секрет кей через двоеточие')
        bot.register_next_step_handler(message, checker)


def checker(message):
    global user
    user.init_api(message.text.split(':'))

bot.polling(none_stop=True)