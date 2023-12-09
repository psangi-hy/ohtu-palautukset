from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, Not, HasFewerThan, All, Or

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    matcher1 = And(
        HasAtLeast(5, "goals"),
        HasAtLeast(20, "assists"),
        PlaysIn("PHI")
    )

    matcher2 = And(
        Not(HasAtLeast(2, "goals")),
        PlaysIn("NYR")
    )

    matcher3 = And(
        HasFewerThan(2, "goals"),
        PlaysIn("NYR")
    )

    matcher4 = Or(
        HasAtLeast(45, "goals"),
        HasAtLeast(70, "assists")
    )

    matcher5 = And(
        HasAtLeast(70, "points"),
        Or(
            PlaysIn("NYR"),
            PlaysIn("FLA"),
            PlaysIn("BOS")
        )
    )

    for matcher in [matcher1, matcher2, matcher3, matcher4, matcher5]:
        for player in stats.matches(matcher):
            print(player)
        print("")

    print(len(stats.matches(All())))


if __name__ == "__main__":
    main()
