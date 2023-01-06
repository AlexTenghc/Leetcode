#You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

#Find two lines that together with the x-axis form a container, such that the container contains the most water.

#Return the maximum amount of water a container can store.

#Notice that you may not slant the container.

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        output = 0

        while l < r:
            area = min(height[l], height[r]) * (r - l)
            output = max(output, area)
            
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1

        return output
