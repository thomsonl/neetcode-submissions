class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = {}
        for n in range(len(nums)):
            if a.get(target - nums[n]) is not None:
                return [a.get(target - nums[n]), n]
            a[nums[n]] = n
        
        return False