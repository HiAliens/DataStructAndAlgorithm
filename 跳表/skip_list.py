#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# author:Dr.Shang
# file: skip_list.py
# time: 2019-11-24 19:37
# @Software: PyCharm
from typing import Optional
import random


class ListNode:
    def __init__(self, data: Optional[int] = None):
        self._data = data
        self._forwards = []  # 存储的是同一个节点在每一层的下一个位置的索引


class SkipList:

    _MAX_LEVEL = 16

    def __init__(self):
        self._head = ListNode()
        self._level_count = 1  # 一共有n层有数据，以find为例，从第n层开始，从上到下寻找待查找元素
        self._head._forwards = [None] * type(self)._MAX_LEVEL

    def find(self, value: int)-> Optional[ListNode]:
        """
        在for循环中，若当前节点P.data小于value，说明需要继续向右走（跳过若干个节点），通过p = p._forwards[i] 实现，
        _forwards[i]存储的是和P同层的下一个节点的位置。
        若是不满足while条件：1.当前节点P同层的下一个节点没有值 2.当前节点P同层的下一个节点大于待查找元素值
        通过i的依次减小来实现向下走，即对对当前节点降低一层，然后在低一层中寻找，不满足在降低一层
        :param value:
        :return:
        """
        p = self._head  # 是链表的头节点，没有值，下一个节点是最高层的第一个元素。
        for i in range(self._level_count - 1, -1, -1):
            while p._forwards[i] and p._forwards[i]._data < value:
                p = p._forwards[i]  # 将P指向同层的下一个节点

        return p._forwards[0] if p._forwards[0] and p._forwards[0]._data == value else None

    def insert(self, value: int):
        level = self._random_level()  # 获得新插入数据，需要插入的索引的层数
        if self._level_count < level: self._level_count = level
        new_node = ListNode(value)
        new_node._forwards = [None] * level
        update = [self._head] * level  # 记录每一层应该插入节点位置的前驱，单链表插入元素需要前驱节点

        p = self._head  # 所有操作都需要从头节点遍历，找到满足条件的位置（对应元素）
        for i in range(level-1, -1, -1):
            "实现找到目标位置的功能，与find（）中一样"
            while p._forwards[i] and p._forwards[i]._data < value:
                p = p._forwards[i]

            # 记录每一次需要插入位置的前驱节点，原理：从上到下，每一层待插入位置的前面元素个数会依次增加，
            # 故只有当i值增加（p位置即将降低一层时）此时p的位置才是满足条件的待插入位置，结合图示理解
            update[i] = p

        for i in range(level):
            "实现将待插入元素插入到每一层中,相当于对多层执行单链表的插入节点操作"
            new_node._forwards[i] = update[i]._forwards[i]  # new_node.next = prev.next,每一步的i是为了保证在同一层中执行插入操作
            update[i]._forwards[i] = new_node   # prev.next = new_node

    def delete(self, value):
        update = [None] * self._level_count
        p = self._head
        for i in range(self._level_count-1, -1, -1):
            while p._forwards[i] and p._forwards[i]._data < value:
                p = p._forwards[i]
            update[i] = p

        if p._forwards[0] and p._forwards[0]._data == value:
            for i in range(self._level_count-1, -1, -1):
                if update[i]._forwards[i] and update[i]._forwards[i]._data == value:
                    update[i]._forwards[i] = update[i]._forwards[i]._forwards[i]

    def _random_level(self, p: float = 0.5)-> int:
        level = 1
        while random.random() < p and level < type(self)._MAX_LEVEL:
            level += 1
        return level

    def __repr__(self) -> str:
        values = []
        p = self._head
        while p._forwards[0]:
            values.append(str(p._forwards[0]._data))
            p = p._forwards[0]
        return "->".join(values)


if __name__ == "__main__":
    l = SkipList()
    for i in range(10):
        l.insert(i)
    print(l)
    p = l.find(7)
    print(p._data)
    l.delete(3)
    print(l)