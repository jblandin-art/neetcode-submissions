class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        chars = {}
        for char in s:
            chars[char] = [chars.get(char, [0])[0] + 1, 0]
        for char in t:
            if char not in chars:
                return False
            chars[char][1] += 1
        for pair in chars.values():
            if pair[0] != pair[1]:
                return False
        return True