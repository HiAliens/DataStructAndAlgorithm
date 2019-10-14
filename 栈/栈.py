#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# author:Dr.Shang
# file: 栈.py
# time: 2019-10-14 22:03
# @Software: PyCharm


class Stack(object):
    """使用python的list【】实现栈"""
    def __init__(self):
        self.__elems = []

    def is_empty(self):
        """判断栈是否为空"""
        return self.__elems == []

    def push(self, elem):
        """入栈：向栈顶插入一个元素"""
        self.__elems.append(elem)

    def pop(self):
        """出栈：从栈顶弹出一个元素"""
        return self.__elems.pop()

    def top(self):
        """返回栈顶元素"""
        return self.__elems[len(self.__elems) - 1]

    def lenth(self):
        """返回栈中元素个数"""
        return len(self.__elems)

    def scan(self):
        """返回栈中存在的元素"""
        print(self.__elems)


if __name__ == '__main__':
    stack = Stack()

    print('栈是否为空:{}'.format(stack.is_empty()))
    print('栈的长度为:{}'.format(stack.lenth()))

    # 入栈元素1
    stack.push(1)
    print('在入栈元素1后，栈中元素有：', end=' ')
    stack.scan()

    # 入栈元素2
    stack.push(2)
    print('在入栈元素2后，栈中元素有：', end=' ')
    stack.scan()

    # 返回栈顶元素
    print('栈顶元素为{}'.format(stack.top()))

    # 出栈
    stack.pop()
    print('在出栈操作后，栈中元素为：', end=' ')
    stack.scan()

    print('栈是否为空:{}'.format(stack.is_empty()))
    print('栈的长度为:{}'.format(stack.lenth()))
