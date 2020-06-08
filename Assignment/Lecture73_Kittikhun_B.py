menuList = []
systemMenu = {"ข้าวหมกไก่":30,"ข้าวมันไก่":35,"ข้าวมันไก่ผสม":40}
def showBill():
    totalPrice = 0
    print("My food".center(20,"-"))
    for number in range(len(menuList)):
        print(menuList[number][0],menuList[number][1])
        totalPrice += int(menuList[number][1])
        totalPriceVat = totalPrice + (totalPrice * 7/100)
    print("Before Vat:",totalPrice, "THB")
    print("Vat included:",totalPriceVat,"THB")

while True:
  menuName = input("Plese Enter Menu :")
  if(menuName.lower() == "exit"):
    break
  else:
      menuList.append([menuName,systemMenu[menuName]])
print(menuList)
showBill()

