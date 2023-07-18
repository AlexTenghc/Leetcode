"""Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray
 whose sum is greater than or equal to target. If there is no such subarray, return 0 instead."""
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        sum = 0
        minlen = float('inf')

        for r in range(len(nums)):
            sum += nums[r]
            while sum >= target:
                minlen = min(minlen, r-l+1)
                sum -= nums[l]
                l += 1
        return minlen if minlen <= len(nums) else 0
