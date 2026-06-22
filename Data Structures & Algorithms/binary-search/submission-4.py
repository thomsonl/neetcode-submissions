class Solution:
    def search(self, nums: List[int], target: int) -> int:
        count = 0
        if nums[0] == target:
                return 0

        while nums:
            loc = len(nums)//2
            if nums[loc] == target:
                return count + loc
            if nums[loc] < target:
                nums = nums[loc + 1:]
                count+= loc + 1
            else:
                nums = nums[:loc]
        return -1
            