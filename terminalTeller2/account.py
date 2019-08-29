#!/usr/bin/env python3

import json
import os


DIR = os.path.dirname(__file__)
DATAFILENAME = "data.json"  # use your tteller filename
DATAPATH = os.path.join(DIR, DATAFILENAME)

class Account:
    data_path = DATAPATH
    data = {}

    def __init__(self, first_name="", last_name="", account_num="", pin="", balance=0):
        self.account_num = account_num
        self.pin = pin
        self.balance = balance
        self.first_name = first_name
        self.last_name = last_name

    def validate(self):
        with open(self.data_path, 'r') as file_object:
            data = json.load(file_object)
            if self.account_num in data:
                if data[self.account_num]["PIN"] == self.pin:
                    return True
            return False

    def new_account(self,account_number, first_name, last_name, pin):
        
        self.data[account_number] = {}
        self.data[account_number]["first Name"] = first_name
        self.data[account_number]["Last Name"] = last_name
        self.data[account_number]["PIN"] = pin
        self.data[account_number]["balance"] = 0


    def load(self, account_num):
        with open(self.data_path, 'r') as file_object:
            data = json.load(file_object)
            data[self.account_num]["Last Name"]
            data[self.account_num]["first Name"] 
            data[self.account_num]["balance"]
            data[self.account_num]["PIN"]

            # my_data = data[self.account_num]
            # self.balance = my_data['balance']
        # load the account with this object's self.account_num
        # Sample CONTROLLER code
        # user = Account(account_num="0000000001", pin="1234")
        # if user.validate():
        #     user.load()
        # else:
        #     raise AuthenticationError



    def save(self):
        with open(self.data_path, 'w') as json_file:
            json.dump(self.data, json_file, indent=2)

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            pass

# Justin = Account(account_num= '1814', pin='1234',balance = 900)
# Justin.withdraw(50)
# print(Justin.balance)
# # print(Justin.validate('3l850', '1111'))
# Justin.load()
# print(Justin.balance)

# steph = Account(account_num='4862', pin='1111',)
# steph.load()
# print(steph.balance)

