import re

class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        lengths = []
        for s in strs:
            lengths.append(str(len(s)))
        output = ",".join(lengths) + "|"
        for s in strs:
            output += s
        return str(output)

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        # find the seperator
        sIndex = s.find("|")
        lengths = [int(L) if L != "" else 0 for L in s[0:sIndex].split(",")]

        # split the string after seperator using the lengths
        rightStr = s[sIndex + 1:]
        #print(s.find("|"), s)
        strs = []
        workingIdx = 0
        for L in lengths:
            strs.append(rightStr[workingIdx: workingIdx + L])
            #print(rightStr, workingIdx, L)
            workingIdx += L
        #print(strs)
        return strs

