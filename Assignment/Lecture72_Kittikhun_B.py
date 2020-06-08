menuList = []

def showBill():
    totalPrice = 0
    print("My food".center(20,"-"))
    for number in range(len(menuList)):
        print(menuList[number])
        totalPrice += int(menuList[number][1])
        totalPriceVat = totalPrice + (totalPrice * 7/100)
    print("Before Vat:",totalPrice, "THB")
    print("Vat included:",totalPriceVat,"THB")

while True:
  menuName = input("Plese Enter Menu :")
  if(menuName.lower() == "exit"):
    break
  else:
      priceName = input("Please Enter Price :")
      menuList.append([menuName,priceName])
print(menuList)
showBill()

