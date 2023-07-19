"""Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping."""
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x : x[1])
        print(intervals)
        print()
        prev = 0
        count = 0
        for i in range(1, len(intervals)):
            print(intervals[prev])
            print(intervals[i])
            print()

            if intervals[i][0] < intervals[prev][1]:
                count += 1
                continue
            else:
                prev = i

        return count
