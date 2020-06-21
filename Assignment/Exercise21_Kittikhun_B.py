from tkinter import *
import math

def leftMouseClick(event):
    bmiResult = float(textBoxWeight.get()) / math.pow(float(textBoxHight.get())/100,2)
    labelbmiResult.configure(text=bmiResult)
    if bmiResult >30:
        labelResultMeaning.configure(text="อ้วนมาก")
    elif bmiResult <18.5:
        labelResultMeaning.configure(text="ผอมเกินไป")
    elif bmiResult <= 22.9:
        labelResultMeaning.configure(text="น้ำหนักปกติ")
    elif bmiResult <=24.9:
        labelResultMeaning.configure(text="น้ำหนักเกิน")
    elif bmiResult <=29.9:
        labelResultMeaning.configure(text="อ้วน")

mainWindow = Tk()
labelHight = Label(mainWindow,text="ส่วนสูง (cm.)")
labelHight.grid(row=0,column=0)
textBoxHight = Entry(mainWindow)
textBoxHight.grid(row=0,column=1)

labelWeight = Label(mainWindow,text="น้ำหนัก (Kg.)")
labelWeight.grid(row=1,column=0)
textBoxWeight = Entry(mainWindow)
textBoxWeight.grid(row=1,column=1)

calculateButton = Button(mainWindow,text="คำนวณ")
calculateButton.grid(row=2,column=0)
calculateButton.bind("<Button-1>",leftMouseClick)

labelbmiResult = Label(mainWindow, text="ค่า BMI")
labelbmiResult.grid(row=2,column=1)

labelResultMeaning = Label(mainWindow, text="ผลลัพท์")
labelResultMeaning.grid(row=3,column=1)

mainWindow.mainloop()