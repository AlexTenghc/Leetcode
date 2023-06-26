"""Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order."""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums[:]]

        output = []

        for i in range(len(nums)):
            num = nums.pop(0)
            perms = self.permute(nums)

            for perm in perms:
                perm.append(num)

            output.extend(perms)
            nums.append(num)

        return output
