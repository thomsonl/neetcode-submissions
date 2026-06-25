class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        m = {}
        ans = 0
        for n in nums:
            m[n] = 1
        for n in nums:
            temp = 1
            k = n - 1
            while m.get(k, 0) == 1:
                temp += 1
                k -= 1
            ans = max(ans, temp)
        return ans