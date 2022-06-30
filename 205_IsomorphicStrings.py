"""

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.



Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true


Constraints:

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.

Please, read this article for understanding problem - https://ru.wikipedia.org/wiki/%D0%98%D0%B7%D0%BE%D0%BC%D0%BE%D1%80%D1%84%D0%B8%D0%B7%D0%BC

"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dict_key = dict()

        for index, item in enumerate(s):
            if not item in dict_key:
                dict_key[item] = t[index]
            else:
                if dict_key[item] != t[index]:
                    return False

        if len(set(dict_key.values())) == len(set(dict_key.keys())):
            return True
        else:
            return False


a = Solution()
print(a.isIsomorphic("badc", "baba"))