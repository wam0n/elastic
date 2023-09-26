import mysql.connector
import info

def get_rows(host, user, pwd):
    my_db = mysql.connector.connect(host=host, user=user, password=pwd, database=info.db)
    cursor = my_db.cursor()
    query = f'SELECT * FROM {info.table}'
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def do_work(row):
    id, ip, time, desc, revid = row[0], row[1], row[2], row[3], row[4]
    print(id, ip, time, desc, revid)

