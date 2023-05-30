import requests
import os
from datetime import datetime

# Dane uwierzytelniające
api_key = 'eue4dfb12c72cbe9a6b26bd8081e9608b6ccc38501'

# Ścieżka do folderu, w którym zostanie zapisany plik
save_folder = r'D:\!Nagrania_CM\\'

# Pobieranie pliku
def download_file(file_hash):
    url = f'https://api.clickmeeting.com/v1/storage/{file_hash}/download'
    headers = {'Api-Key': api_key}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        file_name = datetime.now().strftime('%Y-%m-%d') + '.mp4'
        save_path = os.path.join(save_folder, file_name)
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print('Plik zapisany:', save_path)
    else:
        print('Wystąpił błąd podczas pobierania pliku:', response.text)

# Główna część skryptu
if __name__ == '__main__':
    file_hash = '2023_04_30'

    download_file(file_hash)
