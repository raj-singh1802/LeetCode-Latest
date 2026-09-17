class Solution:
    def minWindow(self, s: str, t: str) -> str:
        required = Counter(t)
        window = {}

        left = 0
        have = 0
        need = len(required)

        min_len = float("inf")
        start = 0

        for right in range(len(s)):
            ch = s[right]
            window[ch] = window.get(ch, 0) + 1
            if ch in required and window[ch] == required[ch]:
                have += 1
            
            while have == need:
                curr_len = right - left + 1
                if curr_len < min_len:
                    min_len = curr_len
                    start = left
                
                left_char = s[left]
                if left_char in window:
                    window[left_char] -= 1

                if left_char in required and window[left_char] < required[left_char]:
                    have -= 1
                
                left += 1
        
        if min_len == float("inf"):
            return ""

        return s[start: start + min_len]