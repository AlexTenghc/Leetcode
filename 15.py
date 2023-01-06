#Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

#Notice that the solution set must not contain duplicate triplets.



class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        
        for i, a in enumerate(nums):
            if i > 0 and nums[i - 1] == a:
                continue
                
            l = i + 1
            r = len(nums) - 1
            
            while l < r:
                threeSum = nums[i] + nums[l] + nums[r]
                
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                    
        return res
