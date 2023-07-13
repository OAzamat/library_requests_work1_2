# –--------------------WORK 1-----------------
from pprint import pprint
import requests
import json

response = requests.get('https://akabab.github.io/superhero-api/api/all.json')

names_of_characters = ['Hulk', 'Captain America', 'Thanos']
intelligence = {}

if response.status_code == 200:
    for character in response.json():
        if character['name'] in names_of_characters:
            response.json()[0]['powerstats']['intelligence']
            intelligence[character['powerstats']['intelligence']] = character['name']
            sorted_intelligence = dict(sorted(intelligence.items()))
            print(f"Самый умный {character['name']}, интелект: {character['powerstats']['intelligence']}")




# –--------------------WORK 2-----------------
import requests
import os

class YaUploader:

    base_host = 'https://cloud-api.yandex.net:443/'

    def __init__(self, token: str):
        self.token = token

    def authorization(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        url = 'v1/disk/resources/upload/'
        request_url = self.base_host + url
        params = {'path': 'file.docx', 'overwrite': True}
        resp = requests.get(request_url, headers = self.authorization(), params=params).json()
        upload_link = resp.get('href')
        response = requests.put(upload_link, data=open(path_to_file, 'rb'), headers=self.authorization())
        print(response.status_code)


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = os.path.abspath('KUOK.txt')
    token = ...