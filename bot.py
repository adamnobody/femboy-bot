#pip install pytelegrambotapi

from images import ImagesLoader
from dub import Dub
import threading
import random
import telebot


TOKEN = "5646601158:AAFj4SvlMvP50qW1vM7BVOgm9qleD6Ge7G4"

tb = telebot.TeleBot(TOKEN)

# Creates images.
imageLoader = ImagesLoader()
imageLoader.loadImages()


@tb.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/help":
        tb.send_message(message.from_user.id, "Список команд:\n1. /myphoto - вывод фотографии с вами;\n2. /joke - вывести анекдот;\n3. /makarova - вывод мнения бота о преподавателе;")
    elif message.text == "/joke":
        tb.send_message(message.from_user.id, "Эстонец поймал золотую рыбку, снял ее с крючка, а она говорит ему:\n- Отпусти меня, я исполню любое твое желание.\nВ ответ на это эстонец берет ее за хвост и со всей дури лупит ее об дерево со словами:\n- Не на-до раз-го-ва-ри-вать со мной по русс-ки.")
    elif message.text == "/showmeyourself":
        send_photo(message)
    elif message.text == "/myphoto":
        send_photo(message)
    elif message.text == "/start":
        tb.send_message(message.from_user.id, "Хочешь посмотреть на себя? введи /myphoto")
    elif "/casino" in message.text:
        if "/casino" in message.text:
            name = message.text.split(' ')[-1]
            dub = Dub(name, message.from_user.id, 0, 0)
            tb.send_message(message.from_user.id, f"Имя вашего древа - {dub.name}")
    elif message.text == "/waltuh":
        file = open("ogorod.txt").read().split("\n")
        ebilo = []
        grzegorz = {}
        obratny_grzegorz = [] # what the fuck?
        for hueta in file:
            ebilo.append(hueta.split(" "))
            grzegorz[hueta.split(" ")[1]] = []
        for hueeta in ebilo:
            pablo = grzegorz[hueeta[1]]
            for huueta in ebilo:
                if huueta[1] == hueeta[1]:
                    pablo.append(huueta)
            for suka in pablo:
                print(pablo)
                grzegorz[hueta.split(' ')[1]].append(suka)
        file.close()
        # {userid: [[]]}
    elif message.text == "/dubs":
        ogorod = getDub()
        for dub in ogorod:
            tb.send_message(message.from_user.id, dub)
    else:
        tb.send_message(message.from_user.id, "Фигню несешь, поехавший. Хочешь посмотреть на себя? введи /myphoto")

"""whose breath smells of the master's cum
whose breath smells of the master's cum
whose breath smells of the master's cum
whose breath smells of the master's cum
whose breath smells of the master's cum
whose breath smells of the master's cum
whose breath smells of the master's cum
whose breath smells of the master's cum"""

def getDub():
    with open("ogorod.txt") as ogorod:
        dubs = ogorod.read().split('\n')
    return dubs


@tb.message_handler(commands=['myphoto'])
def send_photo(message):
    if message.text == "/show-me-yourself":
        tb.send_chat_action(message.chat.id, 'upload_photo')
        img = open('1.jpg', 'rb')
        tb.send_photo(message.chat.id, img, reply_to_message_id=message.message_id)
        img.close()
    elif message.text == "/myphoto":
        tb.send_chat_action(message.chat.id, 'upload_photo')

        imageName = ''
        random.seed(random.randint(1, 100000))

        while True:
            imageName = f'{random.randint(0, imageLoader.getCountOfImages())}.jpg'
            if imageName == '1.jpg':
                continue
            break
        
        img = open(f'{imageName}', 'rb')
        tb.send_photo(message.chat.id, img, reply_to_message_id=message.message_id)
        img.close()

tb.polling()