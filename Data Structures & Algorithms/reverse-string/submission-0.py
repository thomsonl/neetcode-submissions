class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for n in range(len(s)//2):
            s[n], s[-1 * n - 1] = s[-1 * n - 1], s[n]