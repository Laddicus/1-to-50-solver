import pyautogui
import threading
REGION = (2535, 945, 370, 370)
num = 1
xPos = list()
yPos = list()

def search():
    try:
        global num
        # pyautogui.locateOnScreen('./sc/1.png')
        # print("test")
        targetx, targety = pyautogui.center(pyautogui.locateOnScreen('./sc/%d.png' % num, grayscale = True, region=REGION))
        xPos.append(targetx)
        yPos.append(targety)
        # if num >25:
        #     print(num)
        num += 1
    except:
        print("Number not found")
        exit()
def sFZ():
    while num<=50:
        search()
def clickTE(i):
    try:
        if len(xPos) > i:
            pyautogui.click(xPos[i], yPos[i])
        else:
            pyautogui.sleep(0.001)
            clickTE(i)
    except Exception as e:
        print("Click not done")
        print(e)
        exit()
def cFZ():
    for i in range(25, 50):
        clickTE(i)

t1 = threading.Thread(target=sFZ)
t2 = threading.Thread(target=cFZ)

while num<=25:
    search()
for i in range(25):
    pyautogui.click(xPos[i], yPos[i])

pyautogui.moveTo(10,10)

t1.start()
t2.start()

t1.join()
t2.join()