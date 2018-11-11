# Initialising our blockchain list
blockchain = []
open_transaction = []
owner = 'Sri'


def get_last_blockchain_value():
    """ Returns the last value of the current blockchain. """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transaction(recipient, sender=owner, amount=1.0):
    """ Appends a new value to the blockchain as well as the last trasaction value to it.

    Arguments:
        :sender: The sender of the coins
        :sender: The recipient of the coins 
        :amount: The amoutn of coins sent with the transaction. (default is 1.0)
    """
    transaction = {'sender': sender, 'recipient': recipient, 'amount': amount}
    open_transaction.append(transaction)


def mine_block():
    pass


def get_transaction_value():
    """ Returns the input value from the user (new transaction amount) as a float. """
    tx_recipient = input('Enter the recipient of the transaction: ')
    tx_amount =  float(input('Your transaction amount please: '))
    return tx_recipient, tx_amount


def get_user_choice():
    user_input = input("Your choice: ")
    return user_input


def print_blockchain_elements():
    # Output Blockchain list to the console
    for block in blockchain:
        print("Outputting Block")
        print(block)
    else:
        print('-' * 20)


def verify_chain():
    # block_index = 0
    is_valid = True
    for block_index in range(len(blockchain)):
        if block_index == 0:
            continue
        elif blockchain[block_index][0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False

    # for block in blockchain:
    #     if block_index == 0:
    #         block_index += 1
    #         continue
    #     elif block[0] == blockchain[block_index - 1]:
    #         print("block[0] value: " + str(block[0]))
    #         print("previous block value : " + str(blockchain[block_index - 1]))
    #         is_valid = True
    #     else:
    #         print("block[0] value: " + str(block[0]))
    #         print("previous block value : " + str(blockchain[block_index - 1]))
    #         is_valid = False
    #         break
    #     block_index += 1
    return is_valid


    # Print the value
print(blockchain)

waiting_for_input = True

while waiting_for_input:
    print("Please choose")
    print("1. Add a new transaction value")
    print("2. Output the blockchain blocks")
    print('h: Manipulate the chain')
    print("q. Quit")
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        #Add the transaction to the blockchain
        add_transaction(recipient, amount=amount)
        print(open_transaction)
    elif user_choice == '2':
        print_blockchain_elements()
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print("Input was invalid. Please pick a value from the list!")
    if not verify_chain():
        print_blockchain_elements()
        print("Invalid Blockchain!!")
        break
else:
    print("User left!")

print("Done!")
