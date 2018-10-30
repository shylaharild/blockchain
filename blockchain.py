# Initialising our blockchain list
blockchain = []


def get_last_blockchain_value():
    """ Returns the last value of the current blockchain. """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transaction(transaction_amount, last_transaction_value=[1]):
    """ Appends a new value to the blockchain as well as the last trasaction value to it.

    Arguments:
        :transaction_amount: The amount to be added
        :last_transaction_value: The last transaction amount (default[1])
    """
    if last_transaction_value == None:
        last_transaction_value = [1]
    blockchain.append([last_transaction_value, transaction_amount])


def get_transaction_value():
    """ Returns the input value from the user (new transaction amount) as a float. """
    return float(input('Your transaction amount please: '))


def get_user_choice():
    user_input = input("Your choice: ")
    return user_input


def print_blockchain_elements():
    # Output Blockchain list to the console
    for block in blockchain:
        print("Outputting Block")
        print(block)


def verify_chain():
    block_index = 0
    is_valid = True
    for block in blockchain:
        if block_index == 0:
            block_index += 1
            continue
        elif block[0] == blockchain[block_index - 1]:
            print("block[0] value: " + str(block[0]))
            print("previous block value : " + str(blockchain[block_index - 1]))
            is_valid = True
        else:
            print("block[0] value: " + str(block[0]))
            print("previous block value : " + str(blockchain[block_index - 1]))
            is_valid = False
            break
        block_index += 1
    return is_valid

    # Print the value
print(blockchain)

while True:
    print("Please choose")
    print("1. Add a new transaction value")
    print("2. Output the blockchain blocks")
    print('h: Manipulate the chain')
    print("q. Quit")
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_transaction(tx_amount, get_last_blockchain_value())
    elif user_choice == '2':
        print_blockchain_elements()
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_choice == 'q':
        break
    else:
        print("Input was invalid. Please pick a value from the list!")
    if not verify_chain():
        print("Invalid Blockchain!!")
        break


print("Done!")
