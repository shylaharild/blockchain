# Initialising the variables
name = "Sri"
age = "30"


def get_name():
    name = input("Please enter your name: ")
    return name


def get_age():
    age = input("Please give your age: ")
    return age


def calculate_decade(given_age):
    decade = int(given_age)/10
    return int(decade)


def answer(given_name, given_age):
    print("Your name is " + given_name)
    print("your age is " + given_age + " and you have lived for " +
          str(calculate_decade(given_age)) + " decades")


name = get_name()
age = get_age()
answer(name, age)
