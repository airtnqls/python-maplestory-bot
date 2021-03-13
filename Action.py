import math
import pyautogui
import sys
import time
import random
import keyboard


def rand(num, mul=0.5):
    return num + random.uniform(0, num * mul)


def sleep(t=0.02, mul=0.5):
    time.sleep(rand(t, mul))


def release(key):
    keyboard.release(key)


def press(key):
    keyboard.press(key)


def button(key, t=0.02):
    press(key)
    sleep(t)
    release(key)


def skill(key):
    r = random.randint(1, 2)
    for i in range(0, r):
        button(key)
        sleep(0.08)


def buff(key):
    r = random.randint(1, 3)
    for i in range(0, r):
        button(key)
        sleep(0.08)


def idle(self):
    return


def pressMove(d):
    if d is True:
        press('left')
    else:
        press('right')


def releaseMove():
    release('left')
    release('right')


def attack():
    button('z')


def jump():
    button('x')


def jumpAttack():
    jump()
    sleep(0.01, 5)
    attack()
    sleep(0.30, 0.2)


def doubleJumpAttack():
    jump()
    sleep(0.08)
    if random.randint(0, 1) == 1:
        jump()
        sleep(0.04)
    jumpAttack()


def delayJumpAttack():
    jump()
    sleep(0.2)
    if random.randint(0, 1) == 1:
        jump()
        sleep(0.04)
    jumpAttack()


def highJumpAttack(self):
    jump()
    sleep(0.2)
    press('up')
    sleep()
    if random.randint(0, 1) == 1:
        jump()
        sleep(0.04)
    jumpAttack()
    sleep()
    release('up')


def turnJumpAttack():
    return


def bottomJumpAttack():
    press('down')
    sleep()
    jump()
    sleep(0.04)
    jumpAttack()
    sleep()
    release('down')


def upperImpale():
    press('up')
    sleep()
    button('f')
    sleep(0.01)
    button('d')
    sleep(0.02)
    button('d')
    sleep()
    release('up')
    sleep(0.15, 0.2)


def stopUpperImpale():
    releaseMove()
    sleep()
    upperImpale()
    sleep()
    pressMove(False)


def jumpStopUpperImpale():
    jump()
    sleep(0.1)
    stopUpperImpale()


def highJumpStopUpperImpale():
    jump()
    sleep(0.1)
    press('up')
    sleep()
    jumpStopUpperImpale()


def emergencyEscape():
    button('f2')
    sleep(0.2)
    button('enter')
    print('비상탈출. 약 10초뒤 종료합니다')
    sleep(10)
    sys.exit(1)
