'''
Given a 2D integer array nums where nums[i] is a non-empty array of distinct positive integers, return the list of integers that are present in each array of nums sorted in ascending order.
 

Example 1:

Input: nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
Output: [3,4]
Explanation: 
The only integers present in each of nums[0] = [3,1,2,4,5], nums[1] = [1,2,3,4], and nums[2] = [3,4,5,6] are 3 and 4, so we return [3,4].
Example 2:

Input: nums = [[1,2,3],[4,5,6]]
Output: []
Explanation: 
There does not exist any integer present both in nums[0] and nums[1], so we return an empty list [].
 

Constraints:

1 <= nums.length <= 1000
1 <= sum(nums[i].length) <= 1000
1 <= nums[i][j] <= 1000
All the values of nums[i] are unique.
'''
from typing import List


class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        d = {}
        
        for i in range(len(nums)):
            for j in nums[i]:
                if j not in d:
                    d[j] = 1
                else:
                    d[j]+=1
        print(d)
        res = []
        for k,v in d.items():
            if v == len(nums):
                res.append(k)
                
        return sorted(res)


a = Solution()
print(a.intersection([[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]))