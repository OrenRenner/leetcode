'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]



Constraints:

    2 <= nums.length <= 104
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    Only one valid answer exists.


Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
Accepted
5,717,056
Submissions
11,883,903

'''

class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        for index1, item1 in enumerate(nums):
            for index2, item2 in enumerate(nums):
                if index1 != index2 and item1 + item2 == target:
                    return [index1, index2]


a = Solution()
print(a.twoSum(nums = [3,2,4], target = 6))