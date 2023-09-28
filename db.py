import mysql.connector
import info

def get_rows(host, user, pwd, db, query):
    my_db = mysql.connector.connect(host=host, user=user, password=pwd, database=db)
    cursor = my_db.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def delete(host, user, pwd, ip, revid):
    my_db = mysql.connector.connect(host=host, user=user, password=pwd, database=info.mon_db)
    cursor = my_db.cursor()
    query = f'DELETE FROM blocklist WHERE ip=\'{ip}\' AND reciever_id={revid}'
    print(f'[+] Running command "{query}"')
    cursor.execute(query)
    my_db.commit()
    print(f'[+] Deleted {ip}')

def insert(host, user, pwd, ip, revid, start, end, detail):
    my_db = mysql.connector.connect(host=host, user=user, password=pwd, database=info.mon_db)
    cursor = my_db.cursor()
    query = info.q4.format(ip, revid, start, end, detail)
    print(f'[+] Running command {query}')
    cursor.execute(query)
    my_db.commit()
    print(f'[+] Insert {ip}')
