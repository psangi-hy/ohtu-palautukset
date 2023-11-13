import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"
    response = requests.get(url).json()

    players = [Player(player_dict) for player_dict in response]

    for player in players:
        if player.nationality == "FIN":
            print(player)

if __name__ == "__main__":
    main()
