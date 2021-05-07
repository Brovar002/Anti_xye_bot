# -*- coding: utf-8 -*-

import telebot
import re
import random
import constants
import synonym

reg = r"хуе|Хуе|хуи|Хуи|Хую|хую|хуе|хуй|Хуй|пизда|Пизда|Пиздец|пиздец|ебал|Ебал|ебаный|Ебаный|ебаная|Ебаная|хуета|Хуета|долбоёб|Долбоёб|ебать|Ебать|ебола|Ебола|ебало|Ебало|пидор|Пидор|хуесос|Хуесос|пиздос|Пиздос|хуйня|Хуйня|нихуя|Нихуя|ебалу|Ебалу|Бля|бля|уебать|Уебвть|пизду|Пизду|уёбок|Уёбок|блядина|Блядина"



bot = telebot.TeleBot(constants.token)

# upd = bot.get_updates()
# print(upd)

# last_upd = upd[-1]
# message_from_user = last_upd.message
# print(message_from_user)

print(bot.get_me())


@bot.message_handler(content_types=['text'])
def handle_text(message):
    cid = message.chat.id
    s = ''
    if re.findall(reg, message.text):
        for e in re.findall(reg, message.text):
            message.text = re.sub(r'хуй\b|Хуй\b', random.choice(synonym.xyi), message.text, 1)
            message.text = re.sub(r'пизда|Пизда|манда\b|Манда\b|пиздятина|Пиздятина', random.choice(synonym.pizda), message.text, 1)
            message.text = re.sub(r'пиздец|Пиздец|пиздос|Пиздос', random.choice(synonym.pizdec), message.text, 1)
            message.text = re.sub(r'ебал\b|Еба\bл', random.choice(synonym.ebal), message.text, 1)
            message.text = re.sub(r'ебаный|Ебаный', random.choice(synonym.ebaniy), message.text, 1)
            message.text = re.sub(r'ебаная|Ебаная', random.choice(synonym.ebanaya), message.text, 1)
            message.text = re.sub(r'хуета|Хуета|хуйня|Хуйня|хуетень|Хуетень|Хуитень|хуитень|ебола|Ебола|ебала|Ебала|поебота|Поебота|поебола|Поебола', random.choice(synonym.hueta), message.text, 1)
            message.text = re.sub(r'хуету|Хуету|хуйню|Хуйню|еболу|Еболу|поеботу|Поеботу', random.choice(synonym.huetu), message.text, 1)
            message.text = re.sub(r'долбоёб|Долбоёб|долбоёбина|Долбоёбина|Долбоеб|долбоеб|долбоебина|Долбоебина', random.choice(synonym.dolboeb), message.text, 1)
            message.text = re.sub(r'ебать\b|Ебать\b', random.choice(synonym.ebat), message.text, 1)
            message.text = re.sub(r'ебала|Ебала', random.choice(synonym.ebala), message.text, 1)
            message.text = re.sub(r'ебало|Ебало|ебальник|Ебаньник|ебальничек|Ебальничек', random.choice(synonym.ebalo), message.text, 1)
            message.text = re.sub(r'пидорас|Пидорас|пидор\b|Пидор\b|пидорасина|Пидораисна', random.choice(synonym.pidor), message.text, 1)
            message.text = re.sub(r'уебал|Уебал|въебал|Въебал|вьебал|Вьебал|ебанул\b|Ебанул\b', random.choice(synonym.uebal), message.text, 1)
            message.text = re.sub(r'хуесос\b|Хуесос\b|хуесосина|Хуесосина', random.choice(synonym.huesos), message.text, 1)
            message.text = re.sub(r'уебу|Уебу|въебу|Въебу|вьебу|Вьебу', random.choice(synonym.uebu), message.text, 1)
            message.text = re.sub(r'уебала|Уебала|въебала|Въебала|вьебала|Вьебала|ебанула\b|Ебанула\b', random.choice(synonym.uebala), message.text, 1)
            message.text = re.sub(r'нихуя\b|Нихуя\b|нихуяшеньки|Нихуяшеньки', random.choice(synonym.nihuya), message.text, 1)
            message.text = re.sub(r'ебалу|Ебалу|ебальничку|Ебальничку', random.choice(synonym.ebalu), message.text)
            message.text = re.sub(r'бля\b|Бля\b|блять|Блять', random.choice(synonym.blya), message.text, 1)
            message.text = re.sub(r'уебать|Уебать|въебать|Въебать|вьебать|Вьебать|ебануть\b|Ебануть\b', random.choice(synonym.uebat), message.text, 1)
            message.text = re.sub(r'пизду|Пизду|пиздятину|Пиздятину|манду|Манду', random.choice(synonym.pizdu), message.text, 1)
            message.text = re.sub(r'охуеть|Охуеть|Ахуеть|ахуеть', random.choice(synonym.ohuet), message.text, 1)
            message.text = re.sub(r'охуел|Охуел|Ахуел|ахуел', random.choice(synonym.ohuet), message.text, 1)
            message.text = re.sub(r'охуела|Охуела|Ахуела|ахуела', random.choice(synonym.ohuela), message.text, 1)
            message.text = re.sub(r'хуе|Хуе|хуи|Хуи|Хую|хую|хуе', 'Члено', message.text)
            message.text = re.sub(r'блядина|Блядина|блядь|Блядь|блядушка|Блядушка|блядунья|Блядунья', random.choice(synonym.blyad), message.text, 1)
            message.text = re.sub(r'уёбок|Уёбок|уёбище|Уёбище|уебан|Уебан|уебок|Уебок', random.choice(synonym.uebok), message.text, 1)
            message.text = re.sub(r'нихуя себе|Нихуя себе|нихуя сибе|Нихуя сибе', random.choice(synonym.nihuyaSebe), message.text, 1)
            message.text = re.sub(r'ебануться|Ебануться|ебанутся|Ебанутся|ёбнуться|Ёбнуться|ёбнутся|Ёбнутся', random.choice(synonym.ebanutsya), message.text, 1)
            message.text = re.sub(r'ебанулся|Ебанулся|ёбнулся|Ёбнулся', random.choice(synonym.ebnulsya), message.text, 1)
            message.text = re.sub(r'ебанулась|Ебанулась|ёбнулась|Ёбнулась', random.choice(synonym.ebnulas), message.text, 1)
            s += e[1]
        bot.send_message(cid, message.text)


bot.polling()
