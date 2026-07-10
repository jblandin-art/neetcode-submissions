import re

class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        seperator = '1'
        for s in strs:
            # build string
            string += s
        # create a unique seperator
        seperator = '2' + string
        # we need len(seperator) to be represented in 5 digits
        finalString = f"{len(seperator):06}" + seperator
        # append seperator at the beginning with it's length at the 
        # beginning aswell, for example: 10|Seperator
        for s in strs:
            finalString += s
            finalString += seperator
        #print('|' + str(finalString) + '|')
        return str(finalString)
    def decode(self, s: str) -> List[str]:
        #get the length of the seperator
        trueS = s[6:]
        seperatorLen = int(s[:6])
        seperator = s[6:6+seperatorLen]
        safeSeperator = re.escape(seperator)

        #print(re.findall(f"{safeSeperator}(.*?)(?={safeSeperator})", trueS))
        return re.findall(f"{safeSeperator}(.*?)(?={safeSeperator})", trueS)
