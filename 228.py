"""You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b"""
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        if len(nums) == 0:
            return []

        left, cur = nums[0], nums[0]
        output = []
        for i in range(1, len(nums)):
            

            if nums[i] - 1 == cur:
                cur = nums[i]
            else:
                if left == cur:
                    output.append(str(cur))
                else:
                    output.append(str(left)+"->"+str(cur))

                left = nums[i]
                cur = nums[i]
        if left == cur:
                    output.append(str(cur))
        else:
            output.append(str(left)+"->"+str(cur))

        print(output)
        return output
