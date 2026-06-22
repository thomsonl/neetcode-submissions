class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        size = len(s)
        if size != len(t):
            return False
        mp = {}
        for i in range(size):
            mp[s[i]] = mp.get(s[i], 0) + 1
            mp[t[i]] = mp.get(t[i], 0) - 1
        for value in mp.values():
            if value != 0:
                return False
        return True
        
        