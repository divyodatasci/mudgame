import unittest
from register import register_user
from user import User
from game import Game
import login


# Class related to testing of registration and login method
class test_login_register(unittest.TestCase):

    # Method to test the register_user functionality
    def test_registration(self):
        user = register_user('vivekkumar','vivek67')
        self.assertEqual(user.username,'vivekkumar')

    # Method to test the login_user method when the provided details are incorrect
    def test_wrong_credentials(self):
        user = login.login_user('vivekkumar','vivek77')
        self.assertEqual(user,'')
    # Method to test the login_user method when the provided details are correct
    def test_correct_credentials(self):
        user=login.login_user('vivekkumar','vivek67')
        self.assertEqual(user.username,'vivekkumar')


# Class related to test of the functionalities within the game and game locations 
class test_game_movements(unittest.TestCase):

    # Method to test the movement of user from beginning to west direction
    def test_beginning_to_west(self):
        user = User(username = "DavidUsername", password = "DavidPassword", name="Dave", sex="Male",
         energy=800, fighting_skill=500, wealth=100, location='beginning')
        game=Game(user)
        self.assertEqual(game.getNextLocation('west'),'river')

    # Method to test the movement of user from beginning to east direction
    def test_beginning_to_east(self):
        user = User(username = "DavidUsername", password = "DavidPassword", name="Dave", sex="Male",
         energy=800, fighting_skill=500, wealth=100, location='beginning')
        game=Game(user)
        self.assertEqual(game.getNextLocation('east'),'temple')
    # Method to test the movement of user from temple to west direction
    def test_temple_to_west(self):
        user = User(username = "DavidUsername", password = "DavidPassword", name="Dave", sex="Male", 
            energy=800, fighting_skill=500, wealth=100, location='temple')
        game=Game(user)
        self.assertEqual(game.getNextLocation('west'),'beginning')

    # Method to test the movement of user from temple to west direction using w command
    def test_temple_to_w(self):
        user = User(username = "DavidUsername", password = "DavidPassword", name="Dave", sex="Male", 
         energy=800, fighting_skill=500, wealth=100, location='temple')
        game=Game(user)
        self.assertEqual(game.getNextLocation('w'),'beginning')
    
    # Method to test the movement of user from temple to east direction
    def test_temple_to_east(self):
        user = User(username = "DavidUsername", password = "DavidPassword", name="Dave", sex="Male", 
         energy=800, fighting_skill=500, wealth=100, location='temple')
        game=Game(user)
        self.assertEqual(game.getNextLocation('east'),'nowhere')

    # Method to test the movement of user from temple to east direction using e command
    def test_temple_to_e(self):
        user = User(username = "DavidUsername", password = "DavidPassword", name="Dave", sex="Male", 
         energy=800, fighting_skill=500, wealth=100, location='temple')
        game=Game(user)
        self.assertEqual(game.getNextLocation('e'),'nowhere')

    # Method to test the movement of user from river to east direction
    def test_river_to_east(self):
        user = User(username = "DavidUsername", password = "DavidPassword", name="Dave", sex="Male",
         energy=800, fighting_skill=500, wealth=100, location='river')
        game=Game(user)
        self.assertEqual(game.getNextLocation('east'),'beginning')
    
    # Method to test the movement of user from river to west direction   
    def test_river_to_west(self):
        user = User(username = "DavidUsername", password = "DavidPassword", name="Dave", sex="Male",
         energy=800, fighting_skill=500, wealth=100, location='river')
        game=Game(user)
        self.assertEqual(game.getNextLocation('west'),'nowhere')

    # Method to test the movement of user from beginning to south direction
    def test_beginning_to_south(self):
        user = User(username = "DavidUsername", password = "DavidPassword", name="Dave", sex="Male",
         energy=800, fighting_skill=500, wealth=100, location='beginning')
        game=Game(user)
        self.assertEqual(game.getNextLocation('south'),'potion_seller')
    
    # Method to test the payCognoblin() method when the user has wealth less than 1000 gold coins
    def test_pay_cognoblin_lose(self):
        user = User(username = "DavidUsername", password = "DavidPassword", name="Dave", sex="Male",
         energy=800, fighting_skill=500, wealth=100, location='beginning')
        game=Game(user)
        self.assertEqual(game.payCognoblin(), False)

    # Method to test the payCognoblin() method when the user has wealth more than 1000 gold coins
    def test_pay_cognoblin_win(self):
        user = User(username = "DavidUsername", password = "DavidPassword", name="Dave", sex="Male",
         energy=800, fighting_skill=500, wealth=1100, location='beginning')
        game=Game(user)
        self.assertEqual(game.payCognoblin(), True)
    


    