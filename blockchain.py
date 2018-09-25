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


def get_input_value():
    """ Returns the input value from the user (new transaction amount) as a float. """
    return float(input('Your transaction amount please: '))

tx_amount = get_input_value()
add_value(tx_amount)

tx_amount = get_input_value()
add_value(last_transaction_value=get_last_blockchain_value(),
          transaction_amount=tx_amount)

tx_amount = get_input_value()
add_value(tx_amount, get_last_blockchain_value())

print(blockchain)
