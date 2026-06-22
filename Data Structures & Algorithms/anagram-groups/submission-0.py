class Solution:
    def isAnagram(self, mp: dict, word: str) -> bool:
        temp = mp.copy()
        for char in word:
            if temp.get(char) is not None:
                temp[char] -= 1
            else:
                return False
        for num in temp.values():
            if num != 0:
                return False
        return True

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicts = []
        ans = []
        for word in strs:
            counter = 0
            for mp in dicts:
                if self.isAnagram(mp, word):
                    ans[counter].append(word)
                    break
                counter += 1
            if counter == len(dicts):
                ans.append([word])
                e_dict = {}
                for char in word:
                    e_dict[char] = e_dict.get(char, 0) + 1
                dicts.append(e_dict)
        return ans
