#!usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author:terancechen
@file: 0070-Climbing-Stairs.py 
@version:
@time: 2022/04/03 
@email:terancechen@tencent.com
@function： 
"""


class Solution:

    remember = dict()

    def climbStairs(self, n: int) -> int:

        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:

            num1 = self.remember[n - 1] if n-1 in self.remember else self.climbStairs(n - 1)
            num2 = self.remember[n - 2] if n - 2 in self.remember else self.climbStairs(n - 2)

            result = num1 + num2

            self.remember[n - 1] = num1
            self.remember[n - 2] = num2
            self.remember[n] = result

            return result
        pass


if __name__ == "__main__":
    sol = Solution()

    ret = sol.climbStairs(3)

    print(ret)
