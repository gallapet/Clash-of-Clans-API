import json
import unittest
import coc_api as ca

r = open("../response.json")
test_resp = json.load(r)


class TestGetPlayerHeroes(unittest.TestCase):
    def test_player_heroes_correct_length(self):
        self.assertEqual(len(ca.get_player_heroes(test_resp)), 4)

class TestBarbarianKing(unittest.TestCase):
    def test_first_hero_is_barbarian_king(self):
        self.assertEqual(ca.get_player_heroes(test_resp)[0].name, "Barbarian King")
    def test_barbarian_king_is_maxed(self):
        self.assertEqual(ca.get_player_heroes(test_resp)[0].is_max(), True)
