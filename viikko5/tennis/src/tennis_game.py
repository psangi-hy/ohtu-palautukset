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

    def get_score(self):
        score = ""
        temp_score = 0

        if self.score1 == self.score2:
            score = [
                "Love-All",
                "Fifteen-All",
                "Thirty-All",
                "Deuce"
            ][min(self.score1, 3)]
        elif self.score1 >= 4 or self.score2 >= 4:
            minus_result = self.score1 - self. score2

            if minus_result == 1:
                score = "Advantage " + self.name1
            elif minus_result == -1:
                score = "Advantage " + self.name2
            elif minus_result >= 2:
                score = "Win for " + self.name1
            else:
                score = "Win for " + self.name2
        else:
            for i in range(1, 3):
                if i == 1:
                    temp_score = self.score1
                else:
                    score = score + "-"
                    temp_score = self.score2

                if temp_score == 0:
                    score = score + "Love"
                elif temp_score == 1:
                    score = score + "Fifteen"
                elif temp_score == 2:
                    score = score + "Thirty"
                elif temp_score == 3:
                    score = score + "Forty"

        return score
