class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ans = 0
        n = 0
        while n < len(nums):
            if nums[n] == val:
                nums.pop(n)
            else:
                ans += 1
                n += 1
        return ans