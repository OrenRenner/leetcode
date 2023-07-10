"""

Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
 

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000

"""
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection_dict = dict()
        for num in nums1:
            intersection_dict[num] = 1
        
        for num in nums2:
            if num in intersection_dict:
                intersection_dict[num] += 1
        
        res = []
        for key, value in intersection_dict.items():
            if value > 1:
                res.append(key)
        return res