import pyautogui, time

time.sleep(1)
for i in range(50):
    pyautogui.write("AI sovori")
    time.sleep(0.1)
    pyautogui.press("enter")

