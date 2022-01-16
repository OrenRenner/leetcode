'''

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4



Constraints:

    1 <= nums.length <= 10^4
    -10^4 <= nums[i] <= 10^4
    nums contains distinct values sorted in ascending order.
    -104 <= target <= 104

'''


class Solution:

    def searchInsert(self, nums: list, target: int) -> int:
        N = len(nums)
        index = 0

        if N == 1:
            if nums[0] >= target:
                return 0
            if nums[0] < target:
                return 1

        middle = N // 2

        if target >= nums[middle]:
            index += (middle + self.searchInsert(nums[middle:], target))
        if target < nums[middle]:
            index += self.searchInsert(nums[:middle], target)

        return index