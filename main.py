import info
import db

if __name__ == '__main__':
    host = info.host
    user = info.user
    pwd = info.password

    rows = db.get_rows(host, user,pwd)
    
    for row in rows:
        db.do_work(row)
