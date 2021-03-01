import db

dict_product_1 = {'id': 0, 'title': 'Macbook13', 'cart_id': 0}
dict_product_2 = {'id': 1, 'title': 'Iphone12', 'cart_id': 1}
dict_product_21 = {'id': 2, 'title': 'Iphone12', 'cart_id': 1}
dict_product_22 = {'id': 3, 'title': 'Iphone12', 'cart_id': 1}
dict_product_3 = {'id': 4, 'title': 'Macbook13', 'cart_id': 2}
dict_product_31 = {'id': 5, 'title': 'Macbook13', 'cart_id': 2}
dict_product_4 = {'id': 6, 'title': 'Ipad4', 'cart_id': 3}
dict_product_5 = {'id': 7, 'title': 'Iphone10', 'cart_id': 4}
dict_product_6 = {'id': 8, 'title': 'Iphone10', 'cart_id': 5}
dict_product_61 = {'id': 9, 'title': 'Iphone10', 'cart_id': 5}
dict_product_62 = {'id': 10, 'title': 'Iphone10', 'cart_id': 5}

db.insert('product', dict_product_1)
db.insert('product', dict_product_2)
db.insert('product', dict_product_21)
db.insert('product', dict_product_22)
db.insert('product', dict_product_3)
db.insert('product', dict_product_31)
db.insert('product', dict_product_4)
db.insert('product', dict_product_5)
db.insert('product', dict_product_6)
db.insert('product', dict_product_61)
db.insert('product', dict_product_62)

dict_cart_1 = {'id': 0, 'total_products': 2, 'final_price': 10000, 'in_order': 1, 'for_anonymous_user': 0,
               'owner_id': 0}
dict_cart_2 = {'id': 1, 'total_products': 3, 'final_price': 90000, 'in_order': 1, 'for_anonymous_user': 0,
               'owner_id': 1}
dict_cart_3 = {'id': 2, 'total_products': 2, 'final_price': 1000, 'in_order': 1, 'for_anonymous_user': 0,
               'owner_id': 2}
dict_cart_4 = {'id': 3, 'total_products': 3, 'final_price': 5000, 'in_order': 1, 'for_anonymous_user': 0,
               'owner_id': 3}
dict_cart_5 = {'id': 4, 'total_products': 2, 'final_price': 12000, 'in_order': 1, 'for_anonymous_user': 0,
               'owner_id': 4}
dict_cart_6 = {'id': 5, 'total_products': 3, 'final_price': 15000, 'in_order': 1, 'for_anonymous_user': 0,
               'owner_id': 5}

db.insert('shop_cart', dict_cart_1)
db.insert('shop_cart', dict_cart_2)
db.insert('shop_cart', dict_cart_3)
db.insert('shop_cart', dict_cart_4)
db.insert('shop_cart', dict_cart_5)
db.insert('shop_cart', dict_cart_6)

dict_order_1 = {'id': 0, 'first_name': 'Alex', 'last_name': 'Borodnikov', 'phone': '12312512', 'status': 'new_order',
                'buying_type': 'self', 'comment': 'faster', 'created_at': '1.01.2021', 'order_date': '22.02.2021',
                'address': 'Pushkina 10', 'cart_id': 0, 'customer_id': 0}

dict_order_2 = {'id': 1, 'first_name': 'Kapablanka', 'last_name': 'Alexeyeev', 'phone': '12321512',
                'status': 'new_order',
                'buying_type': 'self', 'comment': 'faster', 'created_at': '11.01.2021', 'order_date': '25.02.2021',
                'address': 'Lenina 120', 'cart_id': 1, 'customer_id': 1}

dict_order_3 = {'id': 2, 'first_name': 'Sergey', 'last_name': 'Jose', 'phone': '123512512', 'status': 'new_order',
                'buying_type': 'self', 'comment': 'faster', 'created_at': '21.01.2021', 'order_date': '27.02.2021',
                'address': 'Karavan 11', 'cart_id': 2, 'customer_id': 2}

dict_order_4 = {'id': 3, 'first_name': 'Anatoly', 'last_name': 'Macregor', 'phone': '1212512', 'status': 'new_order',
                'buying_type': 'self', 'comment': 'faster', 'created_at': '25.01.2021', 'order_date': '26.02.2021',
                'address': 'Karakin 21', 'cart_id': 3, 'customer_id': 4}

dict_order_5 = {'id': 4, 'first_name': 'Misha', 'last_name': 'Tall', 'phone': '32312512', 'status': 'new_order',
                'buying_type': 'self', 'comment': 'faster', 'created_at': '27.01.2021', 'order_date': '28.02.2021',
                'address': 'new arbat 125', 'cart_id': 4, 'customer_id': 4}

dict_order_6 = {'id': 5, 'first_name': 'Sasha', 'last_name': 'Nurmagomedov', 'phone': '12315555', 'status': 'new_order',
                'buying_type': 'self', 'comment': 'faster', 'created_at': '12.01.2021', 'order_date': '14.02.2021',
                'address': 'magnus 1', 'cart_id': 5, 'customer_id': 5}

db.insert('shop_order', dict_order_1)
db.insert('shop_order', dict_order_2)
db.insert('shop_order', dict_order_3)
db.insert('shop_order', dict_order_4)
db.insert('shop_order', dict_order_5)
db.insert('shop_order', dict_order_6)
