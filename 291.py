"""Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s"""
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dic = {}
        s = s.split()

        if len(pattern) != len(s):
            return False

        for i in range(len(s)):
            if pattern[i] in dic.keys() and dic[pattern[i]] != s[i]:
                return False
            else:
                dic[pattern[i]] = s[i]

        if len(set(dic.keys())) != len(set(dic.values())):
            return False
        return True
            
