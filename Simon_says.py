import time
import pyautogui as py
import keyboard

# https://www.coolmathgames.com/0-color-memory#immersiveModal
# green: X:  343 Y:  681 RGB: ( 33, 104,  33)
# red: X:  346 Y:  989 RGB: ( 32,  32, 173)
# blue: X:  648 Y: 1006 RGB: (166,  26,  26)
# yellow: X:  653 Y:  688 RGB: (171, 164,  31)


def click(action_list):
    for each_clic in action_list:
        x, y = each_clic
        py.click(x, y)


def get_xy():
    for i in range(0, 4):
        if i == 0:
            global greenx
            global greeny
            global green_rgb
            color_center = py.locateCenterOnScreen('green.png', confidence=0.95, grayscale=False)
            greenx = int(color_center[0])
            greeny = int(color_center[1])
            green_rgb = py.pixel(greenx, greeny)[0]
            print(f"Green x{greenx}, y{greeny}")
            py.moveTo(greenx, greeny)
        elif i == 1:
            global bluex
            global bluey
            global blue_rgb
            color_center = py.locateCenterOnScreen('blue.png', confidence=0.95, grayscale=False)
            bluex = int(color_center[0])
            bluey = int(color_center[1])
            blue_rgb = py.pixel(bluex, bluey)[0]
            print("Blue")
            py.moveTo(bluex, bluey)
        elif i == 2:
            global yellowx
            global yellowy
            global yellow_rgb
            color_center = py.locateCenterOnScreen('yellow.png', confidence=0.95, grayscale=False)
            yellowx = int(color_center[0])
            yellowy = int(color_center[1])
            yellow_rgb = py.pixel(yellowx, yellowy)[0]
            print("Yellow")
            py.moveTo(yellowx, yellowy)
        elif i == 3:
            global redx
            global redy
            global red_rgb
            color_center = py.locateCenterOnScreen('red.png', confidence=0.95, grayscale=False)
            redx = int(color_center[0])
            redy = int(color_center[1])
            red_rgb = py.pixel(redx, redy)[0]
            print("Red")
            print("END")
            py.moveTo(redx, redy)


def check(prev_count):
    print("-----In check block")
    iter_count = 0
    while 1:

        if py.pixel(greenx, greeny)[0] != green_rgb:
            print("in green block")
            while py.pixel(greenx, greeny)[0] != green_rgb:
                time.sleep(0.002)
            iter_count += 1
            if iter_count >= prev_count + 1:
                stack.append((greenx, greeny))
                print("green")
                break
        if py.pixel(redx, redy)[0] != red_rgb:
            print("in Red block")
            while py.pixel(redx, redy)[0] != red_rgb:
                time.sleep(0.002)
            iter_count += 1
            if iter_count >= prev_count + 1:
                stack.append((redx, redy))
                print("red")
                break
        if py.pixel(bluex, bluey)[0] != blue_rgb:
            print("in blue block")
            while py.pixel(bluex, bluey)[0] != blue_rgb:
                time.sleep(0.002)
            iter_count += 1
            if iter_count >= prev_count + 1:
                stack.append((bluex, bluey))
                print("blue")
                break
        if py.pixel(yellowx, yellowy)[0] != yellow_rgb:
            print("in yellow block")
            while py.pixel(yellowx, yellowy)[0] != yellow_rgb:
                time.sleep(0.002)
            iter_count += 1
            if iter_count >= prev_count + 1:
                stack.append((yellowx, yellowy))
                print("yellow")
                break


stack = []

while not keyboard.is_pressed("q"):
    while keyboard.is_pressed("c"):
        get_xy()
        while True:
            check(len(stack))
            time.sleep(0.1)
            click(stack)
            time.sleep(0.05)