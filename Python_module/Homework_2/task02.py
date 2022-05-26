# Реализуйте класс товар, в который включите свойства и методы общие для любого товара из магазина
# бытовой электроники (не менее двух свойств и методов). Реализуйте двух наследников товара, например,
# классы телевизор и холодильник, которые должны будут иметь в дополнение к наследуемым хотя бы по одному
# собственному уникальному свойству и методу.
# Пополните ассортимент своего виртуального магазина несколькими разными товарами с различными параметрами.
# Рассчитайте среднюю цену всех созданных товаров, используя главный класс. Реализуйте корректное сравнение
# двух товаров между собой по их исключительному свойству, например, два объекта-телевизора будут считаться
# равными между собой, если у них одинаковая диагональ. Сравните несколько товаров между собой.

class Item:
    price_list = []

    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        __class__.price_list.append(price)

    @classmethod
    def avg_price(cls):
        return round(sum(cls.price_list) / len(cls.price_list), 2)

    def __str__(self):
        return f'Brand: {self.brand}, Model: {self.model}, Price: {self.price}'


class Tablet(Item):
    price_list = []

    def __init__(self, brand, model, price, display):
        super().__init__(brand, model, price)
        self.display = display
        __class__.price_list.append(price)

    def __str__(self):
        return f'{super().__str__()}, Display: {self.display} inches'

    def __eq__(self, other):
        if not isinstance(other, Tablet):
            return False
        return self.display == other.display


class Fridge(Item):
    price_list = []

    def __init__(self, brand, model, price, capacity):
        super().__init__(brand, model, price)
        self.capacity = capacity
        __class__.price_list.append(price)

    def __str__(self):
        return f'{super().__str__()}, Capacity: {self.capacity} liters'

    def __eq__(self, other):
        if not isinstance(other, Fridge):
            return False
        return self.capacity == other.capacity


ipad = Tablet('Apple', 'iPad pro', 1899, 11)
ipad_mini = Tablet('Apple', 'iPad mini', 999, 8)
ariston = Fridge('Hotpoint Ariston', 'HS 3200', 1899, 350)
smeg = Fridge('Smeg', 'FAB28LPB5', 2200, 350)

print(ipad)
print(ipad_mini)
print(ariston)
print(smeg)

print(Item.avg_price())
print(Tablet.avg_price())
print(Fridge.avg_price())

print(ipad == ipad_mini)
print(ariston == smeg)
print(ariston == ipad)
