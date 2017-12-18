#!/usr/bin/env python
"""
Python script to handle telegram.
Giving command to arduino via serial
and replying cute response to me.
I call her, this bot I mean, Reni
"""

import serial
import telepot
import time

TOKEN = 'xxxxxxx' # my bot token goes here
bot = telepot.Bot(TOKEN)
arduino = serial.Serial('/dev/ttyUSB1', 9600)

def handle(msg):
    nyala = ['n', 'nyala', 'hidup', 'idup','urip','1', 'on']
    mati = ['m', 'mati', 'modar', '0', 'off']
    chat_id = msg['chat']['id']
    message = msg['text']
    arduino.flushInput()
    arduino.flushOutput()
    # bot.sendMessage(chat_id, "test")
    if message.lower() in nyala:
        arduino.write('n')
        time.sleep(.1)
        respon = arduino.readline()
        if respon.strip() == 'success on':
            bot.sendMessage(chat_id, "Oke... Kipas aku nyalain")
        elif respon.strip() == 'already on':
            bot.sendMessage(chat_id, "Kipas udah nyala, tolol!")
    elif message.lower() in mati:
        arduino.write('m')
        time.sleep(.1)
        respon = arduino.readline()
        if respon.strip() == 'success off':
            bot.sendMessage(chat_id, "udah noh, kipas udah aku matiin. Puas?")
        elif respon.strip() == 'already off':
            bot.sendMessage(chat_id, "Lah, kipasnya kan udah mati, goblok")
    else:
        bot.sendMessage(chat_id, "Gila lu ya?")

bot.message_loop(handle)

while True:
    time.sleep(5)
