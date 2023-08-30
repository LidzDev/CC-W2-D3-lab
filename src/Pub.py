class Pub:
    def __init__(self, input_name, input_till):
        self.name = input_name
        self.till = input_till
        self.drinks = []

    def sell_drink(self, input_drink):
        self.increase_till(input_drink.price)

    def add_drink(self, input_drink):
        self.drinks.append(input_drink)

    def increase_till(self, input_amount):
        self.till += input_amount