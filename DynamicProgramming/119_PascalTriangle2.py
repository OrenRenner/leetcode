'''

Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:




Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]


Constraints:

0 <= rowIndex <= 33

'''


class Solution:
    def getRow(self, rowIndex: int):# -> List[int]:
        rowIndex += 1
        if rowIndex == 1:
            return [1]
        elif rowIndex == 2:
            return [1, 1]
        elif rowIndex == 3:
            return [1, 2, 1]
        else:
            last = [1, 2, 1]
            for index in range(4, rowIndex + 1):
                temp = [1 for i in range(index)]
                for i in range(1, index - 1):
                    temp[i] = last[i - 1] + last[i]
                last = temp
            return last


a = Solution()
print(a.getRow(4))