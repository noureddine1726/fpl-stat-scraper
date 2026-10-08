import requests

URL = "https://fantasy.premierleague.com/api/bootstrap-static/"


def fetch_fpl_data():
    response = requests.get(URL)

    if response.status_code == 200:
        data = response.json()
        return data['elements']
    else:
        print(f"API Connection Failed. HTTP Status: {response.status_code}")
        return None


all_players = fetch_fpl_data()

if all_players:
    clean_players = [
        {
            "name": f"{player['first_name']} {player['second_name']}",
            "price": player['now_cost'] / 10.0,
            "total_points": player['total_points'],
            "position": player['element_type']
        }
        for player in all_players
    ]

    print(f"\nSuccessfully cleaned data for {len(clean_players)} players.")
    print("\nSample data for one cleaned player:")
    print(clean_players[0])