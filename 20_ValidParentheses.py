'''

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.



Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false



Constraints:

    1 <= s.length <= 104
    s consists of parentheses only '()[]{}'.

'''


class Solution:
    def isValid(self, s: str) -> bool:
        type1 = 0
        type2 = 0
        type3 = 0

        for i in s:
            if i == '(':
                type1 += 1
            elif i == ')':
                type1 -= 1
            elif i == '{':
                type2 += 1
            elif i == '}':
                type2 -= 1
            elif i == '[':
                type3 += 1
            elif i == ']':
                type3 -= 1

        if type1 == 0 and type2 == 0 and type3 == 0:
            tmp_s = s
            for i in range(len(tmp_s) // 2):
                tmp_s = tmp_s.replace("()", "")
                tmp_s = tmp_s.replace("[]", "")
                tmp_s = tmp_s.replace("{}", "")

            if len(tmp_s) == 0:
                return True
            else:
                return False
        else:
            return False


a = Solution()
print(a.isValid(s = "()[]{}"))