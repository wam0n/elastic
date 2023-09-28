import time
import json
import info
import db
import elastic
import requests
import os

if __name__ == '__main__':
    host = info.host
    user = info.user
    pwd = info.password

    end_time = int(time.time())

    # Get receiver id
    resp1 = db.get_rows(host, user, pwd, info.mon_db, info.q1)
    for row1 in resp1:
        revid = row1[0]
        index_id = row1[1]
        # Get IPs
        resp2 = db.get_rows(host, user, pwd, info.mon_db, info.q2.format(revid))
        # Get Servers
        resp3 = db.get_rows(host, user, pwd, info.siem_db, info.q3.format(index_id))
        # Loop through server & craft url
        for row2 in resp3:
            name = row2[0]
            server = info.servers[row2[1]]
            url = f'http://{server}:9200/{name}/_search'
            # Blocklist
            for row3 in resp2:
                ip = row3[0]
                start_time = row3[2]
                desc = row3[3]
                print(f'[+] Requesting from {url}')
                resp_json = elastic.lookup(url, ip)
                found = (resp_json['hits']['total']['value'])
                if found != 0:
                    print(f'[!] Found {found} entries')
                else:
                    # Delete from DB
                    print(f'[+] Deleting {ip} from database')
                    db.delete(host, user, pwd, ip, revid)
                    print(f'[+] Inserting {ip} into delist')
                    db.insert(host, user, pwd, ip, revid, start_time, end_time, desc)
            print()


