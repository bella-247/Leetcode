class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        evens_sum = sum(filter(lambda x : x % 2 == 0, nums))
        result = []

        for value, index  in queries:
            prev_value = nums[index]
            new_value = prev_value + value

            if prev_value % 2 == 0:
                evens_sum -= prev_value

            if new_value % 2 == 0:
                evens_sum += new_value

            nums[index] = new_value
            result.append(evens_sum)

        return result