class Solution:
    def validPalindrome(self, s: str, chances = 1, first = 0, last = 0) -> bool:
        if last == 0:
            last = len(s) - 1

        while first < last:
            if s[first] != s[last]:
                if chances > 0:
                    chances -= 1
                    return self.validPalindrome(s, chances, first + 1, last) or self.validPalindrome(s, chances, first, last - 1)
                else:
                    return False
            first += 1
            last -= 1
        return True