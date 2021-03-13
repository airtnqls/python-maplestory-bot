
import threading

import pyautogui


class Ready:
    skillHunt = {
        'shift': (30, False),
        's': (20, False),
        'q': (60, False),
        'v': (60, False),
        '7': (250, False),
    }

    skillBoss = {
        '1': (180, False),
        'e': (180, False),
        'r': (180, False),
        'ctrl': (90, False),
    }

    buff = [
        ('3', 180, False),
        ('4', 180, False),
        ('5', 240, False),
        ('8', 600, False),
        ('9', 7200, False),
        ('page_down', 120, False),
    ]

    buffExp = [
        ('Extreme gold', 1800, False),
        ('MVP', 1800, False),
        ('Coupon 30m', 1800, False),
        ('Coupon 15m', 900, False),
        ('Wealth elixir', 7200, False),
        ('Exp elixir', 7200, False),
    ]


class Timer:
    response = 7
    move_f = 7
    ready = Ready()

    def __init__(self):
        print('d')

    @staticmethod
    def timer(obj: (str, int, bool)):
        obj[2] = True

    def manage(self):
        for item in self.ready.buff:
            if item[2] is True:
                threading.Timer(item[1], self.timer, args=item).start()
