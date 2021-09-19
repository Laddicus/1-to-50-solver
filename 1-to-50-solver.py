import pyautogui
import threading

# region of the screen that the number grid resides in
REGION = (2535, 945, 370, 370)
# used to keep track of the locations of each number
position = list()
for x in range(50):
    position.append((0,0))

# function for searching the screen for numbers
def search(number):
    try:
        position[number-1] = (pyautogui.center(pyautogui.locateOnScreen('./sc/%d.png' % number, grayscale = True, region=REGION)))
    except:
        print("Number not found")
        exit()
def sFZ():
    while filled(position)<50:
        search(filled(position)+1)
def clickTE(i):
    try:
        if filled(position) > i:
            pyautogui.click(position[i][0], position[i][1])
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

def filled(list):
    for x, y in enumerate(list):
            if y[0] == 0:
                print(f"{x} : {y}")
                return x
    return len(list)

t1 = threading.Thread(target=sFZ)
t2 = threading.Thread(target=cFZ)


while filled(position)<25:
    search(filled(position)+1)
for i in range(25):
    pyautogui.click(position[i][0], position[i][1])

pyautogui.moveTo(10,10)

t1.start()
t2.start()

t1.join()
t2.join()