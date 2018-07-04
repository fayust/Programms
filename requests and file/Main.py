import re
import requests
import json




def write_to_file(file, data, mode='w'):

    print('Writing to {}\n'.format(file))

    with open(file, mode) as newfile:
        newfile.write(data)


def read_file_data(file):

    print('Reading from {}\n'.format(file))

    try:
        opened_file = open(file)
        data = opened_file.read()
    finally:
        opened_file.close()

    return data




def get_service_data(url):

    result = requests.get(url)

    if result.status_code == 200:
        return result
    else:
        raise RuntimeError("Request from url = '{}' ended with code {}".format(url, result.status_code))


# ОСНОВАЯ ФУНКЦИЯ МОДУЛЯ
def main():
    '''+ Реализовать две функции: write_to_file(data) и read_file_data().
    Которые соотвественно: пишут данные в файл и читают данные из файла.'''

    print('***** TASK 9 part 1 *****\n')
    textdata = 'Hello, this is the example of the data!\nThis is the last line of this text\n'
    print('\nDATA TO SAVE IN FILE:',textdata)
    write_to_file('some_data.txt', textdata)
    print(read_file_data('some_data.txt'))

#Реализовать следующую логику: получать при помощи requests данные сервиса https://jsonplaceholder.typicode.com/
#(сущность можно выбрать любую, например https://jsonplaceholder.typicode.com/comments),
#выводить в консоль все пары заголовки, сохранять полученный json в файл на диск'''

    print('\n***** TASK 9 part 2 *****\n')
    response = get_service_data('https://jsonplaceholder.typicode.com/')
    dict_for_json = {}
    for hdr, value in response.headers.items():
        dict_for_json[hdr] = value
        print('{}:{}\n'.format(hdr, value))

    print('\nJSON response saved in file \'site_response.json\'')
    write_to_file('site_response.json', json.dumps(dict_for_json, sort_keys=True, indent=4))

#Обратиться с странице https://habrahabr.ru/. Получить текст страницы.
#При помощи регулярных выражений нужно получить все ссылки со страницы на другие.
#Ответить себе на вопрос удобно ли так делать?

    print('\n***** TASK 9 part 3 *****\n')
    habrahabr_url = 'https://habrahabr.ru/'
    habrahabr_response = requests.get(habrahabr_url)
    if habrahabr_response.status_code == 200:
        #Если перед открывающей кавычкой стоит символ 'r' (в любом регистре), то механизм экранирования отключается.
        link_pattern = r'<a[^><]*href=[\'"]([^><\'"]*)[\'"][^><]*>'
        #links = re.findall(r'href="(.*?)"', r.text, flags=re.IGNORECASE)    тоже подходит.
        # В скобках (.*?) указывается группа, именно то что мы извлечем из найденного и поместим в переменную links
        print('Links from {} saved in file \'site_links.txt\''.format(habrahabr_url))
        write_to_file('site_links.txt', '')
        for link_string in re.findall(link_pattern, habrahabr_response.text):
            write_to_file('site_links.txt', link_string + '\n', mode = 'a')
            print(link_string)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print('Shutting down, bye!')