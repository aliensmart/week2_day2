#!/usr/bin/env python3
import view
from account import Account
import random



def run():
    view.welcome_menu()
    main_menu()

def main_menu():
    while True:
        
        selection = view.choice()
        
        if selection == "1":
            print()
            # create_account()

        elif selection == "2":
            login()

        elif selection == "3" :

            return

def login():
    account_number = view.account_number()
    pin = view.get_pin()
    the_acc = Account()
    the_acc.pin = pin
    the_acc.account_num = account_number

    if the_acc.validate() == True:
        the_acc.load(account_number)
        print(data[the_acc.account_num]["first Name"])
        # menu(the_acc)
    else:
        print("wrong pin")
        main_menu()





# def menu(the_acc):
#     print(data[])
#     while True:
#         view.main_menu(the_, first_name, last_name)
#         selection = view.choice()

#         if selection == "1":
#             print(account.get_balance(account_number))

#         elif selection == "2":
#             witdraw = float(view.withdraw())
#             account.withdraw(witdraw)
#             # money_left = model.balance(account_number)
            
#             # acc.save()
#             # if money_left < 0:
#             #     view.insuf()

#         elif selection == "3":
#             amount = float(view.deposit())
#             account.deposit(amount)

#             account.save()
#         elif selection == "4":
            
#             account.save()
#             return
        

# def create_account():
#     first_name = view.get_f_name()
#     last_name = view.get_l_name()
#     pin = view.get_pin()
#     confirm_pin = view.pin_confirm(pin)
#     if confirm_pin != pin:
#         print("wrong pin")
#         create_account()
#     else:
#         account_number = "N4321" + str(random.randint(100, 1000))
#         new_acc = Account()
#         new_acc.new_account(account_number, first_name, last_name, pin)
#         acc.save()
#         view.new_account(account_number)
#         view.welcome_menu()
#         main_menu()









if __name__ == "__main__":
    run()
