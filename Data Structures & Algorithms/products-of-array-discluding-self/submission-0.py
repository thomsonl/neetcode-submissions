class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        seen = 1
        ans = [1] * len(nums)
        for n in range(len(nums)):
            ans[n] *= seen
            seen *= nums[n]
        seen = 1
        for n in range(len(nums)-1, -1, -1):
            ans[n] *= seen
            seen *= nums[n]
        return ans