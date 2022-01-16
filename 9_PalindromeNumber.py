'''

Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

    For example, 121 is a palindrome while 123 is not.



Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.



Constraints:

    -231 <= x <= 231 - 1


Follow up: Could you solve it without converting the integer to a string?

'''


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            tmp = x
            count = 0
            while tmp > 0:
                count += 1
                tmp //= 10

            left_tens = 10 ** (count - 1)
            right_tens = 10
            flag = True

            for i in range(count // 2):
                left_part = x // left_tens
                right_part = x % right_tens
                if left_part == right_part:
                    x %= left_tens
                    left_tens //= 100
                    x //= 10
                    flag = True
                    continue
                else:
                    flag = False
                    break
            # 12321
            if flag:
                return True
            else:
                return False


a = Solution()
print(a.isPalindrome(123621))