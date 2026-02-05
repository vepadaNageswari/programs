# save and show of inventory using class

class Inventory:
    def __init__(self, file_name):
        self.file_name = file_name
        self.items = []

    def save_item(self):
        item_id = input("Enter item id: ")
        description = input("Enter description: ")
        unit_price = float(input("Enter unit price: "))
        stock_qty = int(input("Enter stock quantity: "))

        item = [item_id, description, unit_price, stock_qty]
        self.items.append(item)

        with open(self.file_name, "w") as inventory_file:
            inventory_file.write(str(self.items))

    def show_all_items(self):
        with open(self.file_name, "r") as inventory_file:
            self.items = eval(inventory_file.read())
        if not self.items:
            print("No inventory items found!")
            return
        print("Item ID\tDescription\tUnit Price\tStock Qty")
        for item in self.items:
            print(item[0], "\t", item[1], "\t", item[2], "\t\t", item[3])


file_name = "inventory.dat"
inventory = Inventory(file_name)
inventory.save_item()
inventory.show_all_items()