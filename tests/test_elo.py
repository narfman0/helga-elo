import mock
import unittest
from mongomock import MongoClient
from unittest import TestCase
from helga_elo.plugin import add_result, get_player_elo, set_player_elo


class TestElo(TestCase):
    def setUp(self):
        super(TestElo, self).setUp()
        self.db_patch = mock.patch(
            'pymongo.MongoClient',
            new_callable=lambda: MongoClient
        )
        self.db_patch.start()
        self.addCleanup(self.db_patch.stop)
        self.game = 'pingpong'
        self.player1 = 'narfman0'
        self.player2 = 'helga'
        self.initial_elo = 1000

    def test_elo(self):
        set_player_elo(self.game, self.player1, self.initial_elo)
        set_player_elo(self.game, self.player2, self.initial_elo)
        self.assertEqual(get_player_elo(self.game, self.player1), get_player_elo(self.game, self.player2))
        add_result(self.game, self.player1, self.player2)
        add_result(self.game, self.player1, self.player2)
        self.assertTrue(get_player_elo(self.game, self.player1) > get_player_elo(self.game, self.player2))
        add_result(self.game, self.player2, self.player1)
        self.assertTrue(get_player_elo(self.game, self.player1) > get_player_elo(self.game, self.player2))
        add_result(self.game, self.player2, self.player1)
        add_result(self.game, self.player2, self.player1)
        add_result(self.game, self.player2, self.player1)
        add_result(self.game, self.player2, self.player1)
        self.assertTrue(get_player_elo(self.game, self.player1) < get_player_elo(self.game, self.player2))


if __name__ == '__main__':
    unittest.main()
