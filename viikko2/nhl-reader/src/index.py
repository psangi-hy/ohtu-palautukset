import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"
    response = requests.get(url).json()

    players_filtered = filter(
            lambda p: p.nationality == "FIN",
            (Player(player_dict) for player_dict in response))

    players_sorted = sorted(
            players_filtered,
            key=lambda p: p.goals + p.assists,
            reverse=True)

    for player in players_sorted:
        if player.nationality == "FIN":
            print(player)

if __name__ == "__main__":
    main()
