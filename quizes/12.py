import os
import requests
import urllib
from bs4 import BeautifulSoup, UnicodeDammit

url_entryway = 'http://www.leagueoflegends.co.kr/?m=news&cate=notice'

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36',

}


def crawler(url_entryway):
    r = requests.get(url_entryway, headers=headers)

    main_page_text = r.text

    soup = BeautifulSoup(main_page_text, "lxml")

    data_containers = soup.find_all("tbody")

    for d in data_containers:
        print(d.text)


if __name__ == '__main__':
    crawler(url_entryway)