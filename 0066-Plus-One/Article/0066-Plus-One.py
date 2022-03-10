#!usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author:terancechen
@file: 0066-Plus-One.py 
@version:
@time: 2022/03/10 
@email:terancechen@tencent.com
@function： 
"""
from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        isjin = 1

        digits.reverse()
        for i, num in enumerate(digits):
            if num + isjin == 10:
                isjin = 1
                digits[i] = 0
            else:
                digits[i] = num + isjin
                isjin = 0
        if isjin == 1:
            digits.append(1)
        digits.reverse()
        return digits


if __name__ == "__main__":
    sol = Solution()

    nums = [1,2,3]
    ret = sol.plusOne(nums)
    print(ret)

    nums = [1,2,9]
    ret = sol.plusOne(nums)
    print(ret)

    nums = [1,9,9]
    ret = sol.plusOne(nums)
    print(ret)

    nums = [9,9,9]
    ret = sol.plusOne(nums)
    print(ret)