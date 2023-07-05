"""Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

 """

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = 0
        zero = 0
        output = 0

        if 0 not in nums:
            return (len(nums) - 1)

        for r in range(len(nums)):
            if nums[r] == 0:
                zero += 1

            while zero > 1:
                if nums[l] == 0:
                    zero -= 1
                l += 1

            output = max(output, r-l+1-zero)
            print(output)

        return output
            
                    

        
