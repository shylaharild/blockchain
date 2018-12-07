from collections import OrderedDict

from utility.printable import Printable

class Transaction(Printable):
    def __init__(self, sender, recipient, signature, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.signature = signature
    
    # def __repr__(self):
    #     return str(self.__dict__)
        # return '[Sender: {}, Recipient: {}, Amount: {}]'.format(self.sender, self.recipient, self.amount)

    def to_ordered_dict(self):
        return OrderedDict([('sender', self.sender), ('recipient', self.recipient), ('signature', self.signature), ('amount', self.amount)])