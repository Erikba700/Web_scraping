import time
import pyautogui as py
import keyboard


def get_xy():
    for i in range(0, 4):
        if i == 0:
            global greenx
            global greeny
            global green_rgb
            color_center = py.locateCenterOnScreen('green.png', confidence=0.8)
            greenx = int(color_center[0])
            greeny = int(color_center[1])
            green_rgb = py.pixel(greenx, greeny)[0]
        elif i == 1:
            global bluex
            global bluey
            global blue_rgb
            color_center = py.locateCenterOnScreen('blue.png', confidence=0.8)
            bluex = int(color_center[0])
            bluey = int(color_center[1])
            blue_rgb = py.pixel(bluex, bluey)[0]
        elif i == 2:
            global yellowx
            global yellowy
            global yellow_rgb
            color_center = py.locateCenterOnScreen('yellow.png', confidence=0.8)
            yellowx = int(color_center[0])
            yellowy = int(color_center[1])
            yellow_rgb = py.pixel(yellowx, yellowy)[0]
        elif i == 3:
            global redx
            global redy
            global red_rgb
            color_center = py.locateCenterOnScreen('red.png', confidence=0.8)
            redx = int(color_center[0])
            redy = int(color_center[1])
            red_rgb = py.pixel(redx, redy)[0]



time.sleep(1)
get_xy()
print(greenx, 'a', greeny, 'a', blue_rgb)

