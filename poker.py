import random
import threading
from threading import Semaphore


class PokerItem:
    def __init__(self, color, value):
        self.color = color
        self.value = value

    def __repr__(self):
        return '花色:{} 牌面:{}'.format(self.color, self.value)


class Poker:
    COLORS = ['Spade', 'Heart', 'Diamond', 'Club']
    VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'A', 'J', 'Q', 'K']

    def __init__(self):
        # 初始化
        self.poker_list = [PokerItem(color, value) for color in Poker.COLORS for value in Poker.VALUES]

    def shuffle(self):
        # 洗牌
        random.shuffle(self.poker_list)

    def deal(self):
        # 发牌, 每次发一张
        if self.poker_list:
            v = self.poker_list.pop()
            return v


p = Poker()
p.shuffle()


s1 = Semaphore(1)
s2 = Semaphore(0)
s3 = Semaphore(0)
s4 = Semaphore(0)


def get_pokers1():
    while 1:
        s1.acquire()
        v = p.deal()
        s2.release()
        if not v:
            break
        print('Thread1 取牌 {}'.format(v))


def get_pokers2():
    while 1:
        s2.acquire()
        v = p.deal()
        s3.release()
        if not v:
            break
        print('Thread2 取牌 {}'.format(v))


def get_pokers3():
    while 1:
        s3.acquire()
        v = p.deal()
        s4.release()
        if not v:
            break
        print('Thread3 取牌 {}'.format(v))


def get_pokers4():
    while 1:
        s4.acquire()
        v = p.deal()
        s1.release()
        if not v:
            break
        print('Thread4 取牌 {}'.format(v))


t1 = threading.Thread(target=get_pokers1)
t2 = threading.Thread(target=get_pokers2)
t3 = threading.Thread(target=get_pokers3)
t4 = threading.Thread(target=get_pokers4)


t1.start()
t2.start()
t3.start()
t4.start()




