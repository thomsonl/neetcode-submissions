class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        arr = [0] * 100001
        for n in nums:
            arr[n+50000] += 1
        ans = []
        for i in range(len(arr)):
            for j in range(arr[i]):
                ans.append(i - 50000)
        return ans