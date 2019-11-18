#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# author:Dr.Shang
# file: 计数排序.py
# time: 2019-11-18 14:32
# @Software: PyCharm


from typing import List


def counting_sort(a: List[int]):
    """
    下面代码中的b，c计算过程体现了“计数”一词的由来。
    :param a: 待排序数组
    :return:
    """

    max_item = _find_max_item(a)
    b = _make_list(max_item+1)
    for i in range(len(a)):
       b[a[i]] += 1
    # print("a is ", a)
    # rint("b is ", b)
    c = _get_counting_list(b)
    # print("c is ", c)
    # print('')
    result = _sort_c(c, a)
    # print("result is ", result)

    a[:] = result[:]


def _make_list(lenth):
    l = []  # 待生成的数组
    for j in range(lenth):
        l.append(0)
    return l


def _find_max_item(a: List[int]):
    max_item = max(a)
    return max_item


def _get_counting_list(b: List[int]):
    lenth_b = len(b)
    c = _make_list(lenth_b)
    c[0] = b[0]
    for i in range(1, lenth_b):
        c[i] = b[i]+c[i-1]
    return c


def _sort_c(c: List[int], a: List[int]):
    result = _make_list(len(a))
    for i in range(len(a)-1, -1,  -1):
        temp = c[a[i]]
        # print("temp is", temp)
        result[temp-1] = a[i]
        c[a[i]] -= 1
    return result



if __name__ == '__main__':
    a1 = [0, 1, 2, 3, 4]
    counting_sort(a1)
    print(a1)

    a2 = [1, 1, 1, 1]
    counting_sort(a2)
    print(a2)

    a3 = [4, 5, 0, 9, 3, 3, 1, 9, 8, 7]
    counting_sort(a3)
    print(a3)
