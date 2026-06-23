class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        l = 0
        while l < len(strs):
            sub = [strs[l]]
            r = l + 1
            while r < len(strs):
                if self.isAnagrams(strs[l],strs[r]):
                    sub.append(strs.pop(r))
                else:
                    r += 1
            ans.append(sub)
            l += 1
        return ans
            


    def isAnagrams(self, n: str, m: str) -> bool:
        if len(n) != len(m): return False 
        n2 = []
        m2 = []
        for l in range(len(n)):
            n2.append(ord(n[l]))
            m2.append(ord(m[l]))
        n2.sort()
        m2.sort()
        return n2 == m2