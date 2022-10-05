"""

Given a string s, return true if s is a good string, or false otherwise.

A string s is good if all the characters that appear in s have the same number of occurrences (i.e., the same frequency).



Example 1:

Input: s = "abacbc"
Output: true
Explanation: The characters that appear in s are 'a', 'b', and 'c'. All characters occur 2 times in s.
Example 2:

Input: s = "aaabb"
Output: false
Explanation: The characters that appear in s are 'a' and 'b'.
'a' occurs 3 times while 'b' occurs 2 times, which is not the same number of times.

"""


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        occurrences_count_dict = dict()
        for char in s:
            if char in occurrences_count_dict:
                occurrences_count_dict[char] += 1
            else:
                occurrences_count_dict[char] = 1

        char = s[0]
        for key in occurrences_count_dict:
            if not occurrences_count_dict[key] == occurrences_count_dict[char]:
                return False

        return True