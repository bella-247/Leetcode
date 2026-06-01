class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        memo = [[None] * n for _ in range(n)]

        def dp(start, end):
            if end <= start:
                return True

            if memo[start][end] is not None:
                return memo[start][end]

            if s[start] != s[end]:
                memo[start][end] = False

            else:
                memo[start][end] = dp(start + 1, end - 1)

            return memo[start][end]

        start = 0
        length = 1

        for i in range(n):
            for j in range(n - 1, i - 1, -1):
                if s[i] == s[j] and dp(i, j):
                    if j - i + 1 > length:
                        start = i
                        length = j - i + 1
                    break

        return s[start : start + length]
