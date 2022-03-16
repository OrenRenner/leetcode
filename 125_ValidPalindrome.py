'''

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.



Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.


Constraints:

1 <= s.length <= 2 * 10^5
s consists only of printable ASCII characters.

'''


class Solution:
    def isPalindrome(self, s: str) -> bool:
        left_index = 0
        right_index = len(s) - 1
        isPalindrome = True
        while left_index < len(s) and right_index > 0:
            if not s[left_index].isalpha() and not s[left_index].isdigit():
                left_index += 1
                continue

            if not s[right_index].isalpha() and not s[right_index].isdigit():
                right_index -= 1
                continue

            if s[left_index].lower() == s[right_index].lower():
                isPalindrome = True
                left_index += 1
                right_index -= 1
            else:
                isPalindrome = False
                break

        return isPalindrome


a = Solution()
print(a.isPalindrome("0P"))