import sqlite3
from common import get_path_resourses, dict_unpack


SQL_SELECT_INCOMES_ALL = '''
    SELECT
        id, date, amount, owner, source
    FROM
        incomes
'''

SQL_SELECT_COSTS_ALL = '''
    SELECT
        id, date, amount, owner, source
    FROM
        costs
'''

SQL_INSERT_INCOME = '''
    INSERT INTO incomes (date, amount, owner, source) VALUES (?, ?, ?, ?)
'''

SQL_INSERT_COST = '''
    INSERT INTO costs (date, amount, owner, source) VALUES (?, ?, ?, ?)
'''


def connect(db_name=None):
    """Установить соединение с БД"""
    if not db_name:
        db_name = ':memory:'

    conn = sqlite3.connect(db_name)

    return conn


def initialize(conn, creation_script=None):
    """Инициализировать структуру БД"""
    if not creation_script:
        creation_script = get_path_resourses('schema.sql')

    with conn, open(creation_script) as db_script:
        conn.executescript(db_script.read())


def get_all_incomes(conn, domain=''):
    """Получить все доходы"""
    with conn:
        conn.row_factory = dict_factory
        cursor = conn.execute(SQL_SELECT_INCOMES_ALL)
        return cursor.fetchall()


def get_all_costs(conn, domain=''):
    """Получить все расходы"""
    with conn:
        conn.row_factory = dict_factory
        cursor = conn.execute(SQL_SELECT_COSTS_ALL)
        return cursor.fetchall()


def add_income(conn, income_pack, domain=''):
    """Добавить доход в БД"""
    conn.execute(SQL_INSERT_INCOME, dict_unpack(income_pack))


def add_costs(conn, cost_pack, domain=''):
    """Добавить доход в БД"""
    conn.execute(SQL_INSERT_COST, dict_unpack(cost_pack))


def dict_factory(cursor, row):
    """Изменить row_factory"""
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


if __name__ == '__main__':
    get_connection = lambda: connect('transactions.sqlite3')

    f_pack = {'date': '11.06.18',
              'amount': 13666,
              'owner': 'Маша',
              'source': 'ЗП'
              }

    s_pack = {'date': '11.06.18',
              'amount': 5000,
              'owner': 'Маша',
              'source': 'Ткани'
              }

    with get_connection() as conn:
        initialize(conn)
        add_income(conn, f_pack)
        add_costs(conn, s_pack)
        all_inc = get_all_incomes(conn)
        all_cos = get_all_costs(conn)
        print(all_inc)
        print('------------------------')
        print(all_cos)
