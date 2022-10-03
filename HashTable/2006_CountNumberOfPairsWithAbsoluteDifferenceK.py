"""

Given an integer array nums and an integer k, return the number of pairs (i, j) where i < j such that |nums[i] - nums[j]| == k.

The value of |x| is defined as:

x if x >= 0.
-x if x < 0.


Example 1:

Input: nums = [1,2,2,1], k = 1
Output: 4
Explanation: The pairs with an absolute difference of 1 are:
- [1,2,2,1]
- [1,2,2,1]
- [1,2,2,1]
- [1,2,2,1]
Example 2:

Input: nums = [1,3], k = 3
Output: 0
Explanation: There are no pairs with an absolute difference of 3.
Example 3:

Input: nums = [3,2,1,5,4], k = 2
Output: 3
Explanation: The pairs with an absolute difference of 2 are:
- [3,2,1,5,4]
- [3,2,1,5,4]
- [3,2,1,5,4]


Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 100
1 <= k <= 99

"""


class Solution:
    def countKDifference(self, nums: list, k: int) -> int:
        arr = [0] * 201
        count = 0

        # Put the count of each number in the array above
        for num in nums: arr[num] += 1

        # Now for each number, just check how many times (num + k) appears in the array and
        # increment the counter variable with that value
        # Because for each number, if we have number + k in array, it means that pair has an absolute difference of k
        for num in nums: count += arr[num + k]

        return count


a = Solution()
print(a.countKDifference(nums = [1,2,2,1], k = 1))