import requests

class Player:
    def __init__(self, dict):
        for field in ["name", "nationality", "goals", "assists", "team"]:
            setattr(self, field, dict.get(field, "-"))
    
    def __str__(self):
        return "{:25} {:5} {:3}  + {:3}  ={:4}".format(
                self.name, self.team, self.goals, self.assists,
                self.goals + self.assists)


class PlayerReader:
    def __init__(self, url):
        self.url = url

    def get_players(self):
        response = requests.get(self.url).json()
        return [Player(player_dict) for player_dict in response]


class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        players_filtered = filter(
                lambda p: p.nationality == "FIN",
                self.reader.get_players())

        players_sorted = sorted(
                players_filtered,
                key=lambda p: p.goals + p.assists,
                reverse=True)

        return players_sorted
