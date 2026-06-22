class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        counter = 0
        for i in nums:
            if mp.get(target - i) is not None:
                return [mp.get(target - i), counter]
            mp[i] = counter
            counter+= 1
        return null