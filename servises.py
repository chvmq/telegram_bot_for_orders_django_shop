import os
import telebot
from db import *

USER = os.getenv('CORRECT_USER')
TOKEN = os.getenv('TOKEN')
print(type(USER), TOKEN)
bot = telebot.TeleBot(TOKEN)


def check_user_id_and_send_response(message_chat_id: int, response: str) -> None:
    if message_chat_id == int(USER):
        bot.send_message(message_chat_id, response)
    else:
        bot.send_message(message_chat_id, 'Доступ закрыт')


def get_latest_orders_handler(message_chat_id: int) -> None:
    list_of_orders = get_latest_orders()
    response = ''
    for order in list_of_orders:
        parsed_order = ' '.join((str(i) for i in order))
        response += f'\nЗаказ:\n{parsed_order}'
    check_user_id_and_send_response(message_chat_id, response)


def get_order_detail_handler(message_chat_id: int, customer_id: int) -> None:
    response = get_order_detail(customer_id)
    check_user_id_and_send_response(message_chat_id, str(response))

