import json
import info
import db
import elastic

if __name__ == '__main__':
    host = info.host
    user = info.user
    pwd = info.password

    rows = db.get_rows(host, user,pwd)
    
    for row in rows:
        id, ip, ts, desc, revid = row[0], row[1], row[2], row[3], row[4]
        print(f'[+] Checking IP {ip}')
        for ep in info.endpoints:
            print(f'[+] Requesting from {ep}')
            resp_json = elastic.lookup(ep, ip)
            found = resp_json['hits']['total']['value']
            if found != 0:
                print(f'[!] Found {found} entries')
                elastic.write_file('results', 'test_output.txt', ip, found)
                break
            else:
                pass
                # Process here
        
