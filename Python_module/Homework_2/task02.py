class Item:
    item_list = []

    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        __class__.item_list.append(price)

    @classmethod
    def avg_price(cls):
        return round(sum(cls.item_list) / len(cls.item_list), 2)


class Tablet(Item):
    item_list = []

    def __init__(self, brand, model, price, display):
        super().__init__(brand, model, price)
        self.display = display
        __class__.item_list.append(price)

    def __str__(self):
        return f'Brand: {self.brand}, Model: {self.model}, Price: {self.price}, Display: {self.display} inches'

    def __eq__(self, other):
        if not isinstance(other, Tablet):
            return False
        return self.display == other.display


class Fridge(Item):
    item_list = []

    def __init__(self, category, model, price, capacity):
        super().__init__(category, model, price)
        self.capacity = capacity
        __class__.item_list.append(price)

    def __str__(self):
        return f'Brand: {self.brand}, Model: {self.model}, Price: {self.price}, Capacity: {self.capacity} liters'

    def __eq__(self, other):
        if not isinstance(other, Fridge):
            return False
        return self.capacity == other.capacity

ipad = Tablet('Apple', 'iPad pro', 1899, 11)
ipad_mini = Tablet('Apple', 'iPad mini', 999, 8)
ariston = Fridge('Hotpoint Ariston', 'HS 3200', 1899, 350)
smeg = Fridge('Smeg', 'FAB28LPB5', 2200, 350)

print(ipad.__str__())
print(ipad_mini.__str__())
print(ariston.__str__())
print(smeg.__str__())

print(Item.avg_price())
print(Tablet.avg_price())
print(Fridge.avg_price())

print(ipad == ipad_mini)
print(ariston == smeg)
print(ariston == ipad)