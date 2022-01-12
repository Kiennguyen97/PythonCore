from hashlib import new


class Item:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


if __name__ == '__main__':
    food1 = Item('food', 12000)
    print(food1.name)