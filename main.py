# -*- coding: utf-8 -*-

import telebot
import re


reg = r'хуе|Хуе|хуи|Хуи|Хую|хую|хуе|хуй|Хуй|пизда|Пизда|Пиздец|пиздец|ебал|Ебал|ебаный|Ебаный|ебаная|Ебаная|хуета|Хуета|долбоёб|Долбоёб|ебать|Ебать|ебола|Ебола|ебало|Ебало|пидор|Пидор|хуесос|Хуесос|пиздос|Пиздос|хуйня|Хуйня|нихуя|Нихуя|ебалу|Ебалу|Бля|бля|уебать|Уебвть|пизду|Пизду|уёбок|Уёбок|блядина|Блядина'
token = '1747457928:AAGNz2feoREEeOWZ0Q0KjRxVWGP6_Zn3A0U'

bot = telebot.TeleBot(token)

#upd = bot.get_updates()
#print(upd)

#last_upd = upd[-1]
#message_from_user = last_upd.message
#print(message_from_user)

print(bot.get_me())


@bot.message_handler(content_types=['text'])

def handle_text(message):
    cid = message.chat.id
    if re.findall(reg, message.text) :
        answer1 = re.sub(r'хуй\b|Хуй\b', 'член', message.text)
        answer2 = re.sub(r'пизда|Пизда', 'влагалише', answer1)
        answer3 = re.sub(r'пиздец|Пиздец', 'пипец', answer2)
        answer4 = re.sub(r'ебал|Ебал', 'совершал половой акт', answer3)
        answer5 = re.sub(r'ебаный|Ебаный', 'плохой', answer4)
        answer6 = re.sub(r'ебаная|Ебаная', 'плохая', answer5)
        answer7 = re.sub(r'хуета|Хуета', 'херня', answer6)
        answer8 = re.sub(r'долбоёб|Долбоёб', 'дурак', answer7)
        answer9 = re.sub(r'ебать|Ебать', 'совершать половой акт', answer8)
        answer10 = re.sub(r'ебола|Ебола', 'херня', answer9)
        answer11 = re.sub(r'ебало|Ебало', 'лицо', answer10)
        answer12 = re.sub(r'пидорас|Пидорас', 'дырявый', answer11)
        answer13 = re.sub(r'пидор|Пидор', 'голубой', answer12)
        answer14 = re.sub(r'хуесос|Хуесос', 'любитель шлангов', answer13)
        answer15 = re.sub(r'пиздос|Пиздос', 'очень плохо', answer14)
        answer16 = re.sub(r'хуйня|Хуйня', 'ерунда', answer15)
        answer17 = re.sub(r'нихуя|Нихуя', 'ничего', answer16)
        answer18 = re.sub(r'ебалу|Ебалу', 'лицу', answer17)
        answer19 = re.sub(r'бля\b|Бля\b', 'блин', answer18)
        answer20 = re.sub(r'уебать|Уебать', 'сделать больно', answer19)
        answer21 = re.sub(r'пизду|Пизду', 'влагалище', answer20)
        answer22 = re.sub(r'блять|Блять', 'блин', answer21)
        answer23 = re.sub(r'хуе|Хуе|хуи|Хуи|Хую|хую|хуе', 'а', answer22)
        answer24 = re.sub(r'блядина|Блядина', 'легкомысленная девушка', answer23)
        answer = re.sub(r'уёбок|Уёбок', 'задница', answer24)
        bot.send_message(cid, answer)


bot.polling()