#Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

#You must write an algorithm that runs in O(n) time.

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0

        for n in nums:
            if (n - 1) not in nums:
                output = 1
                while (n + output) in nums:
                    output += 1
                longest = max(output, longest)

        return longest
