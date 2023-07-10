"""Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array."""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums = sorted(nums)
        print(nums)

        output = nums[0]
        counter = 0

        if len(nums) <= 2:
            return nums[0]

        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                counter += 1
            else:
                counter = 1
            if counter > floor(len(nums)/2):
                output = nums[i]

        return output
