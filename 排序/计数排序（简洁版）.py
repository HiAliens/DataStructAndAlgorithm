#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# author:Dr.Shang
# file: 计数排序（简洁版）.py
# time: 2019-11-18 16:34
# @Software: PyCharm

from typing import List
from itertools import accumulate


def counting_sort(a: List):
    counts = [0] * (max(a) + 1)  # 为0留出了位置，所以要+1

    for value in a:
        "记录a中元素出现的个数，counts索引是a中元素值，counts值是a中元素值出现的次数,此时的count相当于计数排序.py中的b"
        counts[value] += 1
    counts = list(accumulate(counts))  # 这里的counts相当于c，计算而且用了库函数，相当于函数“_get_counting_list”

    results = [0] * len(a)
    for value in reversed(a):  # 相当于函数 _sort_c
        index = counts[value] - 1
        results[index] = value
        counts[value] -= 1

    a[:] = results


if __name__ == "__main__":
    a1 = [1, 2, 3, 4]
    counting_sort(a1)
    print(a1)

    a2 = [1, 1, 1, 1]
    counting_sort(a2)
    print(a2)

    a3 = [4, 5, 0, 9, 3, 3, 1, 9, 8, 7]
    counting_sort(a3)
    print(a3)