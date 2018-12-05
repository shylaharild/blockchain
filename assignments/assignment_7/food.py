# 1) Create a Food class with a “name” and a “kind” attribute as well as a “describe()” method (which prints “name” and “kind” in a sentence).
# 2) Try turning describe() from an instance method into a class and a static method. Change it back to an instance method thereafter.

class Food:
    # Answer for Q2 - Class Method
    # This is the class attribute directly instantiated for the class
    # name = 'name'
    # kind = 'kind'

    # Answer for Q1 & Q2 - Static Method
    # This is the instance attribute used with constructor
    def __init__(self, name, kind):
        self.name = name
        self.kind = kind

    def __repr__(self):
        return 'Name: {}, Kind: {}'.format(self.name, self.kind)

    # Answer for Q1
    def describe(self):
        print('The name of the food is {} and it is a {}'.format(self.name, self.kind))

    # Answer for Q2 - Static Method
    # @staticmethod
    # def describe(name, kind):
    #     print('The name of the food is {} and it is a {}'.format(name, kind))

    # Answer for Q2 - Class Method
    # @classmethod
    # def describe(cls):
    #     print('The name of the food is {} and it is a {}'.format(cls.name, cls.kind))

# This is a normal method of calling the class using object. This use Instance attributes
# Answer for Q1
f = Food('apple', 'fruit')
f.describe()

# This is using the static method for class. This uses Instance attributes
# Answer for Q2 - Static Method
# fsm = Food('orange', 'fruit')
# fsm.describe('orange', 'fruit')

# This is using the class method for class. This uses class attributes
# Answer for Q2 - Class Method
# Food.kind = 'seafood'
# Food.name = 'fish'
# Food.describe()

# 3) Create a  “Meat” and a “Fruit” class – both should inherit from “Food”. Add a “cook()” method to “Meat” and “clean()” to “Fruit”.
class Meat(Food):
    def __init__(self, name):
        super().__init__(name, 'meat')

    def cook(self):
        print("I'm cooking")

class Fruit(Food):
    def __init__(self, name):
        super().__init__(name, 'fruit')

    def clean(self):
        print("I'm clean")

m = Meat('Pork')
m.describe()
m.cook()

fr = Fruit('banana')
fr.describe()
fr.clean()

# 4) Overwrite a “dunder” method to be able to print your “Food” class.
print(m)
print(fr)

