from typing import List

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        good_pair = 0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if(nums1[i] % (nums2[j] * k) == 0):
                    good_pair += 1

        return good_pair

sol = Solution()
print(sol.numberOfPairs([1,2,4,12], [2,4], 3))