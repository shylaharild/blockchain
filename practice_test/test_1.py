#1 Create two variables – one with your name and one with your age
#2 Create a function which prints your data as one string
#3 Create a function which prints ANY data (two arguments) as one string
#4 Create a function which calculates and returns the number of decades you already lived (e.g. 23 = 2 decades)

# Initialising the variables
# Answer to Question 1
name = "Sri"
age = "30"


def get_name():
    name = input("Please enter your name: ")
    return name


def get_age():
    age = input("Please give your age: ")
    return age


# Answer to Question 4
def calculate_decade(given_age):
    decade = int(given_age)/10
    return int(decade)


def answer(given_name, given_age):
    # Answer to Question 2
    print("Your name is " + given_name)
    # Answer to Question 3
    print("your age is " + given_age + " and you have lived for " +
          str(calculate_decade(given_age)) + " decades")


name = get_name()
age = get_age()
answer(name, age)
