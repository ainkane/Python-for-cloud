class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def total_cost(self):
        return self.price * self.quantity

class Inventory:
    def __init__(self):
        self.items = []
    
    def add_item(self, item):
        self.items.append(item)
    
    def remove_item(self, item_name):
        self.items = [item for item in self.items if item.name != item_name]
    
    def total_inventory_value(self):
        return sum(item.total_cost() for item in self.items)

def test_inventory_system():
    item1 = Item("Laptop", 1000, 2)
    item2 = Item("Mouse", 50, 5)
    item3 = Item("Keyboard", 80, 3)
    
    inventory = Inventory()
    inventory.add_item(item1)
    inventory.add_item(item2)
    inventory.add_item(item3)
    
    print("Total Inventory Value:", inventory.total_inventory_value())

def main():
    test_inventory_system()

if __name__ == "__main__":
    main()
