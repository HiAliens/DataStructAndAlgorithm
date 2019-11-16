#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# author:Dr.Shang
# file: 合并排序.py
# time: 2019-11-15 21:27
# @Software: PyCharm

from typing import List

"""排序依托于index，计算得其实是index得位置"""


def merge_sort(a: List[int]):
    lenth = len(a)
    if lenth <= 0:
        return False
    elif lenth == 1:
        return a
    _merge_sort_between(a, 0, lenth-1)


def _merge_sort_between(a: List[int], low: int, high: int):
    if low < high:
        mid = low + (high - low) // 2  # # 不要忘记+low
        _merge_sort_between(a, low, mid)
        _merge_sort_between(a, mid+1, high)
        _merge(a, low, mid, high)


def _merge(a, low, mid, high):
    i = low
    j = mid + 1
    tem = []
    while i <= mid and j <= high:  # 保证i，j游标的移动
        if a[i] >= a[j]:   # 相等情况下也要考虑
            tem.append(a[j])
            j += 1
        else:
            tem.append(a[i])
            i += 1
    # if i <= mid:
    #     begin = i, end = mid
    # else:
    #     begin = j, end = high  # 这行报错： int 不可迭代
    begin = i if i <= mid else j
    end = mid if i <= mid else high
    tem.extend(a[begin:end+1])
    a[low:high+1] = tem


if __name__ == '__main__':
    a1 = [3, 5, 6, 7, 8]
    a2 = [2, 2, 2, 2]
    a3 = [4, 3, 2, 1]
    a4 = [5, -1, 9, 3, 7, 8, 3, -2, 9]
    merge_sort(a1)
    print(a1)
    merge_sort(a2)
    print(a2)
    merge_sort(a3)
    print(a3)
    merge_sort(a4)
    print(a4)