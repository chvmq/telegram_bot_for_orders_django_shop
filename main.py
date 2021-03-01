from servises import *
from servises import bot


@bot.message_handler(commands=['start'])
def send_welcome_view(message) -> None:
    print(type(message.chat.id))
    check_user_id_and_send_response(message.chat.id, 'welcome')


@bot.message_handler(content_types=['document', 'audio', 'video', 'sticker', 'photo', 'animation', 'voice'])
def wrong_type_of_message_view(message):
    check_user_id_and_send_response(message.chat.id, 'Только текст и команды')


@bot.message_handler(commands='Последние')
def get_latest_orders_view(message) -> None:
    get_latest_orders_handler(message.chat.id)


@bot.message_handler(commands='Заказ')
def get_order_detail_view(message) -> None:
    customer_id = 1
    get_order_detail_handler(message.chat.id, customer_id)


bot.polling()
