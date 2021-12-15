class Item:
    item_list = []

    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        __class__.item_list.append(price)

    def avg_price(__class__):
        return round(sum(__class__.item_list) / len(__class__.item_list), 2)


class Tablet(Item):
    item_list = []

    def __init__(self, brand, model, price, display):
        super().__init__(brand, model, price)
        self.display = display
        __class__.item_list.append(price)

    def __str__(self):
        return f'Brand: {self.brand}, Model: {self.model}, Price: {self.price}, Display: {self.display} inches'


class Fridge(Item):
    item_list = []

    def __init__(self, category, model, price, capacity):
        super().__init__(category, model, price)
        self.capacity = capacity
        __class__.item_list.append(price)

    def __str__(self):
        return f'Brand: {self.brand}, Model: {self.model}, Price: {self.price}, Capacity: {self.capacity} liters'


ipad = Tablet('Apple', 'iPad pro', 1899, 11)
ipad_mini = Tablet('Apple', 'iPad mini', 999, 8)
ariston = Fridge('Hotpoint Ariston', 'HS 3200', 1899, 350)
smeg = Fridge('Smeg', 'FAB28LPB5', 2200, 350)

print(ipad.__str__())
print(ipad_mini.__str__())
print(ariston.__str__())
print(smeg.__str__())

print(Tablet.avg_price(Tablet))
print(Fridge.avg_price(Fridge))
print(Item.avg_price(Item))

# print(ipad.price is ariston.price)
# print(ipad.display is ipad_mini.display)
# print(smeg.capacity is ariston.capacity)

