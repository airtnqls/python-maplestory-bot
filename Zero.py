#!/usr/bin/python
"""
Basic botting program for Zero. Works with my keybindings only.

Premise:
A - Giga Crash
S - Flash Cut
D - Rising Slash
Del - Shadow Rain
End - Rhinne's Protection

Ctrl - Health pots

Run while in Beta form standing on a platform with a wall to your right.
This will bump the character against the wall and spam abilties in all
directions. This bot is not smart responsive except for potting when your
HP is low, so make sure you have thousands of health potions. If you get
moved out of position, the bot will continue doing the same thing, so you
need to find a place to stand where mobs do not or can not attack you.

Author: Alvin Lin (alvin.lin.dev@gmail)
"""
import ctypes

from Bot import Bot
from Keys import Keys
from Macro import Macro

import keyboard
import pywinauto as pwa
import time
import pyautogui
import threading
import random
import sys


def exitButton():
    while True:
        if keyboard.is_pressed('t'):  # if key 'q' is pressed
            sys.exit(1)
        else:
            pass


if __name__ == "__main__":

    if ctypes.windll.shell32.IsUserAnAdmin():
        print('관리자권한으로 실행된 프로세스입니다.')
    else:
        print('일반권한으로 실행된 프로세스입니다.')

    t = threading.Thread(target=exitButton, args=())
    t.start()
    while True:
        if keyboard.is_pressed('q'):  # if key 'q' is pressed
            print('You Pressed A Key!')
            break  # finishing the loop
        else:
            pass

    macro = Macro()

