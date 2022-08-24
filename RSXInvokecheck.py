import pyautogui
import time
import cv2 as cv
import pytesseract

def RSXINVOKEFUNC():

    #Invoke RSX
    print("invoking RSX")
    pyautogui.hotkey('alt', 'r')

    time.sleep(2)

    #Save Screenshot
    print("Saving screenshot")
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r'C:\Users\thomalam\Documents\PROGRAMMING\PYTHON\RSX OCR detection\RSXScreenshot.png')

    time.sleep(1)

    imageread = cv.imread('RSXScreenshot.png')

    crop_img = imageread[200:350, 0:1500]

    cv.imshow("cropped",crop_img)

    toprow = pytesseract.image_to_string(crop_img)
    print(toprow)
    print(type(toprow))

    expected = 'Home'

    if toprow!=expected:
        RSXINVOKE = True
        print("RSX INVOKE IS Success!")
    else:
        RSXINVOKE = False
        print("RSX INVOKE IS FAILED!")

    cv.waitKey(0)
    return RSXINVOKE

RSXINVOKEFUNC()

