class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        stack = [intervals[0]]
        leng = len(intervals)

        for i in range(1, leng):
            if intervals[i][0] <= stack[-1][1]:
                end = max(intervals[i][1], stack[-1][1])
                stack[-1][1] = end

            else:
                stack.append(intervals[i])

        return stack