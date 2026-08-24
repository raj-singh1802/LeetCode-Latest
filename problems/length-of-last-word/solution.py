class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = s.split()
        n = len(res)
        total_chars = len(res[n-1])
        return total_chars