# -*- coding: utf-8 -*-

#import pychecker.checker
import logging
import requests
from bs4 import BeautifulSoup
import json
REQUEST_STATUS_CODE = 200

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s : %(levelname)s : %(message)s') # %(message)s',  filename='error.log') вывод в файл

if __name__ == '__main__':
    req = requests.get('http://storage.mp3cc.org/download/8572563/cU12OTVKVlBlN3ZzeFdCUUZKOFRUaWwxWU1yelkwdElXUENmeCtZZ0JGeE11ZXFmMFF0SHpvbzR5MmtmdVRqRVZnQTdBRjlmMDNCeXFhcWVQWkdETEV4b093MFZQa1VnK0JVdlVDS2l2dFg5UmdselRQcy9oaVZGOGNkMVk4bHk/bratya-grim-kusturica_(mp3.cc).mp3')
    if req.status_code == REQUEST_STATUS_CODE:
       logging.debug('start')
       with open('bratya-grim-kusturica_(mp3.cc).mp3', 'wb') as f:
           f.write(req.content)

print(req.status_code)

