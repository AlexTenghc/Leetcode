"""A binary string is monotone increasing if it consists of some number of 0's (possibly none), followed by some number of 1's (also possibly none).

You are given a binary string s. You can flip s[i] changing it from 0 to 1 or from 1 to 0.

Return the minimum number of flips to make s monotone increasing."""
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        m = 0

        for c in s:
            if c == "0":
                m += 1

        output = m

        for c in s:
            if c == "0":
                m -= 1
            elif c == "1":
                m += 1
            output = min(output, m)
        return output
