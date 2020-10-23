from itertools import cycle
from time import sleep


class TrafficLight:
    __color = ''


def running(self):
    colors_order = {"red": 7, "yellow": 3, "green": 7, "yellow": 3}
    for elem in cycle(colors_order.items()):
        TrafficLight.__color = elem[0]
        print(f"{TrafficLight.__color}")
        sleep(elem[1])


tl = TrafficLight
tl.running()
