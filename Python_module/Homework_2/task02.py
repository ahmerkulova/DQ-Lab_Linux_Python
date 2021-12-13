class Item:
    item_list = []

    def __init__(self, category, title, price):
        self.category = category
        self.title = title
        self.price = price
        self.item_list.append(price)

    @staticmethod
    def avg_price():
        print(f'The average price of all items is {round(sum(Item.item_list) / len(Item.item_list), 2)}')


class Tablet(Item):

    def __init__(self, category, title, price, display):
        super().__init__(category, title, price)
        self.display = display

    def print_info(self):
        print(f'Category: {self.category}, Title: {self.title}, Price: {self.price}, Display: {self.display} inches')


class Fridge(Item):

    def __init__(self, category, title, price, capacity):
        super().__init__(category, title, price)
        self.capacity = capacity

    def print_info(self):
        print(f'Category: {self.category}, Title: {self.title}, Price: {self.price}, Capacity: {self.capacity} liters')


ipad = Tablet('Tablets', 'iPad pro', 1899, 11)
ipad_mini = Tablet('Tablets', 'iPad mini', 999, 8)
ariston = Fridge('Dual-chamber fridges', 'Hotpoint Ariston', 1500, 350)
smeg = Fridge('Single-chamber fridges', 'Smeg', 2100, 350)

ipad.print_info()
ipad_mini.print_info()
ariston.print_info()
smeg.print_info()
Item.avg_price()

print(smeg is ariston)
print(smeg.capacity is ariston.capacity)
