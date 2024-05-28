from typing import List
import math
class Solution:
    def __init__(self):
        pass

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        gap = m + n
        while(gap > 1):
            gap = (gap//2) + (gap%2)
            left = 0
            right = left + gap

            while(right < m+n):
                if(right >= m and left < m):
                    self.swap_if_great(nums1, left, nums2, right - m)
                elif(left >= m):
                    self.swap_if_great(nums2, left - m, nums2, right - m)
                else:
                    self.swap_if_great(nums1, left, nums1, right)
                left += 1
                right += 1
    
    def swap_if_great(self, nums1: List[int], ind1: int, nums2: List[int], ind2: int):
        if(nums1[ind1] > nums2[ind2]):
            nums1[ind1], nums2[ind2] = nums2[ind2], nums1[ind1]
                    
arr1 = [1,3,5,7] 
arr2 = [0,2,6,8,9]
sol = Solution()
sol.merge(arr1, len(arr1), arr2, len(arr2))
print(arr1, arr2)