import requests

URL = "https://fantasy.premierleague.com/api/bootstrap-static/"


def fetch_fpl_data():
    response = requests.get(URL)

    if response.status_code == 200:
        data = response.json()

        players = data['elements']

        print(f"Connection successful! Loaded {len(players)} players into memory.")
        print("\nKeys available for a single player:")
        print(list(players[0].keys())[:10])

        return players
    else:
        print(f"API Connection Failed. HTTP Status: {response.status_code}")
        return None


all_players = fetch_fpl_data()