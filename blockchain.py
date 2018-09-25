blockchain = []


def get_last_blockchain_value():
    return blockchain[-1]


def add_value(transaction_amount, last_transaction_value=[1]):
    blockchain.append([last_transaction_value, transaction_amount])


def get_input_value():
    return float(input('Your transaction amount please: '))

tx_amount = get_input_value()
add_value(tx_amount)

tx_amount = get_input_value()
add_value(last_transaction_value=get_last_blockchain_value(),
          transaction_amount=tx_amount)

tx_amount = get_input_value()
add_value(tx_amount, get_last_blockchain_value())

print(blockchain)
