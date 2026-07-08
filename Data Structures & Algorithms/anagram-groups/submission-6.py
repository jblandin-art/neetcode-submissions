class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for word in strs:
            #group words
            sortedWord = str(sorted(word))
            if hashmap.get(sortedWord, None) is not None:
                hashmap[sortedWord].append(word)
            else:
                hashmap[sortedWord] = [word]
            
        return list(hashmap.values())