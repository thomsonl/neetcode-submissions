class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}
        f = [[] for n in range(len(nums)+1)] 
        for n in nums:
            m[n] = m.get(n, 0) + 1
        for i, j in m.items():
            f[j] += [i]
        ans = []
        while len(ans) < k:
            x = f.pop()
            if x != []:
                for a in x:
                    ans.append(a)
        return ans