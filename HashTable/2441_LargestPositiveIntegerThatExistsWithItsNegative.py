'''
Given an integer array nums that does not contain any zeros, find the largest positive integer k such that -k also exists in the array.

Return the positive integer k. If there is no such integer, return -1.

 

Example 1:

Input: nums = [-1,2,-3,3]
Output: 3
Explanation: 3 is the only valid k we can find in the array.
Example 2:

Input: nums = [-1,10,6,7,-7,1]
Output: 7
Explanation: Both 1 and 7 have their corresponding negative values in the array. 7 has a larger value.
Example 3:

Input: nums = [-10,8,6,7,-2,-3]
Output: -1
Explanation: There is no a single valid k, we return -1.
 

Constraints:

1 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
nums[i] != 0
'''
from typing import List


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        tmp_dict = dict()
        for num in nums:
            if abs(num) not in tmp_dict:
                tmp_dict[abs(num)] = num
            elif tmp_dict[abs(num)] == 0 or tmp_dict[abs(num)] == num:
                continue
            else:
                tmp_dict[abs(num)] += num
        print(tmp_dict)
        result = -1
        for key in tmp_dict:
            if tmp_dict[key] == 0:
                result = max(result, key)
        
        return result


a = Solution()
print(a.findMaxK([-34,7,7,-18,27,2,37,-50,-36,-7,31,23,5,-10,-3,45,20,-16,38,6]))
