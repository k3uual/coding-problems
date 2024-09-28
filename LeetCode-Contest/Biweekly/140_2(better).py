"""You are given an array maximumHeight, where maximumHeight[i] denotes the maximum height the ith tower can be assigned.

Your task is to assign a height to each tower so that:

The height of the ith tower is a positive integer and does not exceed maximumHeight[i].
No two towers have the same height.
Return the maximum possible total sum of the tower heights. If it's not possible to assign heights, return -1.


Example 1:

Input: maximumHeight = [2,3,4,3]

Output: 10

Explanation:

We can assign heights in the following way: [1, 2, 4, 3].

Example 2:

Input: maximumHeight = [15,10]

Output: 25

Explanation:

We can assign heights in the following way: [15, 10].

Example 3:

Input: maximumHeight = [2,2,1]

Output: -1

Explanation:

It's impossible to assign positive heights to each index so that no two towers have the same height.

"""
from typing import List

class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        r = 0
        hs = sorted(maximumHeight, reverse=True)
        p = -1
        for h in hs:
            if  p==-1:
                r+=h
                p=h-1
            else:
                h = min(h, p)
                r+=h
                p=h-1
            if h<=0: return -1
        return r