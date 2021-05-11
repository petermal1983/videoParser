import requests
from bs4 import BeautifulSoup
import urllib.request


'''
    Функция parsing_and_download_videos
    *args -- набор сайтов, с которых происходит скачивание видео
    Функция считывает html-файл с сайта с помощью requests, и создает текстовый
    файл с расширением html.
    После записи и сохранения файла, функция с помощью BeautifulSoup парсит
    теги video и проверяет их src.
    После считывания данных из src, с помощью urlib.request, происходит
    скачивание видео с допиской исходного сайта, т.к. используются
    относительные ссылки.
    Функция, работает только с относительными ссылками и сайтами где есть тег
    html5 videos
    Если необходимо использовать абсолютные ссылки, убираем часть параметра link
    из функции urlretrieve().
'''


def parsing_and_download_videos(*args):
    for link in args:
        count = 0
        response = requests.get(link)
        file = open("download_html_" + str(count) + ".html", "w")
        file.write(response.text)
        file.close()
        with open("download_html_" + str(count) + ".html", "r") as f:
            content = f.read()
            soup = BeautifulSoup(content, 'lxml')
            for tag in soup.findAll("video"):
                try:
                    name_file = tag['src'].split("/")[1].split(".")
                    new_name_file = (name_file[0] + "_download_" + str(count) +
                                     "." + name_file[1])
                    try:
                        print("Downloading videos", name_file, sep="-")
                        urllib.request.urlretrieve(link + tag['src'],
                                                   new_name_file)
                        print("Download is done")
                        count += 1
                    except Exception as e:
                        print("Download is fault", "Problem with: ", e,
                              sep="\n")
                except Exception as e:
                    print("Problem with name, or tag", "More info:", e,
                          sep="\n")  


parsing_and_download_videos("https://shapeshed.com/examples/HTML5-video-element/")