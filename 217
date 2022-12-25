#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicate = set()
        for i in nums:
            if i in duplicate:
                return True
            duplicate.add(i)
        return False
