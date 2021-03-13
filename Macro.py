import time
import pyautogui
import random
import threading
import keyboard

import Action

from Timer import Timer
from Tracker import Tracker

def rand(num):
    t = num * 0.2
    return num + random.uniform(-t, t);


# 키보드 제어 불가능시 세이프
pyautogui.FAILSAFE = True


class Macro:
    start = False
    info = []
    dir = True  # true left down, false right up
    map = None  # (x1, y1, x2, y2)
    time = 0  # 7sec response

    def __init__(self):
        self.timer = Timer()
        self.tracker = Tracker()
        t = threading.Thread(target=self.inputKeyThread, args=())
        t.start()

    def StartMacro(self):
        if self.start is True:
            return
        self.start = True
        print('매크로 시작')
        t = threading.Timer(3, self.tracker.trackingUser)
        t2 = threading.Timer(1, self.tracker.loopTackingPlayer)
        t.start()
        t2.start()
        while True:
            self.directionControl()
            self.control()
            while keyboard.is_pressed('left') or keyboard.is_pressed('right'):
                time.sleep(5)
            time.sleep(0.02)

    def control(self):
        if self.dir:
            if self.map[1] < self.tracker.player[1]:
                self.topLeftToRight()
            else:
                self.topRightToBottom()
        else:
            if self.map[1] >= self.tracker.player[1]:
                self.bottomLeftToRight()
            else:
                self.bottomLeftToTop()

    def topLeftToRight(self):
        Action.doubleJumpAttack()

    def topRightToBottom(self):
        Action.bottomJumpAttack()

    def bottomLeftToRight(self):
        Action.doubleJumpAttack()

    def bottomLeftToTop(self):
        Action.upperImpale()


    def directionControl(self):
        if self.dir is True:
            if self.map[0] + 30 >= self.tracker.player[0]:
                print('우로돌아')
                self.dir = False
                Action.releaseMove()
                time.sleep(0.02)
                Action.pressMove(False)
        else:
            if self.map[2] - 30 <= self.tracker.player[0]:
                print('좌로돌아')
                self.dir = True
                Action.releaseMove()
                time.sleep(0.02)
                Action.pressMove(True)

    def inputKeyThread(self):
        was_pressed = False
        while True:
            if keyboard.is_pressed('num_0'):  # if key 'q' is pressed
                if not was_pressed:
                    print('키 입력됨. 처리중..')
                    result = self.tracker.trackingPlayer()
                    if result is None:
                        was_pressed = True
                        continue
                    self.info.append(result)
                    print(f'완료 length: {len(self.info)}, pos: {result}')
                    self.analysisMap()
                    was_pressed = True
            else:
                was_pressed = False
                pass

    def analysisMap(self):
        left = top = 10000
        right = bottom = -10000

        if len(self.info) < 3:
            return
        for item in self.info:
            if left > item[0]:
                left = item[0]
            if top > item[1]:
                top = item[1]
            if right < item[0]:
                right = item[0]
            if bottom < item[1]:
                bottom = item[1]
        self.map = (left, top, right, bottom)
        print(f'map: {self.map}')
        self.StartMacro()
