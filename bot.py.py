import telebot
from telebot import types



phone_book = {
    'Бабурнич': +380951321834,
    'Боровський': +380968533100,
    'Борщун': +380953648652, 
}

bot = telebot.TeleBot('5780863217:AAG7-Zq0_yB5dBzgUHclz-QFPZ8-E8FCh4Q')
@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Hello, {message.from_user.first_name}'
    bot.send_message(message.chat.id, mess)

@bot.message_handler(commands=['help'])
def help(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    start = types.KeyboardButton('/start')
    phone_number = types.KeyboardButton('Боровський')
    markup.add(start, phone_number)
    bot.send_message(message.chat.id, 'Choose action: ', reply_markup=markup)

@bot.message_handler(commands=['get_phone_number'])
def help(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
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
    markup.add(baburnich, borovskiy, borshchun, vasulchenko, voznuy, gorbatiuk, grinchuk, derkach, kozik, kompaniets, ksendzuk,
               marko, marchenkoa, marchenkoo, obuhivskiy, ognivenko, oliynuchenko, parhomenko, pruimuch,
               protasov, romaniuk, salik, safonov, safronov, sorokotiaga, startseva, tsumbaliuk, shpuchka)
    bot.send_message(message.chat.id, 'Choose action: ', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_phone_number(message):
    last_name = message.text
    number = phone_book.get(last_name)
    bot.send_message(message.chat.id, str(number))


bot.polling(none_stop=True)
