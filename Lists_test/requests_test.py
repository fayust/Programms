import requests

response = requests.get('https://httpbin.org/basic-auth/user/passwd', auth=('user', 'passwd'))

print(response.content)
print(response.headers)
#print(response.text)
#b'{\n  "authenticated": true, \n  "user": "user"\n}\n'
print(response.json())
#{'user': 'user', 'authenticated': True}

'''

#print(response.content)  # забрать контент
    #response.json()
    #response.headers
    #response.headers.get('Server')


В requests имеется 2 вида таймаут-исключений:

    ConnectTimeout - таймаут на соединения
    ReadTimeout - таймаут на чтение

>>> import requests
>>> try:
...     response = requests.get('https://httpbin.org/user-agent', timeout=(0.00001, 10))
... except requests.exceptions.ConnectTimeout:
...     print('Oops. Connection timeout occured!')
...     
Oops. Connection timeout occured!
>>> try:
...     response = requests.get('https://httpbin.org/user-agent', timeout=(10, 0.0001))
... except requests.exceptions.ReadTimeout:
...     print('Oops. Read timeout occured')
... except requests.exceptions.ConnectTimeout:
...     print('Oops. Connection timeout occured!')
...     
Oops. Read timeout occured

ConnectionError


>>> import requests
>>> try:
...     response = requests.get('http://urldoesnotexistforsure.bom')
... except requests.exceptions.ConnectionError:
...     print('Seems like dns lookup failed..')
...     
Seems like dns lookup failed..

HTTPError


>>> import requests
>>> try:
...     response = requests.get('https://httpbin.org/status/500')
...     response.raise_for_status()
... except requests.exceptions.HTTPError as err:
...     print('Oops. HTTP Error occured')
...     print('Response is: {content}'.format(content=err.response.content))
...     
Oops. HTTP Error occured
Response is: b'

Я перечислил основные виды исключений, которые покрывают, пожалуй, 90% всех проблем, возникающих при работе с http. 
Главное помнить, что если мы действительно намерены отловить что-то и обработать, то это необходимо явно запрограммировать, 
если же нам неважен тип конкретного исключения, то можно отлавливать общий базовый класс RequestException и действовать уже 
от конкретного случая, например, залоггировать исключение и выкинуть его дальше наверх. Кстати, о логгировании я напишу отдельный подробный пост.

У блога появился свой Telegram канал, где я стараюсь делиться интересными находками из сети на тему разработки программного обеспечения. 
Велком, как говорится :)
Полезные "плюшки"

    httpbin.org очень полезный сервис для тестирования http клиентов, в частности удобен для тестирования нестандартного поведения сервиса
    https://httpbin.org/
    
    httpie консольный http клиент (замена curl) написанный на Python
    https://github.com/jakubroztocil/httpie
    
    responses mock библиотека для работы с requests
    https://github.com/getsentry/responses
    
    HTTPretty mock библиотека для работы с http модулями
    https://github.com/gabrielfalcao/HTTPretty
'''