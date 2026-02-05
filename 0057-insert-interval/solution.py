class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newStart, newEnd = newInterval

        # check if the interval can be added at the end 
        if not intervals or newEnd < intervals[0][0]:
            return [newInterval] + intervals

        if newStart > intervals[-1][1]:
            return intervals + [newInterval]

        result = []
        inserted = False

        i = 0
        while not inserted and i < len(intervals):
            start, end = intervals[i]

            if (
                (start <= newStart <= end) or
                (start <= newEnd <= end) or
                (newStart <= start and end <= newEnd)
            ):
                inserted = True
                start = min(start, newStart)
                end = max(end, newEnd)

                while i < len(intervals) - 1 and end >= intervals[i + 1][0]:
                    end = max(end, intervals[i + 1][1])
                    i += 1

            result.append([start, end])

            if (not inserted
                and i < len(intervals) - 1 
                and newEnd < intervals[i+1][0]
            ):
                inserted = True
                result.append([newStart, newEnd])

            i += 1


        return result + intervals[i:]
