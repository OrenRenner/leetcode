"""

Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

 

Example 1:

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.
Example 2:

Input: grid = [[3,2],[1,0]]
Output: 0
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 100
-100 <= grid[i][j] <= 100
 

Follow up: Could you find an O(n + m) solution?

"""
from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        negatives = 0
        col = 0
        for row in range(ROWS - 1, -1, -1):
            while col < COLS and grid[row][col] >= 0:
                col += 1
            negatives += COLS - col
        return negatives
