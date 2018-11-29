from functools import reduce
import hashlib as hl
import json

MINING_REWARD = 10

genesis_block = {
    'previous_hash': '',
    'index': 0,
    'transaction': []
}
blockchain = [genesis_block]
open_transactions = []
owner = 'Sri'
participants = {'Sri'}

def hash_block(block):
    """ Hashes a block and returns a string representation of it.

    Arguments:
        :block: The block that should be hashed
    """
    return hl.sha256(json.dumps(block).encode()).hexdigest()
    # return '-'.join([str(block[key]) for key in block])



def valid_proof(transactions, last_hash, proof):
    guess = (str(transactions) + str(last_hash) + str(proof)).encode()
    guess_hash = hl.sha256(guess).hexdigest()
    print(guess_hash)
    return guess_hash[0:2] == 'g6'


def proof_of_work():
    last_block = blockchain[-1]
    last_hash = hash_block(last_block)
    proof = 0
    while valid_proof(open_transactions, last_hash, proof):
        proof += 1
    return proof


def get_balances(participant):
    tx_sender = [[tx['amount'] for tx in block['transaction']
                  if tx['sender'] == participant] for block in blockchain]
    open_tx_sender = [tx['amount']
                      for tx in open_transaction if tx['sender'] == participant]
    tx_sender.append(open_tx_sender)
    amount_sent = reduce(
        lambda tx_sum, tx_amt: tx_sum + sum(tx_amt) if len(tx_amt) > 0 else tx_sum + 0, tx_sender, 0)
    # amount_sent = 0
    # for tx in tx_sender:
    #     if len(tx) > 0:
    #         amount_sent += tx[0]
    tx_recipient = [[tx['amount'] for tx in block['transaction']
                     if tx['recipient'] == participant] for block in blockchain]
    amount_received = reduce(
        lambda tx_bal, tx_amt: tx_bal + sum(tx_amt) if len(tx_amt) > 0 else tx_bal + 0, tx_recipient, 0)
    # amount_received = 0
    # for tx in tx_recipient:
    #     if len(tx) > 0:
    #         amount_received += tx[0]
    return amount_received - amount_sent


def get_last_blockchain_value():
    """ Returns the last value of the current blockchain. """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def verify_transaction(transaction):
    sender_balance = get_balances(transaction['sender'])
    return sender_balance >= transaction['amount']


def add_transaction(recipient, sender=owner, amount=1.0):
    """ Appends a new value to the blockchain as well as the last trasaction value to it.

    Arguments:
        :sender: The sender of the coins
        :sender: The recipient of the coins 
        :amount: The amoutn of coins sent with the transaction. (default is 1.0)
    """
    transaction = {
        'sender': sender,
        'recipient': recipient,
        'amount': amount
    }
    if verify_transaction(transaction):
        open_transaction.append(transaction)
        participants.add(sender)
        participants.add(recipient)
        return True
    return False


def mine_block():
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    print(hashed_block)
    reward_transaction = {
        'sender': 'MINING',
        'recipient': owner,
        'amount': MINING_REWARD
    }
    copied_transactions = open_transactions[:]
    copied_transactions.append(reward_transaction)
    block = {
        'previous_hash': hashed_block,
        'index': len(blockchain),
        'transaction': copied_transactions
    }
    blockchain.append(block)
    return True


def get_transaction_value():
    """ Returns the input value from the user (new transaction amount) as a float. """
    tx_recipient = input('Enter the recipient of the transaction: ')
    tx_amount = float(input('Your transaction amount please: '))
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
    """ Verify the current blockchain and return True if it's valid, False otherwise"""
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        if block['previous_hash'] != hash_block(blockchain[index - 1]):
            return False

    return True


def verify_transactions():
    return all([verify_transaction(tx) for tx in open_transactions])
    # is_valid = True
    # for tx in open_transactions:
    #     if verify_transaction(tx):
    #         is_valid = True
    #     else:
    #         is_valid = False
    # return is_valid


waiting_for_input = True

while waiting_for_input:
    print("Please choose")
    print("1. Add a new transaction value")
    print("2. Mine a new block")
    print("3. Output the blockchain blocks")
    print("4. Output Participants")
    print("5. Check transaction validity")
    print('h: Manipulate the chain')
    print("q. Quit")
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        # Add the transaction to the blockchain
        if add_transaction(recipient, amount=amount):
            print("Added transaction! ")
        else:
            print("Transaction Failed")
        print(open_transaction)
    elif user_choice == '2':
        if mine_block():
            open_transaction = []
    elif user_choice == '3':
        print_blockchain_elements()
    elif user_choice == '4':
        print(participants)
    elif user_choice == '5':
        if verify_transactions:
            print("All transactions are valid!")
        else:
            print("There are invalid tranactions")
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = {
                'previous_hash': '',
                'index': 0,
                'transaction': [{'sender': 'dammale', 'recipient': 'gummale', 'amount': '100'}]
            }
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print("Input was invalid. Please pick a value from the list!")
    if not verify_chain():
        print_blockchain_elements()
        print("Invalid Blockchain!!")
        break
    print('The Balance available for {} is: {:6.6f}'.format(
        'Sri', get_balances('Sri')))
else:
    print("User left!")

print("Done!")
