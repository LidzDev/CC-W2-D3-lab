from src.pub import Pub
class Customer:

    def __init__(self, input_name, input_wallet, input_age):
        self.name = input_name
        self.wallet = input_wallet
        self.age = input_age
        self.drunkenness_level = 0

    def pay(self, input_amount):
        self.wallet -= input_amount
    
    def buy_drink(self, input_drink, input_age):
        if (Pub.sell_drink(input_drink, input_age)):
            self.pay(input_drink.price)
        