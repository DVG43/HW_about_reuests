from pprint import pprint



import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
                'Content-Type': 'application/json',
                'Authorization': 'OAuth {}'.format(self.token)
        }

    def get_files_list(self, file_path: str):
        files_url = file_path
        headers = self.get_headers()
        response = requests.get(url=files_url, headers=headers)
        return response.json()

    # def upload(self, file_path: str):
    #     """Метод загружает файлы по списку file_list на яндекс диск"""


    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        pprint(response.json())
        return response.json()

    def upload_file_to_disk(self, disk_file_path, filename):
        href = self._get_upload_link(disk_file_path=disk_file_path).get("href", "")
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")




if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 'https://cloud-api.yandex.net/v1/disk/resources/files'
    token = '****************'
    uploader = YaUploader(token)
    pprint(uploader.get_files_list(path_to_file))

    putloader = YaUploader(token)
    fail_list = ['new_tecst.txt','new_1.txt'] # по этому списку идет загрузка из текущей директории
    for n_file in fail_list:
        putloader.upload_file_to_disk(f"Netologi/{n_file}", f"{n_file}")










# result = uploader.upload(path_to_file)


   # https: // disk.yandex.ru / client / disk / Netologi/v1/disk
#"https: // disk.yandex.ru / client / disk / Netologi / upload"
#https://docviewer.yandex.ru/view/1537863710/
#https://yandex.ru/dev/disk/poligon/v1/disk

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