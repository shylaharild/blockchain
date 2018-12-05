# 1) Create a Food class with a “name” and a “kind” attribute as well as a “describe()” method (which prints “name” and “kind” in a sentence).

class Food:
    def __init__(self, name, kind):
        self.name = name
        self.kind = kind

    def describe(self):
        print('The name of the food is {} and it is a {}'.format(self.name, self.kind))

f = Food('apple', 'fruit')
f.describe()