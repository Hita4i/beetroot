import pyodbc


conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb)};'
    r'DBQ=import.mdb;'
    )

conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

for row in cursor.columns(table='tab'):  # показать все колонки в таблице
    print(row.column_name)




conn.close()
