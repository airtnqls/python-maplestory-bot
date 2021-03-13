import time
import pyautogui
import random
import threading
import keyboard
import Action


class Tracker:
    player = ()
    user_warning = 0

    def trackingUser(self):
        while True:
            user = pyautogui.locateOnScreen('data/user.png', region=(0, 0, 300, 400))
            if user is None:
                print('3초지남')
                self.user_warning -= 1
                if self.user_warning < 0:
                    self.user_warning = 0
            else:
                self.user_warning += 3
                print(f'다른 유저 발견. 위험도: {self.user_warning}/10')
                if self.user_warning > 12:
                    Action.emergencyEscape()
                elif self.user_warning > 6:
                    Action.releaseMove()
            time.sleep(3)

    def loopTackingPlayer(self):
        while True:
            self.trackingPlayer()
            time.sleep(0.5)

    def trackingPlayer(self):
        mp = pyautogui.locateOnScreen('data/maple.png', region=(0, 0, 300, 400))
        player = pyautogui.locateOnScreen('data/player.png', region=(0, 0, 300, 400))
        if mp is None or player is None:
            print('None')
            return
        x = int(player[0]) - int(mp[0])
        y = int(player[1]) - int(mp[1])
        print(f'player x: {x}, y: {y}')
        self.player = (x, y)
        return x, y
