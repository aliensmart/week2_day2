#!/usr/bin/env python3
def welcome_menu():
    print()
    print("Welcom to Terminal Teller")
    print("1) create account")
    print("2) log in")
    print("3) quit")

# def new_account():
#     print()
#     input("First Name: ")
#     input("Last Name: ")
#     input("PIN: ")
#     input("Confirm Pin")
#     print(f"account created, your account number is")
def get_f_name():
    return input("Firt Name: ")

def get_l_name():
    return input("Last Name: ")

def get_pin():
    return input("PIN: ")

def choice():
    print()
    print("your choice: ")
    return input()

def account_number():
    return input("Account Number: ")

# def login():
#     print()
#     input("Account number: ")
#     input("Pin: ")

def main_menu(account_number, first_name, last_name):
    print()
    print(f"hello  {first_name} {last_name} ({account_number})")
    print("1) check balance")
    print("2) withdraw fund")
    print("3) deposit funds")
    print("4) sign out")

def withdraw():
    print()
    return input("how much to withdraw : ")

def deposit():
    print()
    return input("How much to deposit: ")

def insuf():
    print()
    print("Insuffisant fund")

def pin_confirm(pin):
    pin2 = input("confirm PIN:  ")
    return pin2
def new_account(account_number):
    print(f"account created, your account number is {account_number}")

if __name__ == "__main__":
    welcome_menu()























