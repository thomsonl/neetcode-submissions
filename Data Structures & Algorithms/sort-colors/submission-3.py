class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        first = 0
        mid = 0
        last = len(nums) - 1
        while mid <= last:
            if nums[mid] == 1:
                mid += 1
            elif nums[last] == 2:
                last -= 1
            elif nums[mid] > nums[last]:
                nums[mid], nums[last] = nums[last], nums[mid]
                last -= 1
            elif nums[mid] <= nums[first]:
                nums[mid], nums[first] = nums[first], nums[mid]
                first += 1
                mid += 1
            else:
                mid += 1

            print(first, mid, last)
            