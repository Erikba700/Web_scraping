import pyautogui as py

color_center = py.locateCenterOnScreen('green.png', confidence=0.8)
greenx = color_center[0]
greeny = intcolor_center[1]
print(type(greenx), greeny)
green_rgb = py.pixel(314, 675)
print(green_rgb)
