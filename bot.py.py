import telebot
import time
from telebot import types
from threading import Thread
from datetime import datetime

bot = telebot.TeleBot('5780863217:AAG7-Zq0_yB5dBzgUHclz-QFPZ8-E8FCh4Q')     #Токен бота

phone_book = {                                                              #Номера телефону групи
    'бабурнич': +380951321834,              
    'боровський': +380968533100,            
    'борщун': +380953648652,                
}



#def time_message():
#    while True:
#        time.sleep(1)
#        if(datetime.now().strftime("%H") == "10" and datetime.now().strftime("%M") == "51" and datetime.now().strftime("%S") == "01"):
#            bot.send_message(528510018, "nice")

#th = Thread(target=time_message)
#th.start()

def validation(id, type):
    ids = []
    if(type == "gr"):
        with open("groupsID.txt", "r") as f:
            ids = f.readlines()
        if(len(ids) > 0):
            for x in ids:
                if(x.split(" ")[0] == id):
                    return False

            return True
        else:
            return True
    elif(type == "pr"):
        with open("usersID.txt", "r") as f:
            ids = f.readlines()
        if(len(ids) > 0):
            for x in ids:
                if(x.split(" ")[0] == id):                    
                    return False

            return True
        else:
            return True

@bot.message_handler(commands=['brgr'])
def brodcast_group(message):
    ids = []
    str = ""
    for x in range(len(message.text.split(" ")) - 1):
        str += message.text.split(" ")[x + 1] + " "
    with open("groupsID.txt", "r") as f:
        ids = f.readlines()
        if(len(ids) > 0):
            for x in ids:
                if(len(str) > 0):
                    bot.send_message(x.split(" ")[0], str)

@bot.message_handler(commands=['brusr'])
def brodcast_users(message):
    ids = []
    str = ""
    for x in range(len(message.text.split(" ")) - 1):
        str += message.text.split(" ")[x + 1] + " "
    with open("usersID.txt", "r") as f:
        ids = f.readlines()
        if(len(ids) > 0):
            for x in ids:
                if(len(str) > 0):
                    bot.send_message(x.split(" ")[0], str)

@bot.message_handler(commands=['start'])                                    #Команда /start
def start(message):
    mess = f'Hello, {message.from_user.first_name}'
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    userid = types.KeyboardButton('Get ID')
    get_phone = types.KeyboardButton('Phone numbers')
    markup.add(userid, get_phone);    
    if(message.chat.type == "group"):
        if(validation(message.chat.id, "gr")):
            with open("groupsID.txt", "a") as f:
                f.write(str(message.chat.id)+ " " + f"{message.chat.title}" + "\n")
    elif(message.chat.type == "private"):
        if(validation(message.chat.id, "pr")):
            with open("usersID.txt", "a") as f:
                f.write(str(message.chat.id)+ " " + f"{message.from_user.first_name}" + "\n")
    bot.send_message(message.chat.id, mess, reply_markup=markup)

def numbers(message):                                                       #Фамілії групи 
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    menu = types.KeyboardButton('Головне меню')
    baburnich = types.KeyboardButton('Бабурнич')
    borovskiy = types.KeyboardButton('Боровський')
    borshchun = types.KeyboardButton('Борщун')
    vasulchenko = types.KeyboardButton('Васильченко')
    voznuy = types.KeyboardButton('Возний')
    gorbatiuk = types.KeyboardButton('Горбатюк')
    grinchuk = types.KeyboardButton('Грінчук')
    derkach = types.KeyboardButton('Деркач')
    kozik = types.KeyboardButton('Козік')
    kompaniets = types.KeyboardButton('Компанієць')
    ksendzuk = types.KeyboardButton('Ксендзук')
    marko = types.KeyboardButton('Марко')
    marchenkoa = types.KeyboardButton('МарченкоА')
    marchenkoo = types.KeyboardButton('МарченкоО')
    obuhivskiy = types.KeyboardButton('Обухівський')
    ognivenko = types.KeyboardButton('Огнівенко')
    oliynuchenko = types.KeyboardButton('Олійниченко')
    parhomenko = types.KeyboardButton('Пархоменко')
    pruimuch = types.KeyboardButton('Приймич')
    protasov = types.KeyboardButton('Протасов')
    romaniuk = types.KeyboardButton('Романюк')
    salik = types.KeyboardButton('Салік')
    safonov = types.KeyboardButton('Сафонов')
    safronov = types.KeyboardButton('Сафронов')
    sorokotiaga = types.KeyboardButton('Сорокотяга')
    startseva = types.KeyboardButton('Старцева')
    tsumbaliuk = types.KeyboardButton('Цимбалюк')
    shpuchka = types.KeyboardButton('Шпичка')
    markup.add(menu, baburnich, borovskiy, borshchun, vasulchenko, voznuy, gorbatiuk, grinchuk, derkach, kozik, kompaniets, ksendzuk,
               marko, marchenkoa, marchenkoo, obuhivskiy, ognivenko, oliynuchenko, parhomenko, pruimuch,
               protasov, romaniuk, salik, safonov, safronov, sorokotiaga, startseva, tsumbaliuk, shpuchka)
    bot.send_message(message.chat.id, 'Choose action: ', reply_markup=markup)

@bot.message_handler(content_types=['text'])                                #Обробка запитів
def read_user_text(message):
    if(message.text.lower() == 'головне меню'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        userid = types.KeyboardButton('Get ID')
        get_phone = types.KeyboardButton('Phone numbers')
        markup.add(userid, get_phone)
        bot.send_message(message.chat.id,'Choose action: ', reply_markup=markup)
    if(message.text.lower() == 'get id'):
        bot.send_message(message.chat.id, f'{message.from_user.first_name}:{message.from_user.id}')
    if(message.text.lower() == 'phone numbers'):
        numbers(message);
    try:
        if(phone_book.fromkeys(message.text.lower())):
            bot.send_message(message.chat.id, phone_book.get(message.text.lower()))
    except:
        pass


bot.polling(none_stop=True, interval=0)                                     #Багатопоточність
