#!usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author:terancechen
@file: 0075-Sort-Colors.py 
@version:
@time: 2022/04/12 
@email:terancechen@tencent.com
@function： 
"""
from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        todo: 重点
            all in [0, p0)      == 0
            all in [p0, i)      == 1
            all in [p2, len-1]  == 2
        """
        p0 = 0
        i = 0
        p2 = len(nums) - 1
        while i <= p2:
            if nums[i] == 0:
                nums[p0], nums[i] = nums[i], nums[p0]
                p0 += 1
                i += 1
            elif nums[i] == 2:
                nums[p2], nums[i] = nums[i], nums[p2]
                p2 -= 1
            elif nums[i] == 1:
                i += 1
        pass


if __name__ == "__main__":
    sol = Solution()

    nums = [2, 0, 2, 1, 1, 0]
    sol.sortColors(nums)

    print(nums)
