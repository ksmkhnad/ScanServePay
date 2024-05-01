class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class MenuBuilder:
    def __init__(self):
        self.menu_items = []

    def add_item(self, name, price):
        item = MenuItem(name, price)
        self.menu_items.append(item)

    def get_menu(self):
        return self.menu_items