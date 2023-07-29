"""Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 """
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}

        for key, val in enumerate(nums):
            if val not in dic:
                dic[val] = key

            else:
                if abs(dic.get(val) - key) <= k:
                    return True

                else:
                    dic[val] = key
        return False
