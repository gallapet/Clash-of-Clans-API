import coc_api as ca
import unittest
import json

r = open("../response.json")
test_resp = json.load(r)

class TestGetPlayerName(unittest.TestCase):
    def test_get_player_name_matching_name(self):
        self.assertEqual(ca.get_player_name(test_resp), "sample name")

    def test_get_player_name_no_match(self):
        self.assertNotEqual(ca.get_player_name(test_resp), "blah blah")

class TestGetTownHallLevel(unittest.TestCase):
    def test_get_town_hall_level_matching_level(self):
        self.assertEqual(ca.get_town_hall_level(test_resp), 20)

    def test_get_town_hall_level_no_match(self):
        self.assertNotEqual(ca.get_town_hall_level(test_resp), 1)
