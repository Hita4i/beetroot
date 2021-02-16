"""
1) Табельный номер ввод (добавить работника на номеру из дикта).
2) Выбор смены и времени работы или произвольние время работы.
    Указать дату или выбрать авто.
3) Ввод даты + автоматическое заполнение даты создания записи.
4) Выбор оборудования.
5) Выбор препарата.
6) Выбор времени простоя.
7) Причина простоя.
8) Указать специалиста ремонтной службы.
"""
import TelegramBot.config as conf
import json
import telebot
from telebot import types
import datetime
import os

TOKEN = conf.BOT_TOKEN
bot = telebot.TeleBot(TOKEN)
base = {
    'Дата': '',
    'Табельный номер': '',
    'Смена': '',
    'Время работы': '',
}

DATE = datetime.datetime.today().strftime("%d.%m.%Y")
TIME = datetime.datetime.today().strftime("%H:%M:%S")

def work_date_keyb():
    keyb = types.InlineKeyboardMarkup(row_width=1)
    bt_dt1 = types.InlineKeyboardButton('Текущая дата', callback_data='bt_dt1')
    bt_dt2 = types.InlineKeyboardButton('Ввести произвольную дату', callback_data='bt_dt2')
    keyb.add(bt_dt1, bt_dt2)
    return keyb
def work_time_keyb():
    keyb = types.InlineKeyboardMarkup(row_width=1)
    bt1 = types.InlineKeyboardButton('Смена 1 07:00-15:30', callback_data='bt1')
    bt2 = types.InlineKeyboardButton('Смена 2 14:00-22:30', callback_data='bt2')
    bt3 = types.InlineKeyboardButton('Смена 3 22:30-06:00', callback_data='bt3')
    bt4 = types.InlineKeyboardButton('Ввести произвольное время', callback_data='bt4')
    keyb.add(bt1, bt2, bt3, bt4)
    return keyb


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f"Здравствуйте {message.chat.first_name} {message.chat.last_name}!\n"
                          f"Введите табальный номер для начала работы")


@bot.message_handler(func=lambda message: True)
def person_num(message):
    if message.text:
        base['Табельный номер'] = message.text
        print(base)
        bot.send_message(message.from_user.id, 'Выберите время работы или введите произвольное в формате ЧЧ:ММ',
                         reply_markup=work_time_keyb())
def add_self_time(message):     # Добавить проверку
    base['Смена'] = 'random'
    base['Время работы'] = str(message.text)
    get_base()
    datamsg = bot.send_message(message.from_user.id, 'Укажитедату в формате Ч.Д.Г или...',
                               reply_markup=work_date_keyb())
    bot.register_next_step_handler(datamsg, add_date)

@bot.callback_query_handler(func=lambda message: True)
def answer(message):

    if message.data == 'bt1':
        base['Смена'] = '1'
        base['Время работы'] = '07:00-15:30'
        get_base()
    elif message.data == 'bt2':
        base['Смена'] = '2'
        base['Время работы'] = '14:00-22:30'
        get_base()
    elif message.data == 'bt3':
        base['Смена'] = '3'
        base['Время работы'] = '22:30-06:00'
        get_base()
    elif message.data == 'bt4':
        msg = bot.send_message(message.from_user.id, text='Ведите произвольное время')
        bot.register_next_step_handler(msg, add_self_time)

def add_date(message):
    if message.data == 'bt_dt1':
        base['Дата'] = f'{DATE} - {TIME}'
        print(f'{DATE} - {TIME}')
    elif message.data == 'bt_dt2':
        base['Дата'] = message.data
        get_base()

# def add_self_time(message):
#     base['Смена'] = 'random'
#     base['Время работы'] = str(message.text)
#     get_base()
#     datamsg = bot.send_message(message.from_user.id, 'Укажитедату в формате Ч.Д.Г или...',
#                                reply_markup=work_date_keyb())
#     bot.register_next_step_handler(datamsg, add_date)

# @bot.callback_query_handler(func=lambda message: True)
# def add_date(message):
#     if message.data == 'bt_dt1':
#         base['Дата'] = f'{DATE} - {TIME}'
#         print(f'{DATE} - {TIME}')
#     elif message.data == 'bt_dt2':
#         base['Дата'] = message.data
#         get_base()


def get_base():
    print(base)


if __name__ == '__main__':

    bot.polling()

