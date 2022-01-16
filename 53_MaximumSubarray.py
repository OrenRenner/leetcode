'''

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.



Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:

Input: nums = [1]
Output: 1

Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23



Constraints:

    1 <= nums.length <= 10^5
    -10^4 <= nums[i] <= 10^4

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

'''


class Solution:

    def maxSubArray(self, nums: list) -> int:
        current, result = nums[0], nums[0]
        for i in range(1, len(nums)):
            current = max(current + nums[i], nums[i])
            result = max(current, result)
        return result

        # list_of_sums = []
        # sum_all = sum(nums)
        # list_of_sums.append(sum_all)
        # sum_j = sum_all
        # for j in range(len(nums) - 1, -1, -1):
        #     list_of_sums.append(sum_j)
        #     sum_j -= nums[j]
        # for i in range(len(nums)):
        #     sum_all -= nums[i]
        #     sum_i = sum_all
        #     for j in range(len(nums) - 1, i, -1):
        #         list_of_sums.append(sum_i)
        #         sum_i -= nums[j]
        # return max(list_of_sums)