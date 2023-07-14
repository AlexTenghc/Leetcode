"""Given an integer array arr and an integer difference, return the length of the longest subsequence in arr which is an arithmetic sequence such that the difference between adjacent elements in the subsequence equals difference.

A subsequence is a sequence that can be derived from arr by deleting some or no elements without changing the order of the remaining elements."""
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:

        dp = {}

        for num in arr:
            if num - difference in dp:
                dp[num] = dp[num-difference] + 1

            else:
                dp[num] = 1

        print(dp.values())
        return max(dp.values())
