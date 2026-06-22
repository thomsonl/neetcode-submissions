class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        a = {}
        b = {}
        for n in range(len(s)):
            a[s[n]] = a.get(s[n], 0) + 1
            b[t[n]] = b.get(t[n], 0) + 1
        print(a)
        print(b)
        return a == b
