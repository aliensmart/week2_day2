#!/usr/bin/env python3

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
class Student(Person):
    def __init__(self, first_name, last_name, gpa, classes = []):
        super().__init__(first_name, last_name)
        self.gpa = gpa
        self.classes = classes
    
    def update_gpa(self, gpa):
        self.gpa = gpa


class Teacher(Person):
    def __init__(self, first_name, last_name, tenure, subject):
        super().__init__(first_name, last_name)
        self.tenure = tenure
        self.subject = subject
    
    def add_students(self, students):
        self.students = students 

class Food:
    def __init__(self, name, healthy, price):
        self.name = name
        self.healthy = healthy
        self.price = price

class ShoppingList:
    def __init__(self, shopping_list=[]):
        self.shopping_list = shopping_list

    def add_to_list(self, name, healthy, price):
        food = Food(name, healthy, price)
        self.shopping_list.append(food)

    def view_list(self):
        total = 0
        for item in self.shopping_list:
            print(item.name, item.price)
            total += item.price
        print(total)

    def healthy(self):
        healthy = 0
        non_healthy = 0
        

        for item in self.shopping_list:
            if item.healthy == True:
                healthy +=1
            else:
                non_healthy +=1

        total = healthy - non_healthy
        if total < 0:
            print("you are not eating healthy bro, be careful")
        elif total == 0:
            print("broooooooooo please what are you eating")
        else:
            print("bro you are my friend")
            

# justin = Student('Justin', 'Sarraga', 4.0, ['web development'])
# print(justin.first_name)
# print(justin.gpa)
# justin.update_gpa(2.3)
# print(justin.gpa)

apple = Food('apple',True,1.0)
# print(apple.name, apple.healthy, apple.price)
food_list = ShoppingList()
# print(food_list.shopping_list)
food_list.add_to_list('apple', True, 1.0)
food_list.add_to_list('pinapple', False, 2.0)
food_list.add_to_list('banana', False, 3.0)
food_list.add_to_list('carotte', False, 4.0)
# print(food_list.shopping_list)
food_list.view_list()
food_list.healthy()