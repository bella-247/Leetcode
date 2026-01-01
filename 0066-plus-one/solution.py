class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        carry = 1
        i = n - 1
        while carry > 0:
            if i < 0:
                digits = [carry] + digits
                break

            summ = digits[i] + carry
            carry = summ // 10
            res = summ % 10

            digits[i] = res
            i -= 1

        return digits