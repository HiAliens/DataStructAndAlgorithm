#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# author:Dr.Shang
# file: 插入排序.py
# time: 2019-10-27 20:17
# @Software: PyCharm

import random
from typing import List


def insert_sort(array: List[int or float]):
    lenth = len(array)
    if lenth == 0:
        return False

    for i in range(1, lenth):
        for j in range(i, 0, -1):
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
    return array


if __name__ == '__main__':
    # random.seed(2019)
    myarray = []
    for _ in range(10):
        random_item = random.uniform(1, 100)
        myarray.append(random_item)

    print("随机初始化的数组为：")
    print(myarray)
    print("插入排序后的数组为：")
    print(insert_sort(myarray))