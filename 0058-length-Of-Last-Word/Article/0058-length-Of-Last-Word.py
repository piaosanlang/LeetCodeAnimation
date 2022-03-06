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
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        # todo 代表是否开始计数
        isinit = True
        for char in s:
            if char == " ":
                isinit = True
            else:
                if isinit:
                    count = 0
                    isinit = False
                count += 1

        return count


if __name__ == "__main__":
    sol = Solution()

    nums = "Hello World  mm  "
    ret = sol.lengthOfLastWord(nums)
    print(ret)
