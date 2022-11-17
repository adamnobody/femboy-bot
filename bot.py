#pip install pytelegrambotapi

from images import ImagesLoader
from dub import Dub
import threading
import random
import telebot


def createDubs():
    global DUBY
    # Данная хуебредень создает словарь с парами КЛЮЧ: <НИХУЯ>,
    # при этом ключ берется из динамически создаваемого списка.
    # Данный список просто состоит из айдишников, которые мы достаем с помощью id.split(' ')[1].
    # file - список строк с др(о/е)вами, собсна, мы перебираем этот список и достаем айдишники,
    # после чего суем их в качестве ключа в создаваемый словарь. Значение к этому словарю будет
    # тупо пустой список.
    # Далее просто перебираются все ключи, которые имеются в словаре,
    # для каждого ключа идет перебор древа, которое содержится в file.
    # Создается шаблон словаря информации о древе, который добавляется
    # к определеннному ключу только при соответствии непосредственно ключа и имеющегося 
    # айдишника в древе. При этом мы имеем словарь вида { ID: [ {}, ], }.
    # Просто словарь айдишников пользователей, к каждому айдишнику создается список,
    # в котором хранится в виде словарей инфа о каждом дубе, что есть у пользователя.
    # Доступ к инфе осуществляется не в виде ссанных обращений по индексу, как в цикле ниже,
    # а с помощью барских обращений к имени ключа. Удобно, хуй ли.
    # Ебаться подано, господа.
    
    file = open("ogorod.txt").read().split('\n')
        
    DUBY = {key: [] for key in [id.split(' ')[1] for id in file]}

    for id in DUBY.keys():
        for drevo in file:
            info = {"Name": drevo.split(' ')[0],
                    "Growth": drevo.split(' ')[2],
                    "Apples": drevo.split(' ')[3],}
            if id == drevo.split(' ')[1]:
                DUBY[drevo.split(' ')[1]].append(info)

TOKEN = "5646601158:AAFj4SvlMvP50qW1vM7BVOgm9qleD6Ge7G4"
DUBY = {}
createDubs()

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
            createDubs()
            tb.send_message(message.from_user.id, f"Имя вашего древа - {dub.name}")
    elif "/zapoi" in message.text:
        nameWater = message.text.split(' ')[-1]
        id = str(message.from_user.id)
        if id in DUBY.keys():
            duby = DUBY[id]
            for dub in duby:
                if dub["Name"] == nameWater:
                    dubGrowth = int(dub["Growth"])
                    dubApples = int(dub["Apples"])
                    dubGrowth += 1
                    dub["Growth"] = str(dubGrowth)
                    if dubGrowth % 5 == 0:
                        dubApples += 1
                        dub["Apples"] = str(dubApples)
                        tb.send_message(message.from_user.id, f"Ваше дерево {nameWater} дало плоды.")
                    tb.send_message(message.from_user.id, f"Вы полили своё дерево - {nameWater}")

    elif message.text == "/waltuh":
        id = str(message.from_user.id)
        if id in DUBY.keys():
            duby = DUBY[id]
            msg = ''
            for dub in duby:
                msg += f'Имя: {dub["Name"]} Рост: {dub["Growth"]} Яблоки: {dub["Apples"]}\n'
            tb.send_message(message.from_user.id, msg)
        else:
            tb.send_message(message.from_user.id, "У вас нет дубов. Создайте с помощью команды /casino <Имя дуба>.")
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