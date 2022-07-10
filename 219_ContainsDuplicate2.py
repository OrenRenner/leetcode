"""

Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.



Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false


Constraints:

1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
0 <= k <= 10^5

"""


class Solution:
    def containsNearbyDuplicate(self, nums: list, k: int) -> bool:
        d = dict()
        for index, num in enumerate(nums):
            if num in d and abs(d[num] - index) <= k:
                return True
            d[num] = index

        return False


a = Solution()
print(a.containsNearbyDuplicate(nums = [1,2,3,1], k = 3))
