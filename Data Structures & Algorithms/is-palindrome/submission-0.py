class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        s = s.lower()
        print(s)
        for i in range(len(s)//2):
            if s[i] == s[-1-i]:
                print(s[i], s[-1-i], i)
                continue
            else:
                print(s[i], s[-1-i], i)
                return False

        return True