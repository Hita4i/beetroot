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

    def close_connect(self):
        self.cursor.close()
        self.conn.close()

    def get_oll_colunms(self):
        """
        добавить название всех колонок
        в таблице в масив и словарь
        может пригодится...
        """
        self.my_list = []
        self.my_dict = {}
        for row in self.cursor.columns(table=self.table_name_):
            self.my_list.append(row.column_name)
        for k in self.my_list:
            self.my_dict[f'{k}'] = ''
        with open('columns.json', 'w') as columns:
            json.dump(self.my_list, columns)


class Download(Connect):
    def __init__(self):
        super().__init__()

    def download_to_list(self):

        self.full_list = []
        for i in self.cursor.execute(self.query):
            Тип_ВМД = str(i[0])
            Відправник = str(i[1])
            Відправник_2 = str(i[2])
            ОКПЕО_Одержувач = str(i[3])
            Одержувач = str(i[4])
            Адресa_Одержувача = str(i[5])
            ОКПЕО_Декларанта = str(i[6])
            Декларант = str(i[7])
            Адресa_Декларанта = str(i[8])
            МИТНИЙ_ОРГАН = str(i[9])
            номер_ВМД = str(i[10])
            Дата_випуску = str(i[11])
            Товар_номер = str(i[12])
            Код_товару = str(i[13])
            Опис_товару = str(i[14])
            Торгівельна_марка = str(i[15])
            Країна_відправлення = str(i[16])
            Торгівельна_країна = str(i[17])
            Код_країни_походженн = str(i[18])
            Вага_брутто_кг = str(i[19])
            Вага_нетто_кг = str(i[20])
            Упаковка = str(i[21])
            Додаткова_одиниця_виміру = str(i[22])
            Кількість_в_одиницяx_виміру = str(i[23])
            шт = str(i[24])
            Фактурна_вартість = str(i[25])
            Митна_вартість = str(i[26])
            кг = str(i[27])
            Курс = str(i[28])
            Код_МВВ = str(i[29])
            СТ_55 = str(i[30])
            Ставка_мита = str(i[31])
            контракт = str(i[32])
            ТЗ_на_кордоні = str(i[33])
            номер_контейнеру = str(i[34])
            Процедура = str(i[35])
            Митний_орган = str(i[36])
            Умови_поставки = str(i[37])

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
            self.full_list.append(test_dict)

    def save_to_json(self):

        with open('file.json', 'w') as file:
            json.dump(self.full_list, file)
            print('Job well done!')
            c.close_connect()
            print('Connect is close')


c = Connect()
d = Download()
d.download_to_list()
d.save_to_json()
c.get_oll_colunms()
