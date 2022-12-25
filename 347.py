#Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        frequence = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for n, c in count.items():
            frequence[c].append(n)

        output = []
        for i in range(len(frequence)-1, 0, -1):
            for n in frequence[i]:
                output.append(n)

                if len(output) == k:
                    return output
