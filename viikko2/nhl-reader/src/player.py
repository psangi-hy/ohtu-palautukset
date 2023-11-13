class Player:
    def __init__(self, dict):
        for field in ["name", "nationality", "goals", "assists", "team"]:
            setattr(self, field, dict.get(field, "-"))
    
    def __str__(self):
        return "{} team {} goals {} assists {}".format(
                self.name, self.team, self.goals, self.assists)
