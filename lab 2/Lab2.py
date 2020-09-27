import requests
from bs4 import BeautifulSoup, SoupStrainer
from collections import OrderedDict
from urllib.parse import urlparse
import lxml
import datetime

DOMAIN = '91.210.252.240/broken-links/'
HOST = 'http://' + DOMAIN
links = set()  # множество всех ссылок
linkforignore = ('None', 'tel://1234567920', 'mailto:info@yoursite.com') # ссылки, которые мы в процессе кода игнорируем

def add_all_links_recursive(url, maxdepth=1):
    # извлекает все ссылки из указанного `url`
    # и рекурсивно обрабатывает их
    # глубина рекурсии не более `maxdepth`

    # список ссылок, от которых в конце мы рекурсивно запустимся
    links_to_handle_recursive = []

    # получаем html код страницы
    request = requests.get(url)
    # парсим его с помощью BeautifulSoup
    soup = BeautifulSoup(request.content, 'lxml')
    # рассматриваем все теги <a>
    for tag_a in soup.find_all('a'):
        # получаем ссылку, соответствующую тегу
        link = tag_a.get('href')
        # `/pricing.html` --- это относительная ссылка
        # `http://91.210.252.240/broken-links/pricing.html` --- это абсолютная ссылка

        if not(str(link) in linkforignore):
            if (link == 'https://colorlib.com'): # фича
                links.add(link)
            else:
                links.add(HOST + link)   # преобразуем относительную ссылку в абсолютную
                links_to_handle_recursive.append(HOST + link)

    if maxdepth > 0:
        for link in links_to_handle_recursive:
            add_all_links_recursive(link, maxdepth=maxdepth - 1)



def main():
    add_all_links_recursive(HOST)
    foutvalidink = open('valid.txt', 'w', encoding='utf-8')
    foutinvalidink = open('invalid.txt', 'w', encoding='utf-8')
    count = 0;
    for link in links:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, ke Gecko) Chrome/61.0.3163.100 Safari/537.36'}
        status = requests.get(link, headers=headers).status_code # получение статус кодов при запросе на сайт
        if (status == 200): # запись валидных в один файл, невалидных - в другой
            foutvalidink.write(str(link) + ' ' + str(status) + '\n')
        else:
            foutinvalidink.write(str(link) + ' ' + str(status) + '\n')
            count += 1

    foutvalidink.write('Ссылок - ' + str(len(links)-count) + '\n')
    foutvalidink.write('Время проверки ' + str(datetime.datetime.now()))
    foutinvalidink.write('Ссылок - ' + str(count) + '\n')
    foutinvalidink.write('Время проверки ' + str(datetime.datetime.now()))
    foutvalidink.close()
    foutinvalidink.close()

if __name__ == '__main__':
    main()
