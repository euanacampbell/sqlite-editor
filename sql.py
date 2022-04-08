import sqlite3
from sqlite3 import Error
from tabulate import tabulate
import json
import os

from assets.datasets.questions import TRADING_QUESTIONS, INVESTMENT_QUESTIONS


class SQL:

    def __init__(self, table_setup='trading'):
        self.table_setup = table_setup

        self.refresh_tables()

    def create_connection(self):
        """ create a database connection to a SQLite database """
        try:
            cwd = os.getcwd()
            conn = sqlite3.connect(f"{cwd}/assets/{self.table_setup}.db")
            # print(sqlite3.version)
        except sqlite3.Error as e:
            print(e)

        return(conn)

    def refresh_tables(self):

        sql_script = self.get_table_script()

        conn = self.create_connection()
        cursor = conn.cursor()
        cursor.executescript(sql_script)
        conn.commit()
        conn.close()

    def run_query(self, query: str, sql_print=False):
        conn = self.create_connection()

        try:
            c = conn.cursor()
            c.execute(query)
            conn.commit()
        except sqlite3.Error as e:
            response = {
                'error': True,
                'result': str(e)
            }
            return(response)

        master = []
        try:
            columns = [d[0] for d in c.description]
            master.append(columns)
        except:
            pass

        results = c.fetchall()

        for row in results:
            new_row = []
            for value in row:
                new_row.append(value)

            master.append(new_row)

        if sql_print:
            self.print_results(results, columns)

        conn.close()

        response = {
            'error': False,
            'result': master
        }

        return(response)

    def print_results(self, results, columns):

        print(tabulate(results, headers=columns, tablefmt="pretty"))

    def get_questions(self):

        if self.table_setup == 'investments':
            return INVESTMENT_QUESTIONS
        elif self.table_setup == 'trading':
            return TRADING_QUESTIONS
        else:
            return {}

    def get_table_info(self):

        tables = self.run_query(
            "SELECT name FROM sqlite_master WHERE type='table';")['result']

        tables.remove(['name'])
        table_info = {}

        for table in tables:

            table = table[0]

            table_info[table] = self.run_query(
                f'SELECT * FROM {table}')['result']

        return table_info

    def get_table_script(self):

        cwd = os.getcwd()
        script = f"{cwd}/assets/datasets/{self.table_setup}.sql"

        with open(script, 'r') as sql_file:
            sql_script = sql_file.read()

        return sql_script
