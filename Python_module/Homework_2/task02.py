class Item:
    item_list = []

    def __init__(self, category, title, price):
        self.category = category
        self.title = title
        self.price = price
        self.item_list.append(price)

    def avg_price():
        return round(sum(Item.item_list) / len(Item.item_list), 2)


class Tablet(Item):

    def __init__(self, category, title, price, display):
        super().__init__(category, title, price)
        self.display = display

    def __str__(self):
        return f'Category: {self.category}, Title: {self.title}, Price: {self.price}, Display: {self.display} inches'


class Fridge(Item):

    def __init__(self, category, title, price, capacity):
        super().__init__(category, title, price)
        self.capacity = capacity

    def __str__(self):
        return f'Category: {self.category}, Title: {self.title}, Price: {self.price}, Capacity: {self.capacity} liters'


ipad = Tablet('Tablets', 'iPad pro', 1899, 11)
ipad_mini = Tablet('Tablets', 'iPad mini', 999, 8)
ariston = Fridge('Dual-chamber fridges', 'Hotpoint Ariston', 1899, 350)
smeg = Fridge('Single-chamber fridges', 'Smeg', 2100, 350)

print(ipad.__str__())
print(ipad_mini.__str__())
print(ariston.__str__())
print(smeg.__str__())
print(f'The average price of all items is {Item.avg_price()}')

print(ipad.price is ariston.price)
print(ipad.display is ipad_mini.display)
print(smeg.capacity is ariston.capacity)
