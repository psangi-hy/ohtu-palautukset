class TennisGame:
    def __init__(self, name1, name2):
        self.name1 = name1
        self.name2 = name2
        self.score1 = 0
        self.score2 = 0

    def won_point(self, player_name):
        if player_name == self.name1:
            self.score1 = self.score1 + 1
        elif player_name == self.name2:
            self.score2 = self.score2 + 1

    def _get_score_absolute(self):
        score_names = ["Love", "Fifteen", "Thirty", "Forty"]
        if self.score1 == self.score2:
            return score_names[self.score1] + "-All"
        else:
            return score_names[self.score1] + "-" + score_names[self.score2]

    def _get_score_relative(self):
        leader_name = self.name1 if self.score1 > self.score2 else self.name2
        difference = abs(self.score1 - self.score2)
        return [
            "Deuce",
            "Advantage " + leader_name,
            "Win for " + leader_name
        ][min(difference, 2)]

    def get_score(self):
        if min(self.score1, self.score2) < 3 and max(self.score1, self.score2) < 4:
            return self._get_score_absolute()
        else:
            return self._get_score_relative()
