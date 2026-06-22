class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        freq = [[] for i in range(len(nums) + 1)] 
        for i in nums:
            mp[i] = mp.get(i,0) + 1
        for key,v in mp.items():
            freq[v].append(key)

        ans = []
        for i in range(len(freq) - 1,0,-1):
            for n in freq[i]:
                ans.append(n)
                if len(ans) == k:
                    return ans
        