class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = strs[0]
        for s in strs[1:]:
            if s == "":
                return ""
            for l in range(min(len(ans), len(s))):
                ans = ans[0:min(len(ans), len(s))]
                if s[l] != ans[l]:
                    ans = ans[0:l]
                    break
        return ans