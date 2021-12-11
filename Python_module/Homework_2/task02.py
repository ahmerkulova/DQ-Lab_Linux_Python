class Item:
    item_list = []

    def __init__(self, category, title, price):
        self.category = category
        self.title = title
        self.price = price
        self.item_list.append(price)

    def get_info(self):
        print(f'Category: {self.category}, Title: {self.title}, Price: {self.price}')

    @staticmethod
    def avg_price():
        print(f'The average price of all items is {round(sum(Item.item_list) / len(Item.item_list), 2)}')


class Tablet(Item):

    def __init__(self, category, title, price, display):
        super().__init__(category, title, price)
        self.display = display

    def get_info(self):
        print(f'Category: {self.category}, Title: {self.title}, Price: {self.price}, Display: {self.display} inches')


iphone = Item('Mobile phones', 'iPhone X', 1159)
ipad = Tablet('Tablets', 'iPad pro', 1899, 11)
ipad_mini = Tablet('Tablets', 'iPad mini', 999, 8)

iphone.get_info()
ipad.get_info()
ipad_mini.get_info()
Item.avg_price()
