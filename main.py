
from pprint import pprint
#
import requests
#
# Нужно определить кто самый умный(intelligence) из трех супергероев- Hulk, Captain America, Thanos.
# Для определения id нужно использовать метод /search/name

# забирпаем информацию из файлов. Получаем три словаря.
# из трехсловарей получаем  значение intelligence
# иыбираем максимальое значени и определяем супергероя.



def get_poverstats ():
        url = f"https://superheroapi.com/api/2619421814940190/character-'Hulk'/powerstats"
        response = requests.get(url, params={'poverstats': 'meaning'})
        return response.json()

# def test_request ():
#      url = "https://httpbin.org/get"
#      response = requests.get(url)
#      pprint(response)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
     name_hero_1 = 'Hulk'
     print (get_poverstats(name_hero_1))



#
# import requests
#
#
# class Reddit:
#
#     def get_popular_videos(self):
#         url = "https://www.reddit.com/r/gifs/top.json?t=day"
#         response = requests.get(url, headers={'User-agent': 'netology'})
#         return response.json()





# from pprint import pprint
#
# import requests
#
#
# class YandexDisk:
#
#     def __init__(self, token):
#         self.token = token
#
#     def get_headers(self):
#         return {
#             'Content-Type': 'application/json',
#             'Authorization': 'OAuth {}'.format(self.token)
#         }
#
#     def get_files_list(self):
#         files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
#         headers = self.get_headers()
#         response = requests.get(files_url, headers=headers)
#         return response.json()
#
#     def _get_upload_link(self, disk_file_path):
#         upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
#         headers = self.get_headers()
#         params = {"path": disk_file_path, "overwrite": "true"}
#         response = requests.get(upload_url, headers=headers, params=params)
#         pprint(response.json())
#         return response.json()
#
#     def upload_file_to_disk(self, disk_file_path, filename):
#         href = self._get_upload_link(disk_file_path=disk_file_path).get("href", "")
#         response = requests.put(href, data=open(filename, 'rb'))
#         response.raise_for_status()
#         if response.status_code == 201:
#             print("Success")