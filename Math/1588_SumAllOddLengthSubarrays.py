"""

Given an array of positive integers arr, return the sum of all possible odd-length subarrays of arr.

A subarray is a contiguous subsequence of the array.



Example 1:

Input: arr = [1,4,2,5,3]
Output: 58
Explanation: The odd-length subarrays of arr and their sums are:
[1] = 1
[4] = 4
[2] = 2
[5] = 5
[3] = 3
[1,4,2] = 7
[4,2,5] = 11
[2,5,3] = 10
[1,4,2,5,3] = 15
If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58
Example 2:

Input: arr = [1,2]
Output: 3
Explanation: There are only 2 subarrays of odd length, [1] and [2]. Their sum is 3.
Example 3:

Input: arr = [10,11,12]
Output: 66


Constraints:

1 <= arr.length <= 100
1 <= arr[i] <= 1000


Follow up:

Could you solve this problem in O(n) time complexity?

"""


class Solution:
    def sumOddLengthSubarrays(self, arr: list) -> int:
        N = len(arr)
        if N == 1 or N == 2:
            return sum(arr)

        pre1 = arr[0]
        pre2 = arr[1]
        ans = arr[0] + arr[1]
        for i in range(2, N):
            if i % 2 == 0:
                pre1 += (i // 2) * (arr[i] + arr[i - 1]) + arr[i]
                ans += pre1
            else:
                pre2 += (i // 2) * (arr[i] + arr[i - 1]) + arr[i]
                ans += pre2

        return ans