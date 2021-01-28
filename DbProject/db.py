import json
import pyodbc

DBQ = input('Введите путь к файлу: ')
class Connect:
    def __init__(self):
        self.conn_str = (
            r'DRIVER={Microsoft Access Driver (*.mdb)};'
            rf'DBQ={DBQ};'
        )
        self.conn = pyodbc.connect(self.conn_str)
        self.cursor = self.conn.cursor()
        self.table_name_ = 'tab'
        self.query = f'SELECT * FROM {self.table_name_}'







