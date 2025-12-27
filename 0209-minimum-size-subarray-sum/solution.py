class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums) 
        min_len = float("inf")
        curr_sum = 0
        
        l = 0
        for r in range(n):
            curr_sum += nums[r]

            while curr_sum >= target:
                min_len = min(r - l + 1, min_len)
                curr_sum -= nums[l]
                l += 1

        return 0 if min_len == float("inf") else min_len