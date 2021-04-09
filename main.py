import pyautogui
from PIL import Image, ImageGrab
from time import sleep


def hit():
    pass


def isCollide(data):
    for i in range(290, 346):
        for j in range(600, 667):
            if data[i, j] < 100:
                pyautogui.press('up')
                return True

    for i in range(290, 366):
        for j in range(450, 520):
            if data[i, j] < 100:
                pyautogui.press("down")
                return True

    return False


def draw():
    for i in range(290, 366):
        for j in range(600, 667):
            data[i, j] = 0


def takeScreenshot():
    image = ImageGrab.grab().convert("L")
    return image


if __name__ == "__main__":
    print('in 3 seconds')
    sleep(3)
    pyautogui.press('up')
    while True:
        image = takeScreenshot()
        data = image.load()
        isCollide(data)
"""
        draw()
        # rectangele for bird
        for i in range(290, 366):
            for j in range(450, 520):
                data[i, j] = 0

        image.show()
        break

"""
