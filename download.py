import requests
import json

# Wstaw swój klucz API ClickMeeting
api_key = 'eua598e517c7cd6036fe9ba204d1d50c5a6334db55'

# Endpoint API dla listy nagrań
url = 'https://api.clickmeeting.com/v1/conferences'

# Nagłówki z kluczem API
headers = {
    'X-Api-Key': api_key,
    'Content-Type': 'application/json'
}

# Wysyłanie żądania GET do ClickMeeting API
response = requests.get(url, headers=headers)

# Sprawdzanie, czy żądanie zakończyło się sukcesem
if response.status_code == 200:
    # Wypisanie surowej odpowiedzi przed przetworzeniem
    print("Odpowiedź JSON:")
    print(response.text)

    # Parsowanie odpowiedzi JSON
    response_data = response.json()

    # Sprawdzanie, czy istnieje sekcja "conferences" w danych odpowiedzi
    if 'conferences' in response_data:
        conferences = response_data['conferences']
        
        # Wypisanie danych przechowywanych w zmiennej conferences
        print("\nDane przechowywane w zmiennej conferences:")
        print(conferences)

        # Wyświetlanie nagrań dla każdej konferencji
        for conference in conferences:
            if 'recordings' in conference:
                print(f'Nagrania dla konferencji {conference["name"]}:')
                for recording in conference['recordings']:
                    print(f' - {recording["name"]}: {recording["url"]}')
            else:
                print(f'Brak nagrań dla konferencji {conference["name"]}')
    else:
        print("Brak danych o konferencjach w odpowiedzi API")
else:
    print(f'Błąd żądania API: {response.status_code}')
