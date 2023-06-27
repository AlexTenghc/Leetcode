"""Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 """
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        dp = [False] * (len(s)+1)
        dp[len(s)] = True

        for i in range(len(s)-1, -1, -1):
            for w in wordDict:
                l = len(w)

                if (i+l) <= len(s) and (s[i:i+l] == w) and dp[i+l]:
                    dp[i] = True

        print(dp)
        return dp[0] 
