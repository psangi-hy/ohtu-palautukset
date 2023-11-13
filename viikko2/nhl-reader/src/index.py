import requests
from player import Player, PlayerReader, PlayerStats

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    for player in stats.top_scorers_by_nationality("FIN"):
        print(player)

if __name__ == "__main__":
    main()
