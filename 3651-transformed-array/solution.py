class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n

        for i in range(n):
            index = (i + nums[i]) % n
            result[i] = nums[index]

        return result