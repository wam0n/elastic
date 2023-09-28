import requests
import json
import info
import sys
import os

def write_file(dir, filename, info, found, ep):
    filepath = os.path.join(dir, filename)
    ep = ep.split('/')[-2]
    with open(filepath, 'a') as f:
        f.write(f'{info}:{found}:{ep}\n')

def lookup(url, ip):
    info.json_body['query']['bool']['must'][0]['query_string']['query'] = f'sourceAddress:{ip}'
    response = requests.get(url=url, json=info.json_body)
    print(f'[+] Response code: {response.status_code}')
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        raise Exception("Server not response")

if __name__ == '__main__':
    pass

