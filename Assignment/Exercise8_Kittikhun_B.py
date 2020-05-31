userName = input("user name:")
password = input("password:")
if userName == "kittikhun" and password == "biggy":
    print("Welcome to our shop",userName,"!")
    print("----------------------")
    print("Please select items")
    print("1.Giant Sword = 100 zenny")
    print("2.Paladin Shield = 150 zenny")
    print("3.Orge Helmet = 200 zenny")
    giantSword = 100
    paladinShield = 150
    Orgehelmet = 200
    selectItem = input("SelectItem(1-3):")
    if selectItem == "1":
        selectQuantity1 = int(input("How many?:"))
        print("Giant Sword",selectQuantity1,"ea=",giantSword*selectQuantity1,"Zenny")
    elif selectItem == "2":
        selectQuantity2 = int(input("How many?:"))
        print("Paladin Shield",selectQuantity2,"ea=",paladinShield*selectQuantity2,"Zenny")
    elif selectItem == "3":
        selectQuantity3 = int(input("How many?:"))
        print("Orge Helmet",selectQuantity3,"ea=",Orgehelmet*selectQuantity3,"Zenny")
    print("Thank you for shopping!")

else:
    print("Access Denied")