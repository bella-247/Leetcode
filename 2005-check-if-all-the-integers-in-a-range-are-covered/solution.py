class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        return all(any(start <= i <= end for start, end in ranges) for i in range(left, right+1))
