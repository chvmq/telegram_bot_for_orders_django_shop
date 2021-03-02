import os
import telebot
from db import *

USER = os.getenv('CORRECT_USER')
TOKEN = os.getenv('TOKEN')
print(type(USER), TOKEN)
bot = telebot.TeleBot(TOKEN)


def check_user_id_and_send_response(message_chat_id: int, response: str) -> None:
    """Проверяет пользовател на сотрудника организации"""
    if message_chat_id == int(USER):
        bot.send_message(message_chat_id, response)
    else:
        bot.send_message(message_chat_id, 'Доступ закрыт')


def get_latest_orders_handler(message_chat_id: int) -> None:
    """Получает последние заказы в виде списка и парсит ответ"""
    list_of_orders = get_latest_orders()
    response = ''
    for order in list_of_orders:
        parsed_order = ' '.join((str(i) for i in order))
        response += f'\nЗаказ:\n{parsed_order}'
    check_user_id_and_send_response(message_chat_id, response)


def get_order_detail_handler(message_chat_id: int, customer_id: int) -> None:
    """Получает детальный заказ по идентификатору и парсит ответ"""
    non_parsed_response = get_order_detail(customer_id)
    response: str
    first_name = non_parsed_response[0][0]
    last_name = non_parsed_response[0][1]
    product = non_parsed_response[0][2]
    number_of_products = non_parsed_response[0][3]
    total_price = non_parsed_response[0][4]

    response = f'Заказ пользователя {first_name} {last_name} на сумму {total_price}\n {product} {number_of_products} шт.'

    check_user_id_and_send_response(message_chat_id, str(response))

