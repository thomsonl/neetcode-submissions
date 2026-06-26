class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        
        while i < m+n and j < n:
            if nums1[i] > nums2[j]:
                for k in range(m + n - 1, i - 1, -1):
                    nums1[k] = nums1[k-1]
                nums1[i] = nums2[j]
                j += 1
                i -= 1
            i += 1
        
        c = -1
        while j < n:
            nums1[c] = nums2[c]
            c -= 1
            j += 1
            