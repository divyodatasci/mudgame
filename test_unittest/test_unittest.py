import unittest
from user import User
from game import Game
import login


class test_login(unittest.TestCase):
    def test_correct_credentials(self):
        user=login.login_user('mistu1smiley','mistu113')
        print(user.username)
        self.assertEqual(user.username,'mistu1smiley')

    
class test_game_movements(unittest.TestCase):
    def test_beginning_to_east(self):
        user = User(username = "DavidUsername", password = "DavidPassword", name="Dave", sex="Male",
         energy=800, fighting_skill=500, wealth=100, location='beginning')
        game=Game(user)
        self.assertEqual(game.getNextLocation('east'),'temple')
    def test_temple_to_west(self):
        user = User(username = "DavidUsername", password = "DavidPassword", name="Dave", sex="Male", 
            energy=800, fighting_skill=500, wealth=100, location='temple')
        game=Game(user)
        self.assertEqual(game.getNextLocation('west'),'beginning')

    def test_temple_to_w(self):
        user = User(username = "DavidUsername", password = "DavidPassword", name="Dave", sex="Male", 
         energy=800, fighting_skill=500, wealth=100, location='temple')
        game=Game(user)
        self.assertEqual(game.getNextLocation('w'),'beginning')
    
    def test_temple_to_east(self):
        user = User(username = "DavidUsername", password = "DavidPassword", name="Dave", sex="Male", 
         energy=800, fighting_skill=500, wealth=100, location='temple')
        game=Game(user)
        self.assertEqual(game.getNextLocation('east'),'nowhere')

    def test_temple_to_e(self):
        user = User(username = "DavidUsername", password = "DavidPassword", name="Dave", sex="Male", 
         energy=800, fighting_skill=500, wealth=100, location='temple')
        game=Game(user)
        self.assertEqual(game.getNextLocation('e'),'nowhere')

    def test_river_to_east(self):
        user = User(username = "DavidUsername", password = "DavidPassword", name="Dave", sex="Male",
         energy=800, fighting_skill=500, wealth=100, location='river')
        game=Game(user)
        self.assertEqual(game.getNextLocation('east'),'beginning')
    
    def test_river_to_west(self):
        user = User(username = "DavidUsername", password = "DavidPassword", name="Dave", sex="Male",
         energy=800, fighting_skill=500, wealth=100, location='river')
        game=Game(user)
        self.assertEqual(game.getNextLocation('west'),'nowhere')
    