#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# author:Dr.Shang
# file: 单链表.py
# time: 2019-10-13 18:45
# @Software: PyCharm


class Node(object):
    """节点"""

    def __init__(self, elem, next=None):
        self.elem = elem
        self.next = next   # 初始化时，指向下一个节点的“指针”为空


# 创建单链表，实现单链表的增删改查操作
class SingleLinkList(object):
    """单链表数据结构，其中操作的命名参考了python列表的方法的命名，比如，append是在列表尾部插入数据的"""

    def __init__(self, node=None):
        """初始化一个头节点属性,这里的关键字参数node表示传入的头节点，默认为空"""
        self.__head = node

    def is_empty(self):
        """判断单链表是否为空的方法"""
        return self.__head == None

    def lenth(self):
        """计算单链表长度的方法"""
        # 思路是利用游标（cursor）从头遍历链表，使用cnt（count）统计所包含节点的个数
        cur = self.__head
        cnt = 0
        while cur != None:
            cnt += 1
            cur = cur.next
        return cnt

    def scan(self):
        """从头遍历整个链表"""
        cur = self.__head
        while cur != None:
            print(cur.elem, end=' ')
            cur = cur.next
        print('\n')

    def add(self, elem):
        """向单链表的头部添加元素"""
        node = Node(elem)
        node.next = self.__head
        self.__head = node

    def append(self, elem):
        """向单链表的尾部插入元素"""
        node = Node(elem)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, elem):
        """向指定位置添加元素"""
        if pos <= 0:
            # 头插法
            self.add(elem)
        elif pos > self.lenth() - 1:
            # 尾差法
            self.append(elem)
        else:
            cur = self.__head
            cnt = 0
            while cnt < pos - 1:
                # 移动到pos的前一个位置
                cnt += 1
                cur = cur.next
            node = Node(elem)
            node.next = cur.next
            cur.next = node

    def remove(self, elem):
        """删除"""
        cur = self.__head
        pre = None  # 前驱节点，记录被删除节点的前一个位置
        while cur != None:
            if cur.elem == elem:
                if cur == self.__head:
                    # 判断一下是不是头节点,若是，更改头节点
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    def search(self, elem):
        """查找节点是否存在于链表中"""
        cur = self.__head
        while cur != None:
            if cur.elem == elem:
                return True
            else:
                cur = cur.next
        return False


if __name__ == '__main__':
    # 创建一个链表实例
    llinklist = SingleLinkList()

    print('链表是否为空:{}'.format(llinklist.is_empty()))
    print('链表的长度为:{}'.format(llinklist.lenth()))
    # 向链表头部插入一个节点
    llinklist.add(1)
    print('在向链表头部插入一个值为1的节点操作之后链表中的元素为：', end='')
    llinklist.scan()

    # 向链表尾部插入一个节点
    llinklist.append(3)
    print('在向链表尾部插入一个值为3的节点操作之后链表中的元素为：', end='')
    llinklist.scan()

    llinklist.add(4)
    print('在向链表头部插入一个值为4的节点操作之后链表中的元素为：', end='')
    llinklist.scan()

    # 在指定位置插入一个节点
    llinklist.insert(2, 5)
    print('在指定位置2，插入一个值为5的节点操作之后链表中的元素为：', end='')
    llinklist.scan()

    llinklist.insert(-1, 0)
    print('在指定位置-1，插入一个值为0的节点操作之后链表中的元素为：', end='')
    llinklist.scan()

    print('链表是否为空:{}'.format(llinklist.is_empty()))
    print('链表的长度为:{}'.format(llinklist.lenth()))

    llinklist.insert(10, 6)
    print('在指定位置10(此时列表长为{})，插入一个值为0的节点操作之后链表中的元素为：'.format(llinklist.lenth()-1), end='')
    llinklist.scan()

    llinklist.remove(6)
    print('在删除值为6的节点操作之后链表中的元素为：', end='')
    llinklist.scan()
