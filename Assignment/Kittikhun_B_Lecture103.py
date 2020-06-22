class Customer:
    name = ""
    lastName=""
    age = 0

    def addCart(self):
        print("Added to",self.name,self.lastName,"'s cart")

customer1 = Customer()
customer1.name = "Kittikhun"
customer1.lastName = "Bhukhongkha"

customer2 = Customer()
customer2.name = "Anrita"
customer2.lastName = "Kijsathan"

customer3 = Customer()
customer3.name = "Khemnipat"
customer3.lastName = "Bhukhongkha"

customer1.addCart()
customer2.addCart()
customer3.addCart()
