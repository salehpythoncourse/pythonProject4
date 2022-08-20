import math_helpers
from math_helpers import Fruit
class t(Fruit):
    def __init__(self,flavor):
        print(flavor)
    def __str__(self):
        return f"A {self.color} apple with a  taste"
def get_name_author(author):
    print(author)
print(math_helpers.multiply(10, 20))
print(math_helpers.multiply(10, 20, 30, 40))

print('------')

print(math_helpers.avg(10, 12, 14, 20))
print(math_helpers.avg())

print(help(math_helpers))