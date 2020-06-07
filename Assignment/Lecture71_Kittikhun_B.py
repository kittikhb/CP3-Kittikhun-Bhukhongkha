menuList = []
priceList = []

def showBill():
    totalPrice = 0
    print("My food".center(20,"-"))
    for number in range(len(menuList)):
        print(menuList[number],priceList[number])
        totalPrice += int(priceList[number])
        totalPriceVat = totalPrice+ totalPrice * 1.07
    print("Before Vat:",totalPrice, "THB")
    print("Vat included:",totalPriceVat,"THB")

while True:
  menuName = input("Plese Enter Menu :")
  if(menuName.lower() == "exit"):
    break
  else:
      priceName = input("Please Enter Price :")
      menuList.append(menuName)
      priceList.append(priceName)
print(menuList,priceList)
showBill()

