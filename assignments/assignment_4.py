# 1) Write a normal function that accepts another function as an argument. Output the result of that other function in your “normal” function.
def normal_function(func):
    print(func(100))
# 2) Call your “normal” function by passing a lambda function – which performs any operation of your choice – as an argument.
normal_function(lambda num: num * 100)
print("-*-" * 10)
# 3) Tweak your normal function by allowing an infinite amount of arguments on which your lambda function will be executed.
def second_function(func, *args):
    for arg in args:
        print(func(arg))

second_function(lambda num: num * 2, 43, 78, 87, 52, 9)
print('-*-' * 10)
# 4) Format the output of your “normal” function such that numbers look nice and are centered in a 20 character column.
def third_function(func, *args):
    for arg in args:
        print("The result is : {:^20.2f}".format(func(arg)))

third_function(lambda num: num * 2, 43, 78, 87, 52, 9)
