"""

Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.



Example 1:

Input: s = "Hello"
Output: "hello"
Example 2:

Input: s = "here"
Output: "here"
Example 3:

Input: s = "LOVELY"
Output: "lovely"


Constraints:

1 <= s.length <= 100
s consists of printable ASCII characters.

"""


class Solution:
    def toLowerCase(self, s: str) -> str:
        result_str = ""
        for char in s:
            if 65 <= ord(char) <= 90:
                result_str += chr(ord(char) + 32)
            else:
                result_str += char

        return result_str
