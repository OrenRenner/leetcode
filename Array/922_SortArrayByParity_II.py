"""

Given an array of integers nums, half of the integers in nums are odd, and the other half are even.

Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.

Return any answer array that satisfies this condition.

 

Example 1:

Input: nums = [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
Example 2:

Input: nums = [2,3]
Output: [2,3]
 

Constraints:

2 <= nums.length <= 2 * 10^4
nums.length is even.
Half of the integers in nums are even.
0 <= nums[i] <= 1000

"""
from typing import List


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        answer=[]

        # We split nums into even entries and odd entries
        even = [n for n in nums if n%2 == 0]
        odd =  [n for n in nums if n%2 == 1]

        # We fill answer with even and odd entries 
        for a, b in zip(even, odd):
            answer.append(a)
            answer.append(b)
        
        return answer