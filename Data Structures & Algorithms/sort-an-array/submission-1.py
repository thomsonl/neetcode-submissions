import random

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.rand_sort(nums)
    
    def rand_sort(self, nums):
        if not nums or len(nums) == 1:
            return nums
        
        pivot = nums[random.randint(0, len(nums) - 1)]
        less = [num for num in nums if num < pivot]
        equal = [num for num in nums if num == pivot]
        greater = [num for num in nums if num > pivot]
        return self.rand_sort(less) + equal + self.rand_sort(greater)


