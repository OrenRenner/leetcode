"""

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
 

Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?

"""
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []  # to store the result
        left, right = 0, len(nums)-1  # initialize left and right pointers to the two ends of the array
        
        # loop until left pointer is less than or equal to right pointer
        while left <= right:
            if nums[left] < 0:  
                # if the element pointed by left pointer is negative
                # compare absolute value of left element with the right element
                if abs(nums[left]) >= nums[right]:
                    res.append(nums[left]**2)  
                    # if absolute value of left element is greater than or equal
                    # to right element, add square of left element to the result array
                    left += 1  # move left pointer one position to the right
                else:
                    res.append(nums[right]**2)  
                    # if absolute value of left element is less than right element, add square of right
                    # element to the result array
                    right -= 1  # move right pointer one position to the left
            else:  
                # if the element pointed by left pointer is non-negative, break out of the loop
                break
        
        # loop through the remaining elements from right pointer to left pointer and 
        # append their squares to the result array
        for i in range(right, left-1, -1):
            res.append(nums[i]**2)
        
        res.reverse()  # reverse the result array to get the squares in non-decreasing order
        return res
