from PIL import Image
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
keyboard = KeyboardController()
mouse = MouseController()
import pyautogui
import pytesseract
import time
import csv
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'


Chips = pyautogui.screenshot('Chips.png', region=(1720,50, 115, 50))
print(pytesseract.image_to_string(Chips))


"""
input()
data = [row for row in csv.reader(open("BJValues.csv"))]
print(data[7][5]) # Y, X

input()
"""


"""
input()
time.sleep(3)
print("start")
keyboard.press('d')
time.sleep(3)
keyboard.release('d')
print("Done")
input()
"""


"""
input()
print("5 seconds")
time.sleep(5)
print("start")
for i in range(1):
    keyboard.press('d')
    time.sleep(0.01)
print("stop")
input()
my_str = "You have a 12."

print(int(''.join(filter(str.isdigit, my_str))))
"""


"""
#region=(0,0, 300, 400)
img = pyautogui.screenshot('image.png', region=(970,190, 100, 100))
text = pytesseract.image_to_string(img)
print(text)
input()
"""


input("press any buton to start shit show")
time.sleep(5)
x = 1
ChipsCount = 54
print("attempt start")
while x == 1:
    mouse.release(Button.right)
    DealerValue = 23
    PlayerValue = 23
    image1 = pyautogui.screenshot('PlaceBetImage.png', region=(115,60, 150, 35))
    text1 = pytesseract.image_to_string(image1)
    time.sleep(1)
    if text1 == "Place your bet.":
        ChipsName = "Chips" + str(ChipsCount) + ".png"
        ChipsCount += 1
        pyautogui.screenshot(ChipsName, region=(1720,50, 115, 50))
        print("Play")
        keyboard.press('h')
        time.sleep(1)
        keyboard.release('h')
        #Checks what the dealer has
        time.sleep(15)
        KeepGoing = 0
        while (DealerValue > 22) and (KeepGoing < 4):
            try:
                mouse.press(Button.left)
                time.sleep(5)
                image2 = pyautogui.screenshot('image2.png', region=(115,60, 185, 35))
                print("screenshot taken")
                time.sleep(1)
                mouse.release(Button.left)
                print("d released")
                text2 = pytesseract.image_to_string(image2)
                DealerValue = int(''.join(filter(str.isdigit, text2)))
            except:
                print("Fail to find dealer value, retrying")
                KeepGoing += 1
        print("Dealer has", DealerValue)
        KeepGoing = 0
        PlayerValue = 23
        while KeepGoing < 4:
            KeepGoing = 0
            print("now staying on player cards")
            mouse.press(Button.right)
            while (PlayerValue > 22) and (KeepGoing < 4):
                try:
                    time.sleep(3)
                    image3 = pyautogui.screenshot('image3.png', region=(115,60, 210, 35))
                    print("screenshot taken")
                    text3 = pytesseract.image_to_string(image3)
                    PlayerValue = int(''.join(filter(str.isdigit, text3)))
                except:
                    print("Fail to find player value, retrying")
                    KeepGoing += 1
            print("Player", PlayerValue)


            print("reading csv")
            data = [row for row in csv.reader(open("BJValues.csv"))]
            WhatDo = " "
            try:
                WhatDo = data[(PlayerValue - 1)][(DealerValue - 1)]
            except:
                print("failed to find value")
            PlayerValue = 23
            print("Now going to", WhatDo)
            if WhatDo == "H":
                keyboard.press('h')
                time.sleep(1)
                keyboard.release('h')
            elif WhatDo == "Dh":
                keyboard.press('y')
                time.sleep(1)
                keyboard.release('y')
                time.sleep(1)
                keyboard.press('h')
                time.sleep(1)
                keyboard.release('h')
            elif WhatDo == "S":
                keyboard.press('s')
                time.sleep(1)
                keyboard.release('s')
                KeepGoing = 4
                continue
            else:
                KeepGoing = 4
                continue
            
    else:
        print("fail to start")
        

