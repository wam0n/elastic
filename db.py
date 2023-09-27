import mysql.connector
import info

def get_rows(host, user, pwd):
    my_db = mysql.connector.connect(host=host, user=user, password=pwd, database=info.db)
    cursor = my_db.cursor()
    query = f'SELECT * FROM {info.table}'
    cursor.execute(query)
    result = cursor.fetchall()
    return result

