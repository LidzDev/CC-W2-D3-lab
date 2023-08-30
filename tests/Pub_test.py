import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):

    def setUp(self):
        self.Pub = Pub("King's Arms", 100)
        self.Pub.drinks = [Drink("Cider", 2), Drink("Beer", 5)]
        self.Customer = Customer("John", 50, 25)
        
    def test_check_underage_drinking(self):
        age_check = self.Pub.check_drinking_age(30)
        self.assertEqual(True, age_check)
        age_check = self.Pub.check_drinking_age(4)
        self.assertEqual(False, age_check)            

    def test_sell_drink(self):
        self.Pub.sell_drink(self.Pub.drinks[0], self.Customer.age)
        self.assertEqual(102, self.Pub.till)
        self.Customer.age = 15
        sale_return = self.Pub.sell_drink(self.Pub.drinks[1], self.Customer.age)
        # self.assertEqual(False, sale_return)
        self.assertEqual(102, self.Pub.till)      

    def test_increase_till(self):
        self.Pub.increase_till(5)
        self.assertEqual(105, self.Pub.till)
        