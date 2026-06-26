class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        
        while i < m+n and j < n:
            if nums1[i] > nums2[j]:
                nums1.insert(i, nums2[j])
                nums1.pop()
                j += 1
            i += 1
        
        c = -1
        while j < n:
            nums1[c] = nums2[c]
            c -= 1
            j += 1
            