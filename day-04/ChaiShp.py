from abc import ABC,abstractmethod

class Chai:
    def __init__(self,nm,bp,qty):
        self.name=nm
        self.base_price=bp
        self.quantity_in_stock=qty

    @abstractmethod
    def calculate_price():
        pass
    def display_info():
        pass

class MasalaChai(Chai):
    def __init__(self,nm,bp,qty):
        super().__init__(nm,bp,qty)
    
    def calculate_price(self):
        self.base_price+=10
        return self.base_price

    def display_info(self):
        print("Name: ",self.name," | Price per cup: Rs.",self.calculate_price()," | Stock: ",self.quantity_in_stock)

class GingerChai(Chai):
    def __init__(self,nm,bp,qty):
        super().__init__(nm,bp,qty)
    
    def calculate_price(self):
        self.base_price+=8
        return self.base_price

    def display_info(self):
        print("Name: ",self.name," | Price per cup: Rs.",self.calculate_price()," | Stock: ",self.quantity_in_stock)


class ElaichiChai(Chai):
    def __init__(self,nm,bp,qty):
        super().__init__(nm,bp,qty)
    
    def calculate_price(self):
        self.base_price+=12
        return self.base_price

    def display_info(self):
        print("Name: ",self.name," | Price per cup: Rs.",self.calculate_price()," | Stock: ",self.quantity_in_stock)


class ChaiInventory:
    chai_li=[]

    def add_chai(self,chai_obj):
        self.chai_li.append(chai_obj)

    def show_inventory(self):
        for i in self.chai_li:
            i.display_info()
        
    def get_total_inventory_value(self):
        sum = 0
        for i in self.chai_li:
            # self.base_price = print(i.calculate_price())
            total_revenue = i.calculate_price()*i.quantity_in_stock
            sum+=total_revenue
        return sum

inventory = ChaiInventory()
chai1 = MasalaChai("Masala Chai", 20, 50)
chai2 = GingerChai("Ginger Chai", 18, 40)
chai3 = ElaichiChai("Elaichi Chai", 25, 30)

inventory.add_chai(chai1)
inventory.add_chai(chai2)
inventory.add_chai(chai3)

inventory.show_inventory()

print("Total Inventory Value: ₹",inventory.get_total_inventory_value())

