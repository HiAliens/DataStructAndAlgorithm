#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# author:Dr.Shang
# file: 循环队列.py
# time: 2019-10-21 23:32
# @Software: PyCharm

"""
循环队列的实现是借助python的列表，然后通过限制头指针（C语言中的说法）和尾指针来实现循环
"""
import random


class CirculrQueue:
    def __init__(self, capacity: int):
        self._capacity = capacity + 1
        self._elem = []
        self._head = 0
        self._tail = 0

    def is_empty(self):
        return self._tail == self._head

    def enqueue(self, elem: float):
        "入队"
        if (self._tail + 1) % self._capacity == self._head:
            return "队满"
        self._elem.append(elem)
        self._tail = (self._tail + 1) % self._capacity
        return "入队成功"

    def dequeue(self):
        "出队"
        if self.is_empty():
            return "队空"
        item = self._elem[self._head]
        self._head = (self._head + 1) % self._capacity
        return item

    def scan(self):
        "遍历队列中的元素"
        if self.is_empty():
            return "队空"
        return self._elem


if __name__ == '__main__':
    random.seed(2019)
    num = 10
    myCircleQueue = CirculrQueue(num)

    # 连续入队
    for _ in range(num):
        random_num = random.random()
        myCircleQueue.enqueue(random_num)
    print("随机入队%d个元素后，循环队列中的元素为：" % num)
    print(myCircleQueue.scan())

    # 尝试队满入队的情况
    print(myCircleQueue.enqueue(11.2))

    # 连续出队
    print("出队元素依次为:")
    for _ in range(num):
        item = myCircleQueue.dequeue()
        print(item, end=' ')
    print()

    # 尝试队空出队
    print(myCircleQueue.dequeue())