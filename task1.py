from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin


URL = 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'
alphabet = [chr(i) for i in range(ord('А'), ord('Я') + 1)]
response = requests.get(URL)
count_animal = {}
for alpha in alphabet:
    count_animal[alpha] = 0


soup = BeautifulSoup(response.content, 'html.parser')

flag = True
while flag:
    div = soup.find(id='mw-pages')
    url_next_page = div.find_all('a', {'title': 'Категория:Животные по алфавиту'})[-1]
    url_next_page = urljoin(URL, url_next_page.get('href'))

    animals = div.find('div', {'dir': 'ltr'}).find_all('a')
    for animal in animals:
        current_name_animal = animal.get('title')
        
        if current_name_animal:
            # print(current_name_animal)
            #                         == latin letter A
            if current_name_animal[0] == 'A':
                flag = False
                break
            if current_name_animal[0] in count_animal:
                count_animal[current_name_animal[0]] += 1
    
    response = requests.get(url_next_page)
    soup = BeautifulSoup(response.content, 'html.parser')

for key in count_animal:
    print(f'{key}: {count_animal[key]}')
