#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# author:Dr.Shang
# file: 冒泡排序.py
# time: 2019-10-24 22:33
# @Software: PyCharm

from typing import List
import random


def bubble_sort(array: List[int or float]) -> List[int or float]:
    lenth = len(array)
    for i in range(lenth):
        swap_flag = False
        for j in range(lenth - i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
            swap_flag = True
        if not swap_flag:
            break
    return array

if __name__ == '__main__':

    # 随机构造一个数组
    random.seed(2019)
    my_list = []
    for _ in range(10):
        random_num = random.randrange(100)
        my_list.append(random_num)
    print("为排序的数组为：")
    print(my_list)
    print("排序过后的数组为：")
    print(bubble_sort(my_list))