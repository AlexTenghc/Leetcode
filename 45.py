"""You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:"""
class Solution:
    def jump(self, nums: List[int]) -> int:
        answer, n = 0, len(nums)
        end, far = 0, 0

        for i in range(n-1):
            far = max(far, i+nums[i])

            if i == end:
                answer += 1
                end = far

        return answer
