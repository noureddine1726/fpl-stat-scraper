<<<<<<< HEAD
import cloudscraper
import csv
=======
import requests
>>>>>>> 9845c3e72c495b3dcaa65d1827885d3e2ca56a74

URL = "https://fantasy.premierleague.com/api/bootstrap-static/"


def fetch_fpl_data():
<<<<<<< HEAD
    scraper = cloudscraper.create_scraper(browser={
        'browser': 'chrome',
        'platform': 'windows',
        'mobile': False
    })
    response = scraper.get(URL)
    return response.json()['elements'] if response.status_code == 200 else None


all_players = fetch_fpl_data()

if all_players:
    positions_map = {1: "Goalkeepers", 2: "Defenders", 3: "Midfielders", 4: "Forwards"}

    clean_players = [
        {
            "name": f"{p['first_name']} {p['second_name']}",
            "price": p['now_cost'] / 10.0,
            "total_points": p['total_points'],
            "position_id": p['element_type'],
            "position": positions_map.get(p['element_type'], "Unknown")
        }
        for p in all_players
    ]

    active_players = [p for p in clean_players if p['total_points'] > 0]

    for p in active_players:
        p['roi'] = round(p['total_points'] / p['price'], 2)

    ranked_players = sorted(active_players, key=lambda x: x['roi'], reverse=True)

    filename = "fpl_top_players_all_positions.csv"

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Position", "Rank", "Name", "Price (M)", "Total Points", "ROI"])

        for pos_id, pos_name in positions_map.items():
            top_for_pos = [p for p in ranked_players if p['position_id'] == pos_id][:5]

            print(f"\n--- TOP 5 {pos_name.upper()} ---")
            for rank, player in enumerate(top_for_pos, 1):
                print(
                    f"{rank}. {player['name']} | Prix: {player['price']}M | Pts: {player['total_points']} | ROI: {player['roi']}")
                writer.writerow(
                    [pos_name, rank, player['name'], player['price'], player['total_points'], player['roi']])

    print(f"\nFichier complet exporté avec succès dans {filename}")
=======
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
>>>>>>> 9845c3e72c495b3dcaa65d1827885d3e2ca56a74
