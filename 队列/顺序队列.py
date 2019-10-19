#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# author:Dr.Shang
# file: 顺序队列.py
# time: 2019-10-19 21:55
# @Software: PyCharm


class Queue(object):
    def __init__(self, n):
        """
        初始化队列和队列元素
        :param n:队列长度
        """
        self._head = 0
        self._tail = 0
        self._queue = [None] * n
        self._lenth = n  # 最大长度

    def is_empty(self):
        """判断队列是否为空"""

        return self._head == self._tail == 0

    def enqueue(self, elem):
        """入队操作"""
        if self._lenth == self._tail:
            print("队列已满")
        else:
            self._queue[self._tail] = elem
            self._tail += 1

    def dequeue(self):
        """出队操作"""
        if self.is_empty():
            print("队列中没有元素")
        else:
            elem = self._queue[self._head]
            self._head += 1
            print("出队元素为：", elem)

    def scan(self):
        for elem in range(self._head+1, self._tail+1):
            print(elem, end=' ')


if __name__ == '__main__':
    myqueue = Queue(10)
    print('队列是否为空：', myqueue.is_empty())

    myqueue.enqueue(1)
    print("入队元素1后，队列中元素为：")
    myqueue.scan()
    print()

    import random
    random.seed(2019)
    # 随机入队9个数（队列容量为10）
    for i in range(9):
        random_elem = random.randint(0, 100)
        myqueue.enqueue(random_elem)
    print("随机入队元素后，队列中元素为：")
    myqueue.scan()
    print('队列是否为空：', myqueue.is_empty())

    myqueue.enqueue(2)

    myqueue.dequeue()
    print("进行出队操作后，队中元素为：")
    myqueue.scan()

    myqueue.dequeue()
    print("进行出队操作后，队中元素为：")
    myqueue.scan()