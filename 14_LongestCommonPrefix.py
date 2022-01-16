'''

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.



Constraints:

    1 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lower-case English letters.

'''


class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        min_len = len(strs[0])
        tmp_s = strs[0]
        for i in strs:
            if len(i) < min_len:
                min_len = len(i)
                tmp_s = i

        i = 0
        while i < len(strs):
            obj = strs[i]
            if obj[:len(tmp_s)] == tmp_s:
                i += 1
            else:
                tmp_s = tmp_s[:len(tmp_s) - 1]

        return tmp_s


a = Solution()
print(a.longestCommonPrefix(strs = ["flower","flow","flight"]))