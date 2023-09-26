import mysql.connector
import info


def connect(host, user, pwd):
    my_db = mysql.connector.connect(host=host, user=user, password=pwd, database=info.db)
    return my_db

def do_work(row):
    id, ip, time, desc, revid = row[0], row[1], row[2], row[3], row[4]
    print(id, ip, time, desc, revid)


if __name__ == '__main__':
    host = info.host
    user = info.user
    pwd = info.password

    my_db = connect(host, user,pwd)

    my_cursor = my_db.cursor()

    query = f'SELECT * FROM {info.table}'

    my_cursor.execute(query)

    my_result = my_cursor.fetchall()

    for x in my_result:
        do_work(x)