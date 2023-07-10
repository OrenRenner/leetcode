"""

You are given an n x n grid where we place some 1 x 1 x 1 cubes that are axis-aligned with the x, y, and z axes.

Each value v = grid[i][j] represents a tower of v cubes placed on top of the cell (i, j).

We view the projection of these cubes onto the xy, yz, and zx planes.

A projection is like a shadow, that maps our 3-dimensional figure to a 2-dimensional plane. We are viewing the "shadow" when looking at the cubes from the top, the front, and the side.

Return the total area of all three projections.

 

Example 1:


Input: grid = [[1,2],[3,4]]
Output: 17
Explanation: Here are the three projections ("shadows") of the shape made with each axis-aligned plane.
Example 2:

Input: grid = [[2]]
Output: 5
Example 3:

Input: grid = [[1,0],[0,2]]
Output: 8
 

Constraints:

n == grid.length == grid[i].length
1 <= n <= 50
0 <= grid[i][j] <= 50

"""
from typing import List


class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        xy = 0
        yz = 0
        xz = 0

        for i in range(len(grid)):
            max_yz = 0
            max_xz = 0
            for j in range(len(grid[i])):
                if grid[i][j] > 0:
                    xy += 1
                if grid[i][j] > max_yz:
                    max_yz = grid[i][j]
                if grid[j][i] > max_xz:
                    max_xz = grid[j][i]
            yz += max_yz
            xz += max_xz

        return xy + yz + xz
