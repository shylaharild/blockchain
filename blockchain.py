# Initialising our blockchain list
blockchain = []


def get_last_blockchain_value():
    """ Returns the last value of the current blockchain. """
    return blockchain[-1]


def add_value(transaction_amount, last_transaction_value=[1]):
    """ Appends a new value to the blockchain as well as the last trasaction value to it.

    Arguments:
        :transaction_amount: The amount to be added
        :last_transaction_value: The last transaction amount (default[1])
    """
    blockchain.append([last_transaction_value, transaction_amount])


def get_transaction_value():
    """ Returns the input value from the user (new transaction amount) as a float. """
    return float(input('Your transaction amount please: '))

def get_user_choice():
    user_input = input("Your choice: ")
    return user_input

def print_blockchain_elements():
    #Output Blockchain list to the console
    for block in blockchain:
        print("Outputting Block")
        print(block)

# Get the first value
tx_amount = get_transaction_value()
add_value(tx_amount)

# Print the value
print(blockchain)

while True:
    print("Please choose")
    print("1. Add a new transaction value")
    print("2. Output the blockchain blocks")
    print("q. Quit")
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_value(tx_amount, get_last_blockchain_value())
    elif user_choice == '2':
        print_blockchain_elements()
    elif user_choice == 'q':
        break
    else:
        print("Input was invalid. Please pick a value from the list!")

print("Done!")
