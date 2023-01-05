#A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

#Given a string s, return true if it is a palindrome, or false otherwise.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = "".join([c for c in s if c.isalnum()])
        l = 0
        r = len(s) - 1
        print(s)

        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
