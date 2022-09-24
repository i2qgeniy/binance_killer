import telebot
from telebot import types
import binance_script


class current_monet():

    def __init__(self, name):
        self.name = name


class Start():
    def __init__(self, start_butt):
        self.messadge_id = []
        self.markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3, one_time_keyboard=True)
        for btn in start_butt:
            self.markup1.add(types.KeyboardButton(btn))

    def obrabotka(self, sms):
        self.chat_id = sms.chat.id
        self.m = sms
        #self.messadge_id.append(sms.text)
        self.messadge_text = self.m.text.strip().lower()
        if (self.messadge_text == "помощь"):
            print(1)
        elif (self.messadge_text == "стакан объём"):
            self.volume_graph()
        elif (self.messadge_text == "крут баланса"):
            print(3)
        elif (self.messadge_text == "показать весь объем"):
            self.volume()
        else:
            bot.send_message(self.chat_id, 'Я не совсем Вас понимаю. Попробуйте использовать кнопки ниже')

    def get_cryptoname(self, name):
        print('get_start')
        print(name)
        monet = name.text
        print(monet)
        if self.last_opperation == 'volume':
            self.volume(monet)
        elif self.last_opperation == 'volume_graph':
            self.volume_graph(monet)

    def volume(self, monet = '0'):
        if monet == '0':
            print('volume_start')
            bot.send_message(self.chat_id, "Введите название монеты", parse_mode='html')
            a = bot.register_next_step_handler(self.m, self.get_cryptoname)
            print('volume_end')
            print(a)
            self.last_opperation = 'volume'
        else:
            token = binance_script.Start_interface(self.chat_id, monet)
            info = token.get_volume(2, 500)
            bot.send_message(self.chat_id, f'Объём продаж: {info[0]}\nОбъём покупок: {info[1]}\n', parse_mode='html',
                             reply_markup=self.markup1)

    def volume_graph(self, monet = '0'):
        if monet == '0':
            print('graph_start')
            bot.send_message(self.chat_id, "Введите название монеты", parse_mode='html')
            a = bot.register_next_step_handler(self.m, self.get_cryptoname)
            print('graph_end')
            self.last_opperation = 'volume_graph'
        else:
            token = binance_script.Start_interface(self.chat_id, monet)
            info = token.add_volume_graph(30)
            bot.send_message(self.chat_id, 'data add', reply_markup=self.markup1)




bot=telebot.TeleBot("1597496144:AAGukHlg_wigl2YA7-JYk1Ys_0Ai6Dx8Eq8")
start_butt = ['NEWS', 'Крут баланса', 'Помощь', 'Стакан объём', 'Показать весь объем']
btn_none = types.KeyboardButton('По умолчанию')


startt = Start(start_butt)
print(startt)
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!', parse_mode='html')

@bot.message_handler(content_types=['text'])
def mess(message):
    get_message_bot = message.text.strip().lower()
    startt.obrabotka(message)
    print(125125156)



bot.polling(none_stop=True)
'''


@bot.message_handler(commands=['start'])
def start(message):
    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3, one_time_keyboard=True)
    markup1.add(btn1, btn2, btn3, btn4, btn5)
    global user
    user=binance_script.User(message.chat.id)
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!', parse_mode='html')

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
    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3, one_time_keyboard=True)
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


def volume_default(message):
    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3, one_time_keyboard=True)
    markup1.add(btn1, btn2, btn3, btn4, btn5)
    global monet
    print(monet.name)
    try:
        token=binance_script.Start_interface(message.chat.id,monet.name)
        info=token.get_volume(2, message.text)
        bot.send_message(message.chat.id, f'Объём продаж: {info[0]}\nОбъём покупок: {info[1]}\n',parse_mode='html',reply_markup=markup1)
    except BaseException:
        bot.send_message(message.chat.id, "Вы ввели неправильное название монеты",reply_markup=markup1)

def volume_2(message):
    markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3, one_time_keyboard=True)
    markup2.add(btn_none)
    global monet
    monet=current_monet(message.text)
    bot.send_message(message.chat.id, 'Какое количество запросов вы хотите добавить в график?',reply_markup=markup2)
    bot.register_next_step_handler(message,is_default)

def crut(message):
    global user
    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3, one_time_keyboard=True)
    markup1.add(btn1, btn2, btn3, btn4, btn5)
    if user.check_user()=='1':
        bot.send_message(message.chat.id, 'Work',reply_markup=markup1)
    else:
        bot.send_message(message.chat.id, 'Зарегистрируйтесь, введя апи кей и секрет кей через двоеточие')
        bot.register_next_step_handler(message, checker)


def checker(message):
    global user
    user.init_api(message.text.split(':'))
    bot.send_message('Вы успешно зарегистрировались!')

def is_default(message):
    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3, one_time_keyboard=True)
    markup1.add(btn1, btn2, btn3, btn4, btn5)
    get_message_bot = message.text.strip().lower()
    global monet
    print(monet.name)
    if(get_message_bot=='по умолчанию'):
        try:
            token = binance_script.Start_interface(message.chat.id, monet.name)
            info = token.get_volume(2, 200)
            bot.send_message(message.chat.id, f'Объём продаж: {info[0]}\nОбъём покупок: {info[1]}\n', parse_mode='html', reply_markup=markup1)
        except BaseException:
            bot.send_message(message.chat.id, "Вы ввели неправильное название монеты")
    else:
        volume_default(message)


def is_default(message):
    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3, one_time_keyboard=True)
    markup1.add(btn1, btn2, btn3, btn4, btn5)
    get_message_bot = message.text.strip().lower()
    global monet
    print(monet.name)
    if(get_message_bot=='по умолчанию'):
        try:
            token = binance_script.Start_interface(message.chat.id, monet.name)
            info = token.get_volume(2, 200)
            bot.send_message(message.chat.id, f'Объём продаж: {info[0]}\nОбъём покупок: {info[1]}\n', parse_mode='html', reply_markup=markup1)
        except BaseException:
            bot.send_message(message.chat.id, "Вы ввели неправильное название монеты")
    else:
        volume_default(message)

bot.polling(none_stop=True)
'''