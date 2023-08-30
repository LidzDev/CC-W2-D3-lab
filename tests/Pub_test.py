import unittest
from src.pub import Pub

class TestPub(unittest.TestCase):

    def setUp(self):
        self.Pub = ("King's Arms", 100, [{"name" : "Cider", 
                                          "price" : 2},
                                          {"name" : "Beer",
                                           "price" : 5}])
        

