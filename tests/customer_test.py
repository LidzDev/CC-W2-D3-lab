import unittest
from src.customer import Customer
from src.drink import Drink

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("John", 50, 25)
        self.drink = Drink("Cider", 2)

    def test_pay(self):
        self.customer.pay(5)
        self.assertEqual(45, self.customer.wallet)

    def test_buy(self):
        self.customer.buy_drink(self.drink, self.customer.age)
        self.assertEqual(48, self.customer.wallet)        
