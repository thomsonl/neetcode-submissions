class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        length = min(len(word1), len(word2))
        ans = ""
        for i in range(length):
            ans += word1[i]
            ans += word2[i]
        ans += word1[length:] + word2[length:]
        return ans