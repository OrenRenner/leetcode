'''
Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

 

Example 1:

Input: words = ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: words = ["cool","lock","cook"]
Output: ["c","o"]
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of lowercase English letters.
'''
from typing import List
from collections import Counter


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = Counter(words[0])
        for i in words:
            res &= Counter(i)
            print(res)
        print(list(res.elements()))
        return list(res.elements())


a = Solution()
a.commonChars(["bella","label","roller"])