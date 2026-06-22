class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        mid = len(nums)//2

        if nums[left] < nums[right]:
            return nums[left]
        
        if not nums:
            return None
        
        if left == right:
            return nums[0]

        while not (left == mid - 1 and nums[left] > nums[mid]):
            if left == right - 1:
                return nums[right]
        
            if nums[left] > nums[mid]:
                right = mid
                mid = (left + right) // 2
            elif nums[right] < nums[mid]:
                left = mid
                mid = (left + right) // 2
            
        return nums[mid]
                  