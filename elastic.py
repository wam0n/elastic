import requests
import json
import info
import sys
import os

def write_file(dir, filename, info, found):
    filepath = os.path.join(dir, filename)
    with open(filepath, 'a') as f:
        f.write(f'{info} : {found}\n')

def lookup(url, ip):
    info.json_body['query']['bool']['must'][0]['query_string']['query'] = f'sourceAddress:{ip}'
    response = requests.get(url=url, json=info.json_body)
    return json.loads(response.text)

if __name__ == '__main__':
    pass

