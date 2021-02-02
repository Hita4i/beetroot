import json
import pyodbc
from typing import List

class Connect:
    def __init__(self, db_file_path='import.mdb'):
        self.table_name_ = 'tab'
        self.db_file_path = db_file_path
        self.conn_str = (
            r'DRIVER={Microsoft Access Driver (*.mdb)};'
            rf'DBQ={db_file_path};'
        )
        self.conn = pyodbc.connect(self.conn_str)
        self.cursor = self.conn.cursor()
        self.query = f'SELECT * FROM {self.table_name_}'

    def close_connect(self):
        self.cursor.close()
        self.conn.close()

    def get_all_colunms(self):
        """
        добавить название всех колонок
        в таблице в масив и словарь
        может пригодится...
        """
        self.my_list = []
        self.my_dict = {}
        for row in self.cursor.columns():
            self.my_list.append(row.column_name)
        for k in self.my_list:
            self.my_dict[f'{k}'] = ''
        with open('columns.json', 'w') as columns:
            json.dump(self.my_list, columns)


class Download(Connect):
    def __init__(self, db_file_path):
        super().__init__(db_file_path)

    def download_to_list(self):

        data = []
        for i in self.cursor.execute(self.query):
            Тип_ВМД = i[0]
            Відправник = i[1]
            Відправник_2 = i[2]
            ОКПЕО_Одержувач = i[3]
            Одержувач = i[4]
            Адресa_Одержувача = i[5]
            ОКПЕО_Декларанта = i[6]
            Декларант = i[7]
            Адресa_Декларанта = i[8]
            МИТНИЙ_ОРГАН = i[9]
            номер_ВМД = i[10]
            Дата_випуску = i[11]
            Товар_номер = i[12]
            Код_товару = i[13]
            Опис_товару = i[14]
            Торгівельна_марка = i[15]
            Країна_відправлення = i[16]
            Торгівельна_країна = i[17]
            Код_країни_походженн = i[18]
            Вага_брутто_кг = i[19]
            Вага_нетто_кг = i[20]
            Упаковка = i[21]
            Додаткова_одиниця_виміру = i[22]
            Кількість_в_одиницяx_виміру = i[23]
            шт = i[24]
            Фактурна_вартість = i[25]
            Митна_вартість = i[26]
            кг = i[27]
            Курс = i[28]
            Код_МВВ = i[29]
            СТ_55 = i[30]
            Ставка_мита = i[31]
            контракт = i[32]
            ТЗ_на_кордоні = i[33]
            номер_контейнеру = i[34]
            Процедура = i[35]
            Митний_орган = i[36]
            Умови_поставки = i[37]

            test_dict = {
                'Тип ВМД': Тип_ВМД,
                'Відправник': Відправник,
                'Відправник 2': Відправник_2,
                'ОКПЕО Одержувач': ОКПЕО_Одержувач,
                'Одержувач': Одержувач,
                'Адресa Одержувача': Адресa_Одержувача,
                'ОКПЕО Декларанта': ОКПЕО_Декларанта,
                'Декларант': Декларант,
                'Адресa Декларанта': Адресa_Декларанта,
                'МИТНИЙ ОРГАН': МИТНИЙ_ОРГАН,
                '№ ВМД': номер_ВМД,
                'Дата випуску': Дата_випуску,
                'Товар №': Товар_номер,
                'Код товару': Код_товару,
                'Опис товару': Опис_товару,
                'Торгівельна марка': Торгівельна_марка,
                'Країна відправлення': Країна_відправлення,
                'Торгівельна країна': Торгівельна_країна,
                'Код країни походження': Код_країни_походженн,
                'Вага брутто (кг)': Вага_брутто_кг,
                'Вага нетто (кг)': Вага_нетто_кг,
                'Упаковка %': Упаковка,
                'Додаткова одиниця виміру': Додаткова_одиниця_виміру,
                'Кількість в одиницяx виміру': Кількість_в_одиницяx_виміру,
                '$/1шт': шт,
                'Фактурна вартість($)': Фактурна_вартість,
                'Митна вартість($)': Митна_вартість,
                '$/1кг': кг,
                'Курс $': Курс,
                'Код МВВ': Код_МВВ,
                'СТ 55': СТ_55,
                'Ставка мита %': Ставка_мита,
                'контракт': контракт,
                'ТЗ на кордоні': ТЗ_на_кордоні,
                '№ контейнеру': номер_контейнеру,
                'Процедура': Процедура,
                'Митний орган в"їзду': Митний_орган,
                'Умови поставки': Умови_поставки
            }
            data.append(test_dict)
            d.save_to_json(data)
    def save_to_json(self, data: List, file_name='file.json'):

        with open(file_name, 'w') as file:
            json.dump(data, file)
            print('Job well done!')
            c.close_connect()



c = Connect('import.mdb')
d = Download('import.mdb')
# d.download_to_list()
# d.save_to_json()
c.get_all_colunms()
