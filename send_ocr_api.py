import argparse
import json
import os.path
import time
import uuid

import requests

default_url = 'https://37e0b16932ac4be481cc8f3fbda54da4.apigw.ntruss.com/' \
              'custom/v1/7517/6bc8e6825e6e6cf74a0c072c6b4bdad627bbe22ba6f87bb87c20c38ada80d75c/general'
default_key = 'ZFd6WUNlaXBtQW5DYVRPdFNpdUpQSHhRSktCWXp3UUI='

parser = argparse.ArgumentParser(description='')
parser.add_argument('--url', type=str, default=default_url, help='API url.')
parser.add_argument('--key', type=str, default=default_key, help='Secret key.')
parser.add_argument('--path', type=str, help='Document image path.')
args = parser.parse_args()

if __name__ == '__main__':
    path = args.path
    url = args.url
    key = args.key
    
    request_json = {
        'images': [
            {
                'format': 'jpg',
                'name': 'demo'
            }
        ],
        'requestId': str(uuid.uuid4()),
        'version': 'V2',
        'timestamp': int(round(time.time() * 1000))
    }
    payload = {'message': json.dumps(request_json).encode('UTF-8')}
    files = [
        ('file', open(path, 'rb'))
    ]
    headers = {
        'X-OCR-SECRET': key
    }
    
    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    
    with open(os.path.splitext(path)[0] + '.json', 'w', encoding='utf-8') as fout:
        json.dump(response.json(), fout, indent=4, ensure_ascii=False)
