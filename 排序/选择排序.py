#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# author:Dr.Shang
# file: 选择排序.py
# time: 2019-10-26 20:51
# @Software: PyCharm

import random
from typing import List


def Select_sort(array: List[int or float]) ->List[int or float]:
    lenth = len(array)
    if lenth < 0:
        return False

    for i in range(lenth):
        # i 代表第i轮，也是array中的第i个元素
        min_idx = i
        min_value = array[i]
        for j in range(i, lenth):  # 为了找到最小元素
            if min_value > array[j]:
                min_idx = j
                min_value = array[j]
        array[min_idx], array[i] = array[i], array[min_idx]
    return array


if __name__ == '__main__':
    random.seed(2019)
    my_queue = []
    for _ in range(10):
        random_elem = random.random()
        my_queue.append(random_elem)
    print("随机初始化的数组为：")
    print(my_queue)
    print('排序之后的数组为:')
    print(Select_sort(my_queue))