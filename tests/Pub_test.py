import unittest
from src.pub import Pub
from src.drink import Drink

class TestPub(unittest.TestCase):

    def setUp(self):
        self.Pub = Pub("King's Arms", 100)
        self.Pub.drinks = [Drink("Cider", 2), Drink("Beer", 5)]
        
    def test_sell_drink(self):
        self.Pub.sell_drink(self.Pub.drinks[0])
        self.assertEqual(102, self.Pub.till)

    def test_increase_till(self):
        self.Pub.increase_till(5)
        self.assertEqual(105, self.Pub.till)
        