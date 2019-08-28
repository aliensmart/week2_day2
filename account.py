import json
import os


DIR = os.path.dirname(__file__)
DATAFILENAME = "accounts.json"  # use your tteller filename
DATAPATH = os.path.join(DIR, DATAFILENAME)

class Account:
    data_path = DATAPATH

    def __init__(self, account_num="", pin="", balance=""):
        self.account_num = account_num
        self.pin = pin
        self.balance = balance

    def validate(self):
        # return True or False if the account_num and pin is in the datafile
        pass

    def load(self):
        pass
        # load the account with this object's self.account_num
        # Sample CONTROLLER code
        # user = Account(account_num="0000000001", pin="1234")
        # if user.validate():
        #     user.load()
        # else:
        #     raise AuthenticationError

    def save(self):
        pass

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            pass