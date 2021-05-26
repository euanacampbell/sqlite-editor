import sqlite3
from sqlite3 import Error
from tabulate import tabulate
import json

class SQL:

    def __init__(self):
        pass

    def create_connection(self):
        """ create a database connection to a SQLite database """
        try:
            conn = sqlite3.connect("/Users/euancampbell/Google Drive/Projects/sqlite-editor/assets/main.db")
            # print(sqlite3.version)
        except sqlite3.Error as e:
            print(e)

        return(conn)

    def run_query(self, query:str, sql_print=False):
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
        
        master=[]
        try:
            columns = [d[0] for d in c.description]
            master.append(columns)
        except:
            pass

        results = c.fetchall()

        for row in results:
            new_row=[]
            for value in row:
                new_row.append(value)
            
            master.append(new_row)

        if sql_print:
            self.print_results(results, columns)
        
        conn.close()

        # results = json.dumps(results)
        # print('dumps')
        # print(results)

        response = {
            'error': False,
            'result': master
        }

        return( response )

    def build_tables(self):
        
        
        query = """CREATE TABLE [Trade](
                    [TradeId] varchar(3) NOT NULL,
                    [CustCode] [nvarchar](50) NOT NULL,
                    [Qty] [int] NULL)"""
        self.run_query(query)

        query = """CREATE TABLE [Customer](
                [CustCode] [nvarchar](50) NOT NULL,
                [CustName] [nvarchar] (50) NOT NULL)"""
        self.run_query(query)

        query = "insert into Trade values ('001', 'A',3), ('002', 'C',5), ('003', 'C',20), ('004', 'D',7), ('005', 'B',4), ('006', 'A',10), ('007', 'B',5), ('008', 'E',15)"
        self.run_query(query)

        query = "insert into Customer values ('A','CustA'), ('B','CustB'), ('D','CustD'), ('E','CustE')"
        self.run_query(query)

    def refresh_tables(self):

        print('RE-BUILDING TABLES')
        query = "DROP TABLE Trade"
        self.run_query(query)
        query = "DROP TABLE Customer"
        self.run_query(query)

        self.build_tables()
    
    def print_results(self, results, columns):
        
        print(tabulate(results, headers=columns, tablefmt="pretty"))

if __name__=="__main__":
    sql = SQL()

    sql.build_tables()
    results = sql.run_query('SELECT * FROM Trade', sql_print=True)

    results = sql.run_query('SELECT * FROM Customer', sql_print=True)

    results = sql.run_query("SELECT * FROM Trade t LEFT JOIN Customer c ON c.custcode=t.custcode", sql_print=True)

    results = sql.run_query("SELECT c.custcode, c.custname, SUM(t.qty) FROM Customer c LEFT JOIN Trade t ON t.custcode=c.custcode GROUP BY c.custcode, c.custname", sql_print=True)