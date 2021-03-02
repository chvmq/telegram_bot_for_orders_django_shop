import sqlite3 as sql
from typing import Dict, List, Tuple


def get_connect() -> Tuple:
    """Соеденение с базой данных"""
    conn = sql.connect('database.db')
    cursor = conn.cursor()
    return conn, cursor


def create_db() -> None:
    """Создаёт БД"""
    conn, cursor = get_connect()
    with open('create_db.sql', 'r') as f:
        query = f.read()
        try:
            cursor.executescript(query)
            conn.commit()
        except sql.OperationalError as ex:
            print('Что то пошло не так', ex)


def get_tables() -> List:
    """Получает название таблиц из базы данных"""
    conn, cursor = get_connect()
    cursor.execute("select name from sqlite_master where type='table';")
    return cursor.fetchall()


def insert(table: str, column_values: Dict):
    """Добавляет поля в таблицу"""
    conn, cursor = get_connect()
    columns = ', '.join(column_values.keys())
    values = [tuple(column_values.values())]
    placeholders = ", ".join("?" * len(column_values.keys()))
    cursor.executemany(
        f"INSERT INTO {table} "
        f"({columns}) "
        f"VALUES ({placeholders})",
        values)
    conn.commit()


def delete(table: str, row_id: int) -> None:
    """Удаляет поля из таблицы по идентификатору"""
    row_id = int(row_id)
    cursor = get_connect()[1]
    cursor.execute(f'delete from {table} where id={row_id}')


def check_db_exists():
    """Проверяет наличие базы данных"""
    conn, cursor = get_connect()
    query = get_tables()
    if not query:
        create_db()


def get_latest_orders() -> List:
    """Получает последние заказы из бд, сортированые по дате заказа"""
    conn, cursor = get_connect()
    query = f"""
    SELECT o.id, first_name, last_name, c.final_price
    FROM shop_order o JOIN shop_cart c ON o.id = c.id
    ORDER BY o.created_at LIMIT 5;
    """
    cursor.execute(query)
    return cursor.fetchall()


def get_order_detail(customer_id: int) -> List:
    """Получает данные одного заказа"""
    conn, cursor = get_connect()
    query = f"""
    SELECT o.first_name, o.last_name, p.title, c.total_products, c.final_price
    FROM shop_order o JOIN product p ON p.cart_id = o.id JOIN shop_cart c ON o.cart_id = c.id
    WHERE o.id = {str(customer_id)}; 
    """
    cursor.execute(query)
    return cursor.fetchall()


check_db_exists()
