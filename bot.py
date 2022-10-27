#pip install pytelegrambotapi

import telebot
import time
import urllib


TOKEN = "5646601158:AAFj4SvlMvP50qW1vM7BVOgm9qleD6Ge7G4"


tb = telebot.TeleBot(TOKEN)


@tb.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Макарова":
        tb.send_message(message.from_user.id, "Лучший преподаватель, однозначно")
    elif message.text == "/joke":
        tb.send_message(message.from_user.id, "Эстонец поймал золотую рыбку, снял ее с крючка, а она говорит ему:\n- Отпусти меня, я исполню любое твое желание.\nВ ответ на это эстонец берет ее за хвост и со всей дури лупит ее об дерево со словами:\n- Не на-до раз-го-ва-ри-вать со мной по русс-ки.")
    elif message.text == "/show-me-yourself":
        send_photo(message)
    elif message.text == "/myphoto":
        send_photo(message)
    elif message.text == "/start":
        tb.send_message(message.from_user.id, "Хочешь посмотреть на себя? введи /myphoto")
    else:
        tb.send_message(message.from_user.id, "Фигню несешь, поехавший. Хочешь посмотреть на себя? введи /myphoto")


@tb.message_handler(commands=['myphoto'])
def send_photo(message):
    if message.text == "/show-me-yourself":
        tb.send_chat_action(message.chat.id, 'upload_photo')
        img = open('femboy.jpg', 'rb')
        tb.send_photo(message.chat.id, img, reply_to_message_id=message.message_id)
        img.close()
    elif message.text == "/myphoto":
        tb.send_chat_action(message.chat.id, 'upload_photo')
        img = open('out.jpg', 'rb')
        tb.send_photo(message.chat.id, img, reply_to_message_id=message.message_id)
        img.close()

        
tb.polling()