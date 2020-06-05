def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        print("Done!")
        return True
    else:
        print("Please input correct username and password")
        return login()

def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")

def menuSelect():
    userSelected = int(input(">>"))
    if userSelected == 1:
        print(vatCalculator(int(input("Price:"))))
    elif userSelected == 2:
        print(priceCalculator())
    else:
        print("Please select again")
        return menuSelect()

def vatCalculator(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result

def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculator(price1 + price2)

login()
showMenu()
menuSelect()

