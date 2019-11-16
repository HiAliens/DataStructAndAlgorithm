#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# author:Dr.Shang
# file: 快速排序.py
# time: 2019-11-16 14:35
# @Software: PyCharm

from typing import List


def quick_sort(a: List[int]):
    lenth = len(a)
    _quick_sort_between(a, 0, lenth-1)


def _quick_sort_between(a, low, high):
    if low < high:
        mid = _select_mid(a, low, high)  # 选择出分界点
        _quick_sort_between(a, low, mid-1)  # 注意mid-1
        _quick_sort_between(a, mid+1, high)  # 注意mid+1


def _select_mid(a, low, high):
    base = a[high]  # 确定最后数组最后一个元素为待比较对象
    i = low
    for j in range(low, high):
        if a[j] < base:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[high] = a[high], a[i]
    return i


if __name__ == "__main__":
    a1 = [3, 5, 6, 7, 8]
    a2 = [2, 2, 2, 2]
    a3 = [4, 3, 2, 1]
    a4 = [5, -1, 9, 3, 7, 8, 3, -2, 9]
    quick_sort(a1)
    print(a1)
    quick_sort(a2)
    print(a2)
    quick_sort(a3)
    print(a3)
    quick_sort(a4)
    print(a4)
