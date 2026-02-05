class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = min(strs, key=len)
        min_leng = len(prefix)

        for s in strs:
            for i in range(min_leng):
                if s[i] != prefix[i]:
                    min_leng = i
                    break
                    
        return prefix[:min_leng]
