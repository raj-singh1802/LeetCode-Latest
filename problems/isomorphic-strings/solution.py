class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map1 = {}
        map2 = {}

        for i in range(len(s)):
            if s[i] not in map1:
                map1[s[i]] = i
            if t[i] not in map2:
                map2[t[i]] = i
            if map1[s[i]] != map2[t[i]]:
                return False
        return True        