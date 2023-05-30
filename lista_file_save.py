import requests
import json

# Wstaw swój klucz API ClickMeeting
api_key = 'eue4dfb12c72cbe9a6b26bd8081e9608b6ccc38501'

# Endpoint API dla listy konferencji
url = 'https://api.clickmeeting.com/v1/conferences'

# Dodawanie parametru 'scope' do żądania, aby pobrać wszystkie wydarzenia
params = {
    'scope': 'all'
}

# Nagłówki z kluczem API
headers = {
    'X-Api-Key': api_key,
    'Content-Type': 'application/json'
}

# Wysyłanie żądania GET do ClickMeeting API z parametrami
response = requests.get(url, headers=headers, params=params)

# Sprawdzanie, czy żądanie zakończyło się sukcesem
if response.status_code == 200:
    # Parsowanie odpowiedzi JSON
    conferences_data = json.loads(response.text)

    total_conferences = 0
    for key in conferences_data:
        total_conferences += len(conferences_data[key])

    processed_conferences = 0

    # Wyświetlanie informacji o konferencjach
    for key in conferences_data:
        conferences = conferences_data[key]
        for conference in conferences:
            print(f'Konferencja: {conference["name"]}')
            print(f'ID: {conference["id"]}')
            print(f'Status: {conference["status"]}')

            if "starts_at" in conference:
                print(f'Data rozpoczęcia: {conference["starts_at"]}')
            if "ends_at" in conference:
                print(f'Data zakończenia: {conference["ends_at"]}')

            recordings_url = f'https://api.clickmeeting.com/v1/conferences/{conference["id"]}/recordings'
            recordings_response = requests.get(recordings_url, headers=headers)

            if recordings_response.status_code == 200:
                recordings = json.loads(recordings_response.text)

                if recordings:
                    print('Nagrania:')
                    for recording in recordings:
                        print(f' - {recording["name"]}: {recording["url"]}')
                else:
                    print('Brak nagrań')

            else:
                print('Błąd podczas pobierania nagrań')

            processed_conferences += 1
            progress = (processed_conferences / total_conferences) * 100
            print(f'\nPostęp: {progress:.2f}%\n')
            print('-' * 80 + '\n')

else:
    print(f'Błąd żądania API: {response.status_code}')
