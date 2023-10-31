import unittest
from statistics_service import StatisticsService, sort_by_points, SortBy
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

    def assert_player_equal(self, a, b):
        self.assertEqual(str(a), str(b))

    def test_search_existing(self):
        res = self.stats.search("etz")
        self.assert_player_equal(res, Player("Gretzky", "EDM", 35, 89))

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

    def assert_player_list_equal(self, a, b):
        self.assertEqual(len(a), len(b))
        for i in range(len(a)):
            self.assert_player_equal(a[i], b[i])

    def test_top_by_points(self):
        by_points = [
            Player("Gretzky", "EDM", 35, 89),
            Player("Lemieux", "PIT", 45, 54),
            Player("Yzerman", "DET", 42, 56),
            Player("Kurri",   "EDM", 37, 53),
            Player("Semenko", "EDM", 4, 12)
        ]
        for i in range(0, 6):
            res = self.stats.top(i)
            res_points = self.stats.top(i, SortBy.POINTS)
            self.assertEqual(res, res_points)
            self.assert_player_list_equal(res, by_points[:i])

    def test_top_by_goals(self):
        by_goals = [
            Player("Lemieux", "PIT", 45, 54),
            Player("Yzerman", "DET", 42, 56),
            Player("Kurri",   "EDM", 37, 53),
            Player("Gretzky", "EDM", 35, 89),
            Player("Semenko", "EDM", 4, 12)
        ]
        for i in range(0, 6):
            res = self.stats.top(i, SortBy.GOALS)
            self.assert_player_list_equal(res, by_goals[:i])

    def test_top_by_assists(self):
        by_assists = [
            Player("Gretzky", "EDM", 35, 89),
            Player("Yzerman", "DET", 42, 56),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Semenko", "EDM", 4, 12)
        ]
        for i in range(0, 6):
            res = self.stats.top(i, SortBy.ASSISTS)
            self.assert_player_list_equal(res, by_assists[:i])

    def test_top_invalid_sort_by(self):
        for i in range(0, 6):
            self.assertIsNone(self.stats.top(i, 4))
