import random
from datetime import datetime

# 1) Import the random function and generate both a random number between 0 and 1 as well as a random number between 1 and 10.

first_random_number = random.random()
print("Generated random number between 0 and 1 is " + str(first_random_number))
second_random_number = random.randint(1, 10)
print("Generated random number between 1 and 10 is " + str(second_random_number))

# 2) Use the datetime library together with the random number to generate a random, unique value.

print("Using datetime & random " + str(first_random_number) + str(datetime.now()))