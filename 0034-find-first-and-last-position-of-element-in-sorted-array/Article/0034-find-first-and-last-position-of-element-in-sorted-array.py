#!usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author:terancechen
@file: 0034-find-first-and-last-position-of-element-in-sorted-array.py 
@version:
@time: 2022/02/05 
@email:terancechen@tencent.com
@function： 
"""
from typing import Optional, List
import heapq


class Solution:
    """
    > mid   = int(left + (right - left) / 2)     ： 数据只有两个值时候，默认靠左侧
    > rigth = int(left + (right - left + 1) / 2) ： 数据只有两个值时候，默认靠右侧

    > 那么在二分查找过程中，一旦出现相同值时候，会出现 靠左侧的 `mid = left` 或者靠右侧的 `mid = right` 卡住死循环

    > - 对应的办法①，靠左的时候, 不可以存在 mid = left ,  执行指针要多(少)一位，因为mid = left, 意味着，nums[mid]>=target，则 mid = left + 1
    > - 对应的办法②，靠右的时候, 不可以存在 mid = right , 执行指针要多(少)一位，因为mid = right, 意味着，nums[mid]<=target，则 mid = right - 1

    """
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1, -1]
        if len(nums) < 1:
            return res
        left = 0
        right = len(nums) - 1

        left = self.getFirstPos(nums, target, left, right)
        if left == -1:
            return res

        right = self.getLastPos(nums, target, left, right)
        if right == -1:
            return res
        return [left, right]

    def getFirstPos(self, nums, target, left, right):
        """

        """
        while left < right:
            mid = int(left + (right - left) / 2)
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1

        if nums[left] == target:
            return left
        return -1

    def getLastPos(self, nums, target, left, right):
        """

        """
        while left < right:
            mid = int(left + (right - left + 1) / 2)
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid
        if nums[left] == target:
            return left
        return -1


if __name__ == "__main__":
    sol = Solution()

    nums = [5, 7, 7, 8, 8, 10]
    target = 8

    # nums = [5, 7, 7, 8, 8, 10]
    # target = 6

    # nums = []
    # target = 0

    # nums = [1]
    # target = 1

    # nums = [2, 2]
    # target = 2

    # nums = [1, 2, 3]
    # target = 2

    left, right = sol.searchRange(nums, target)
    print(left, right)
