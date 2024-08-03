import json
import unittest
import coc_api as ca

r = open("../response.json")
test_resp = json.load(r)

class TestGetPlayerHeroes(unittest.TestCase):
    def test_player_heroes_correct_length(self):
        self.assertEqual(len(ca.get_player_heroes(test_resp)), 4)