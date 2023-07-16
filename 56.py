"""Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input."""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key = lambda x: x[0])

        output = []
        for interval in intervals:
            if not output or output[-1][1] < interval[0]:
                output.append(interval)

            else:
                output[-1][1] = max(output[-1][1], interval[1])
        return output
