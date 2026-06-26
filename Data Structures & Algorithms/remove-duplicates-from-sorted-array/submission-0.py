class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = 0
        while n < len(nums) - 1:
            while nums[n] == nums[n + 1]:
                print(nums[n], nums[n+1])
                nums.pop(n + 1)
                if n + 1 == len(nums):
                    break
            n += 1
        return len(nums)