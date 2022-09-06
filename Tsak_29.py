# Реализовать функцию, которая выведет FirstName из таблицы customers и кол-во их вхождений в таблицу.
# Если решаем через sql, то используем count и секцию group by.
# Результат выполнения функции: "Alex 2", т.е. имя и кол-во его вхождений.
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


def get_count_firstnames() -> None:
    """
    Функция для вывода количества вхождений FirstName в таблицу
    """
    query_sql = f"""
         SELECT FirstName, COUNT(*) AS FirstNamesCount
           FROM customers
           GROUP by FirstName 
    """
    result = execute_query(connection, query_sql)
    unwrapp_query_result(result)


get_count_firstnames()
