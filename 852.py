"""An array arr a mountain if the following properties hold:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given a mountain array arr, return the index i such that arr[0] < arr[1] < ... < arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

You must solve it in O(log(arr.length)) time complexity."""
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 0, len(arr)

        while l < r:
            mid = (l + r) // 2

            if arr[mid] < arr[mid+1]:
                l += 1
            else:
                r = mid

        return l


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 0, len(arr)

        while l < r:
            mid = (l + r) // 2

            if arr[mid] > arr[mid+1] and arr[mid] > arr[mid-1]:
                return mid

            elif arr[mid+1] > arr[mid]:
                l = mid + 1

            else:
                r = mid

        

