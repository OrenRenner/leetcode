'''
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

 

Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Example 2:

Input: s = "Mr Ding"
Output: "rM gniD"
 

Constraints:

1 <= s.length <= 5 * 104
s contains printable ASCII characters.
s does not contain any leading or trailing spaces.
There is at least one word in s.
All the words in s are separated by a single space.
'''

class Solution:
    def reverseWords(self, s: str) -> str:
        tmp_word = ""
        begin_word_idx = 0
        for idx, char in enumerate(s):
            if char != " ":
                tmp_word = char + tmp_word
            else:
                s = s[:begin_word_idx] + tmp_word + s[idx:]
                tmp_word = ""
                begin_word_idx = idx + 1
        else:
            s = s[:begin_word_idx] + tmp_word
            tmp_word = ""
            begin_word_idx = idx + 1
            
        return s


a = Solution()
print(a.reverseWords("Let's take LeetCode contest"))