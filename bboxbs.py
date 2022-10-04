import pyautogui
pyautogui.PAUSE = 5
pyautogui.FAILSAFE=True


mouseX,mouseY = pyautogui.position()
print(mouseX,mouseY)

