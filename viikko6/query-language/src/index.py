from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, Not, HasFewerThan, All, Or
from query_builder import QueryBuilder

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    matchers = [
        And(
            HasAtLeast(5, "goals"),
            HasAtLeast(20, "assists"),
            PlaysIn("PHI")
        ),
        And(
            Not(HasAtLeast(2, "goals")),
            PlaysIn("NYR")
        ),
        And(
            HasFewerThan(2, "goals"),
            PlaysIn("NYR")
        ),
        Or(
            HasAtLeast(45, "goals"),
            HasAtLeast(70, "assists")
        ),
        And(
            HasAtLeast(70, "points"),
            Or(
                PlaysIn("NYR"),
                PlaysIn("FLA"),
                PlaysIn("BOS")
            )
        ),
        QueryBuilder()
            .playsIn("NYR")
            .hasAtLeast(10, "goals")
            .hasFewerThan(20, "goals")
            .build()
    ]

    for matcher in matchers:
        for player in stats.matches(matcher):
            print(player)
        print("")

    print(len(stats.matches(All())))


if __name__ == "__main__":
    main()
