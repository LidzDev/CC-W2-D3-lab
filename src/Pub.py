class Pub:
    def __init__(self, input_name, input_till):
        self.name = input_name
        self.till = input_till
        self.drinks = []

    def sell_drink(self, input_drink, input_customer_age):
        if self.check_age(input_customer_age):
            self.increase_till(input_drink.price)
        
    def check_age(self, input_age):
        return(input_age >= 21)       

    def add_drink(self, input_drink):
        self.drinks.append(input_drink)

    def increase_till(self, input_amount):
        self.till += input_amount