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

    def enqueue_2(self, elem):
        """
        当无法队未满，但无法插入元素时，在入队时进行数据搬移。
        :return:
        """
        if self._tail == self._lenth:
            if self._head == 0:  # 队满
                return False
            for i in range(self._head, self._tail):
                idx = int(i - self._head)
                self._queue[idx] = self._queue[i]  # 数据搬移操作

            self._tail -= self._head
            self._head = 0
        self._queue[self._tail] = elem
        self._tail += 1

    def scan(self):
        for elem in range(self._head, self._tail):
            print(self._queue[elem], end=' ')
        print()
        print('队头下标为：', self._head)
        print('队尾下标为：', self._tail)


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
    print("第一次进行出队操作后，队中元素为：")
    myqueue.scan()

    myqueue.dequeue()
    print("第二次进行出队操作后，队中元素为：")
    myqueue.scan()

    myqueue.dequeue()
    print("第三次进行出队操作后，队中元素为：")
    myqueue.scan()

    myqueue.enqueue(2)
    print("可以看到，此时队头还有空位，但无法入队")
    print()

    print("-" * 40)
    print("下面采用enqueue_2（），可以在上述情况下，执行出队操作时进行数据搬移")

    myqueue.enqueue_2(2)
    print("进行插入元素后，队中元素尾：")
    myqueue.scan()

    print("-" * 40)