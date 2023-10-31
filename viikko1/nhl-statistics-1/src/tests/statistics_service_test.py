import unittest
from statistics_service import StatisticsService, sort_by_points
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def test_sort_by_points(self):
        player = Player("Semenko", "EDM", 4, 12)
        points = sort_by_points(player)
        self.assertEqual(points, 4 + 12)

    def test_search_existing(self):
        res = self.stats.search("etz")
        self.assertEqual(str(res), str(Player("Gretzky", "EDM", 35, 89)))

    def test_search_nonexisting(self):
        res = self.stats.search("Horvat")
        self.assertIsNone(res)

    def test_team_existing(self):
        edm = self.stats.team("EDM")
        self.assertEqual(len(edm), 3)
        self.assertTrue(all(p.team == "EDM" for p in edm))

    def test_team_nonexisting(self):
        invented_team = self.stats.team("INV")
        self.assertEqual(len(invented_team), 0)

    def test_top(self):
        players_sorted = [
            Player("Gretzky", "EDM", 35, 89),
            Player("Lemieux", "PIT", 45, 54),
            Player("Yzerman", "DET", 42, 56),
            Player("Kurri",   "EDM", 37, 53),
            Player("Semenko", "EDM", 4, 12)
        ]
        for i in range(0, 6):
            res = self.stats.top(i)
            self.assertEqual(len(res), i)
            for j in range(i):
                self.assertEqual(str(res[j]), str(players_sorted[j]))
