"""

Reversing an integer means to reverse all its digits.

For example, reversing 2021 gives 1202. Reversing 12300 gives 321 as the leading zeros are not retained.
Given an integer num, reverse num to get reversed1, then reverse reversed1 to get reversed2. Return true if reversed2 equals num. Otherwise return false.

 

Example 1:

Input: num = 526
Output: true
Explanation: Reverse num to get 625, then reverse 625 to get 526, which equals num.
Example 2:

Input: num = 1800
Output: false
Explanation: Reverse num to get 81, then reverse 81 to get 18, which does not equal num.
Example 3:

Input: num = 0
Output: true
Explanation: Reverse num to get 0, then reverse 0 to get 0, which equals num.
 

Constraints:

0 <= num <= 10^6

"""


class Solution:
    @staticmethod
    def reverse_num(num: int) -> int:
        new_num: int = 0
        while num > 0:
            new_num = 10 * new_num + num % 10
            num //= 10
        return new_num

    def isSameAfterReversals(self, num: int) -> bool:
        num1 = Solution.reverse_num(num)
        num2 = Solution.reverse_num(num1)
        return num == num2


a = Solution()
print(a.isSameAfterReversals(526))