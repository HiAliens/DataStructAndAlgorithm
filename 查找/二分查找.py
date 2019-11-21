#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# author:Dr.Shang
# file: 二分查找.py
# time: 2019-11-21 10:50
# @Software: PyCharm
'''二分查找分为非递归实现和递归实现，其时间复杂度达到了惊人的O（logn），但对待查找的数组有要求：
1.数组有序
2.必须是数组，不能是链表
3.不适合数据过小和过大的数据
'''
from typing import List
import numpy as np


def binary_search(a: List, value):
    low = 0
    high = len(a) - 1
    mid = low + (high - low) >> 1

    while low <= high:
        if a[mid] == value:
            return mid
        elif value < a[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1


def bsearch_recursion(a: List[int], value: int) -> int:
    low = 0
    high = len(a) - 1

    return _bsearch_recursiong_betw(a, low, high, value)


def _bsearch_recursiong_betw(a: List[int], low: int, high: int, value: int) ->int:
    if low >= high:
        return -1
    mid = low + (high - low) >> 1
    if a[mid] == value:
        return mid
    elif value < a[mid]:
        return _bsearch_recursiong_betw(a, low, mid-1, value)
    else:
        return _bsearch_recursiong_betw(a, mid+1, high, value)


if __name__ == '__main__':
    np.random.seed(2019)
    a = np.random.randint(0, 100, size=20)  # [72 31 37 88 62 24 29 15 12 16 48 71 83 12 80 50 95  5 24 28]
    a = list(a)
    idx = binary_search(a, 16)
    idx1 = bsearch_recursion(a, 16)
    print(idx == idx1)
