#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# author:Dr.Shang
# file: 链队列.py
# time: 2019-10-20 22:23
# @Software: PyCharm

from typing import Optional
import random


class Node(object):
    def __init__(self, elem: int=None, next=None):
        """初始化一个链表节点"""
        self.elem = elem
        self._next = next


class LinkQueue(object):
    def __init__(self):
        # self._head = Node()
        # self._tail = Node()
        self._head: Optional[Node] = None  # puthon2.7不支持函数注解
        self._tail: Optional[Node] = None

    def is_empyt(self):
        return self._head == None

    def enqueue(self, elem: int):
        "入队"
        new_node = Node(elem=elem)
        if self._tail:
            self._tail._next = new_node
        else:
            self._head = new_node
        self._tail = new_node
        # print("头%d" % self._head.elem)
        # print("尾%d" % self._tail.elem)

    def dequeue(self):
        "出队并返回出队元素"
        if self._head:
            elem = self._head.elem
            # print("elem %d" % elem)
            self._head = self._head._next
            if not self._head:
                self._tail = None
            return elem
        else:
            return "队空"

    def scan(self):
        cur = self._head  # 必须用cur代指
        while(cur):
            print(cur.elem, end=' ')
            cur = cur._next
        print()


if __name__ == '__main__':
    mylinkqueue = LinkQueue()
    print("队列是否为空：")
    print(mylinkqueue.is_empyt())

    random.seed(2019)
    for i in range(10):
        random_num = random.randint(0, 100)
        mylinkqueue.enqueue(random_num)
    print("在随机插入十个节点后，队列中的元素有：")
    mylinkqueue.scan()


    values = []
    for _ in range(5):
        values.append(mylinkqueue.dequeue())
    print("出队的元素有：{}".format(values))
    print("在出队操作后，队列中的元素有：")
    mylinkqueue.scan()