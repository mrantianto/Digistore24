import requests

# Digistore24 API-Key
API_KEY = '1277151-f5lPrSrxftJdXye9ee793QqGhvAGJ3fmdmfoMDb6'
BASE_URL = 'https://www.digistore24.com/api/call/createVoucher'

# Liste mit Gutschein-Codes (zum Beispiel 350 Codes)
codes_liste = ['code1', 'code2', 'code3', 'code4']  # Ersetze dies durch deine 350 Codes

def erstelle_gutschein(code):
    # Daten für den Gutschein mit dem jeweiligen Code
    voucher_data = {
        'data[code]': code,  # Gutschein-Code
        'data[product_ids]': '12345',  # Produkt-ID (Beispiel)
        'data[first_amount]': 400.00,  # Rabatt für die erste Zahlung
        'data[other_amounts]': 0.00,  # Rabatt für Folgezahlungen
        'data[currency]': 'EUR',  # Währung
        'data[is_active]': '1',  # Der Gutschein ist aktiv (1 entspricht True)
        'data[expires_at]': '2024-03-11 00:00:00',  # Gültig bis
        'data[is_count_limited]': '1',  # Gutschein nur einmal anwendbar (1 entspricht True)
        'data[count_left]': '1',  # Anzahl der verfügbaren Verwendungen
        'data[upgrade_policy]': 'other_only',  # Rabatt nur auf Folgezahlungen
        'data[note]': 'VO Community Bella',  # Notiz
    }

    # HTTP-Header für die API-Anfrage
    headers = {
        'X-DS-API-KEY': API_KEY,
        'Accept': 'application/json'  # Antwort im JSON-Format
    }

    # Anfrage an die API senden
    response = requests.post(BASE_URL, headers=headers, data=voucher_data)

    # Statuscode und Antworttext drucken
    print(f'Status Code: {response.status_code} für Gutschein: {code}')
    print(f'Response Text: {response.text}')

    # Prüfen, ob die Anfrage erfolgreich war
    if response.status_code == 200:
        api_response = response.json()
        if api_response['result'] == 'success':
            print(f"Gutschein {code} erfolgreich erstellt: {api_response['data']}")
        else:
            print(f"Fehler für Gutschein {code}: {api_response['message']}")
    else:
        print(f'Fehler bei der Anfrage für Gutschein {code}: {response.status_code}')


# Hauptprogramm, das die Codes aus der Liste durchgeht und erstellt
if __name__ == "__main__":
    for code in codes_liste:
        erstelle_gutschein(code)
