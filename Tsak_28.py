# Реализовать функцию, которая выведет прибыль по таблице invoice_items.
# Сумма по заказу = UnitPrice * Quantity. Если решаем через sql, то нужно использовать sum.
# Результат выполнение функции - одно число, которое является суммой всех заказов.
import sqlite3
import os

from typing import List

db_pass = os.path.join(os.getcwd(), "chinook.db")
connection = sqlite3.connect(db_pass)

print(db_pass)


def execute_query(connection, querly_sql: str) -> List:
    """
    Функция для выполнения запроса
    :param соежинение с бд, sql запрос
    :return: результат выполнения запроса
    """
    cur = connection.cursor()
    result = cur.execute(querly_sql)
    return result

def unwrapp_query_result(records: List) -> None:
    """
    Функция для красивого вывода результата в консоль
    :param список строк
    """
    for record in records:
        print(*record)

def get_invoice_items() -> None:
    """

    :return:
    """
    query_sql = f"""
         SELECT sum(UnitPrice * Quantity)
           FROM invoice_items;    
    """
    result = execute_query(connection, query_sql)
    unwrapp_query_result(result)


get_invoice_items()