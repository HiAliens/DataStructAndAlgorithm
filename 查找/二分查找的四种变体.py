#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# author:Dr.Shang
# file: 二分查找的四种变体.py
# time: 2019-11-23 13:54
# @Software: PyCharm
from typing import List


def bsearch_variation1(a: List[int], value: [int]):
    """查找第一个值等于给定值的元素"""
    low = 0
    high = len(a) - 1
    while low <= high:
        mid = low + ((high - low) >> 1)  # 注意移位运算的优先级
        if a[mid] < value:
            low = mid + 1
        elif a[mid] > value:
            high = mid - 1
        else:
            if mid == 0 or a[mid-1] != value: return mid
            else:
                high = mid - 1
    return -1


def bsearch_variation2(a: List[int], value: int):
    """查找最后一个值等于给定值的元素"""
    low = 0
    high = len(a) - 1
    while(low <= high):
        mid = low + ((high - low) >> 1)
        if a[mid] < value:
            low = mid + 1
        elif a[mid] > value:
            high = mid -1
        else:
            if mid == len(a)-1 or a[mid+1] != value: return mid
            else:
                low = mid +1
    return -1


def bsearch_variation3(a: List[int], value: int):
    """
    查找第一个大于等于给定值的元素
    :param a:array to search
    :param value:desired item
    :return:
    """
    low = 0
    high = len(a) - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if a[mid] < value:
            low = mid + 1
        else:
            if mid == 0 or a[mid-1] < value: return mid
            else:  # a[mid-1] >= value
                high = mid - 1
    return -1


def bsearch_variation4(a: List[int], value: int):
    """
    查找最后一个小于等于给定值的元素
    :param a:array to search
    :param value:desired item
    :return:
    """
    low = 0
    high = len(a) - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if a[mid] > value:
            high = mid - 1
        else:
            if mid == len(a)-1 or a[mid+1] > value: return mid
            else:
                low = mid + 1
    return -1


if __name__ == '__main__':
    a = [1, 1, 2, 3, 4, 6, 7, 7, 7, 7, 10, 22]
    print(bsearch_variation1(a, 7) == 6)
    print(bsearch_variation1(a, 100) == -1)

    print(bsearch_variation2(a, 100) == -1)
    print(bsearch_variation2(a, 7) == 9)

    print(bsearch_variation3(a, 100) == -1)
    print(bsearch_variation3(a, 5) == 5)
    print(bsearch_variation3(a, 6) == 5)

    print(bsearch_variation4(a, 0) == -1)
    print(bsearch_variation4(a, 23) == 11)
    print(bsearch_variation4(a, 22) == 11)