'''html страница всегда читается в виде массива байт. Это значит, что для удобства обработки, строки нужно декодировать в utf-8 с помощью метода decode(‘utf-8’).
Задача состоит в том, чтобы вытащить с сайта математического факультета список всех сотрудников и их контактные данные.'''

import urllib.request

# url, на котором находится список преподователей
link = urllib.request.urlopen('http://math.csu.ru/index.php?option=com_content&view=article&id=56&Itemid=70')

lines = []
for line in link.readlines():
    # взяли все строки с сотрудниками
    # Каждый сотрудник начинается с тегов <li><a href .....
    if line.find(b'<li>') != -1 and line.find(b'a href') != -1:
        lines.append(line)

link.close()

# Переводим bytes в str
for i in range(len(lines)):
    lines[i] = lines[i].decode('utf-8')

# Можно работать как с обычной строкой
for i in range(len(lines)):
    # Убираем все лишнее
    lines[i] = lines[i].replace('\t\t\t<li>', '')
    lines[i] = lines[i].replace('\"', '')
    lines[i] = lines[i].replace('<a href=', '')
    lines[i] = lines[i].replace('target=_blank>', '')
    lines[i] = lines[i].replace('</a></li>', '')
    lines[i] = lines[i].replace('</ul>', '')
    lines[i] = lines[i].replace("\r\n", '')

# Фио сотрудников
names = []
# URL`ы с их контактными данными
urls = []
for line in lines:
    words = line.split(' ')
    urls.append(words[0])
    name = words[1] + ' ' + words[2] + ' ' + words[3]
    names.append(name)

# Теперь нужно сходить на ссылку каждого и вытащить контактные данные
contacts = []
for url in urls:
    link = urllib.request.urlopen(url)

    # Данные лежат в <div class="fields ContactInfo">
    for line in link.readlines():
        pos = line.find(b'<div class="fields ContactInfo')
        if pos != -1:
            line = line[pos:]
            # С этого тега заканчивается слово "Контактные данные:" и начинаются сами данные
            start = line.find(b'</b>')
            # Сразу после контактов закрывается тег div
            end = line.find(b'</div>')

            contacts.append(line[start + len(b'</b>'): end].decode('utf-8'))

            break

    link.close()

for i in range(len(names)):
    print(names[i], ' : ', contacts[i])