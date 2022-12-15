import telebot
import time
from telebot import types
from threading import Thread
from datetime import datetime

bot = telebot.TeleBot('5780863217:AAG7-Zq0_yB5dBzgUHclz-QFPZ8-E8FCh4Q')     #Токен бота


#===============================+ ФУНКЦІЯ ОТРИМАННЯ НОМЕРУ +=========================

@bot.message_handler(commands=['get_phone_number'])
def get_phone(message):
    ids = []
    with open("phoneNumbers.txt", "r", encoding="utf-8") as f:
        ids = f.readlines()
    for x in ids:
        try:
            if(x.split(" ")[0] == message.text.split(" ")[1]):
                bot.send_message(message.chat.id, "Тримай: " + x.split(" ")[1])
                return
        except:
            bot.send_message(message.chat.id, "Використовуй так: \"/get_phone_number [Прізвище]\"")
            return
    bot.send_message(message.chat.id, "Крутелика не знайдено(")

#====================================================================================


#===============================+ ФУНКЦІЯ СТАРТУ +===================================

@bot.message_handler(commands=['start'])                                    
def start(message):
    mess = f'Hello, {message.from_user.first_name}' 
    if(message.chat.type == "group"):
        if(validation(message.chat.id, "gr")):
            with open("groupsID.txt", "a") as f:
                f.write(str(message.chat.id)+ " " + f"{message.chat.title}" + "\n")
    elif(message.chat.type == "private"):
        if(validation(message.chat.id, "pr")):
            with open("usersID.txt", "a") as f:
                f.write(str(message.chat.id)+ " " + f"{message.from_user.first_name}" + "\n")
    bot.send_message(message.chat.id, mess)

#====================================================================================


#===============================+ ФУНКЦІЯ РОЗСИЛКИ ПО ГРУПАХ +=======================

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

#====================================================================================


#===============================+ ФУНКЦІЯ РОЗСИЛКИ КОРИСТУВАЧАМ +====================

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

#====================================================================================


#===============================+ ДОДАТКОВІ ФУНКЦІЇ +================================ 


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
                if(x.split(" ")[0] == str(id)):
                    return False

            return True
        else:
            return True
    elif(type == "pr"):
        with open("usersID.txt", "r") as f:
            ids = f.readlines()
        if(len(ids) > 0):
            for x in ids:
                print(x, f" = {id}")
                if(x.split(" ")[0] == str(id)):   
                    print(False)
                    return False
            print(True)
            return True
        else:
            return True

#====================================================================================


bot.polling(none_stop=True, interval=0)      #Спосіб запиту на сервер
