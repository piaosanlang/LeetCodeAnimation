#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:terancechen
@file: 0042-Trap.py
@version:
@time: 2022/02/09
@email:terancechen@tencent.com
@function：
"""

from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    # todo 今天明白了一个大道理：

    # todo： mid   = int(left + (right - left) / 2)     ： 数据只有两个值时候，默认靠左侧
    # todo： rigth = int(left + (right - left + 1) / 2) ： 数据只有两个值时候，默认靠右侧
    # todo: 那么在二分查找过程中，一旦出现相同值时候，会出现 靠左侧的 mid = left 或者靠右侧的 mid = right 卡住死循环
    # todo: 对应的办法①，靠左的时候, 不可以存在 mid = left ,  执行指针要多(少)一位，因为mid = left, 意味着，nums[mid]>=target，则 mid = left + 1
    # todo: 对应的办法②，靠右的时候, 不可以存在 mid = right , 执行指针要多(少)一位，因为mid = right, 意味着，nums[mid]<=target，则 mid = right - 1

    def search_left(self, nums: List[int], target: int):
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = int(left + (right - left) / 2)
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] >= target:
                right = mid
        if nums[left] == target:
            return left
        return -1

    def search_right(self, nums: List[int], target: int):
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = int(left + (right - left + 1) / 2)
            if nums[mid] <= target:
                left = mid
            elif nums[mid] > target:
                right = mid - 1
        if nums[left] == target:
            return left
        return -1

    def search(self, nums: List[int], target: int) -> int:

        left = self.search_left(nums, target)
        right = self.search_right(nums, target)
        if left == -1 or right == -1:
            return 0
        return right - left +1


if __name__ == "__main__":
    sol = Solution()

    nums = [5, 7, 7, 8, 8, 10]
    ret = sol.search(nums, 8)
    print(ret)

    nums = [5, 7, 7, 8, 8, 10]
    ret = sol.search(nums, 6)
    print(ret)

    print('end')
