# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import math as m
from math import ceil, floor
import random

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def calculate_explosion(): #1_Day1
    weight = input("Enter your weight: ")
    cargo_weight = input("Enter your cargo_weight: ")
    max_weight = input("Enter your max weight: ")
    chance_of_explosion = str(5 * float(cargo_weight) / ( float(max_weight) - float(weight) ))
    # print("A roket with " + weight + " kg weight carrying "
    #       + cargo_weight + " kg cargo has chance of explosion equal to "
    #       + chance_of_explosion + " % if its maximum weight is "
    #       + max_weight + " kg")

    print("A roket with {} kg weight carrying  {} kg cargo has chance of explosion equal to {} % if its maximum weight is  {} kg".format(weight, cargo_weight, chance_of_explosion, max_weight))

def calculate_explosion2(): #2_Day1
    cargo_weights = [4000,9000]
    cargo_weight = input("Enter your cargo_weight: ")
    weight = input("Enter your weight: ")
    max_weight = input("Enter your max weight: ")
    sum_cargo_weight = sum(cargo_weights) + float(cargo_weight)
    chance_of_explosion = str(5 * sum_cargo_weight / (float(max_weight) - float(weight)))

    print("A roket with " + weight + " kg weight carrying "
          + cargo_weight + " kg cargo has chance of explosion equal to "
          + chance_of_explosion + " % if its maximum weight is "
          + max_weight + " kg")

def add(x,y):
    print("x is {} and y is {}".format(x,y))
    print("x is {} and y is {}".format(x,y)[::-1])
    return x + y

def swap(x,y):
    return y,x

def swap_xy(x, y):
    print("x is {} and y is {}".format(x, y))
    x, y = swap(x, y)
    print("x is {} and y is {}".format(x, y))

def test(): # global
    x = 200
    print(x)

def create_adder(x):
    def adder(y):
        return x + y
    return adder

def create_double():
    def double(x):
        return x*2
    return double


def higher_order():
    add_10 = create_adder(10)
    print(list(map(add_10,[1,2,3])))
    print(list(map(max, [1, 2, 3],[4,2,1])))
    print(list(filter(lambda x : x > 5, [1, 8, 3, 6, 7])))

def list_comprehension():
    add_10 = create_adder(10)
    print([add_10(i) for i in [1,2,3]])
    print([x for x in [3,8,4,1,6,9] if x > 5])
    print([x**2 for x in [3,8,4,1,6,9] if x > 5])
    print({x for x in 'abcdeadebcd' if x not in 'abc'})
    print({x**2 for x in range(5)})

def test_math():
    print(ceil(3.7))
    print(floor(3.7))
    print(m.sqrt(3.7))
    print(m.floor(3.7))
    print(dir(m))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    # calculate_explosion()

    double = create_double()
    print(double(10))

    # calculate_explosion2()
    # add(y=6, x=5)
    # swap_xy(1, 2)

    # x = 300
    # print(x)
    # test()
    # print(x)

    # add_10 = create_adder(10)
    # print(add_10(3))

    # higher_order()

    # print((lambda x: x > 2)(3))
    # print((lambda x,y: x**2 + y**2)(2,3))  # =>  13

    # list_comprehension()

    # test_math()

    # print(random.randint(1, 100))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
