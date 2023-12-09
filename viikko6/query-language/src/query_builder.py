from matchers import And, HasAtLeast, HasFewerThan, PlaysIn

class QueryBuilder:
    def __init__(self):
        self._matchers = []

    def build(self):
        return And(*self._matchers)

    def playsIn(self, team):
        self._matchers.append(PlaysIn(team))
        return self

    def hasAtLeast(self, value, attr):
        self._matchers.append(HasAtLeast(value, attr))
        return self

    def hasFewerThan(self, value, attr):
        self._matchers.append(HasFewerThan(value, attr))
        return self
