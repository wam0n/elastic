import requests
import json
import info
import sys
import os

def write_file(dir, filename, info):
    filepath = os.path.join(dir, filename)
    with open(filepath, 'w') as f:
        json.dump(info, f, indent=4)

if __name__ == '__main__':
    dir = 'results'
    for ep in info.endpoints:
        print(f'[+] Requesting to {ep}')
        response = requests.get(url=ep)
        write_file(dir, 'test.json', json.loads(response.text))

