class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for word in strs:
            counts = [0] * 26
            for char in word:
                counts[ord(char) - ord('a')] += 1 

            #group words
            if hashmap.get(tuple(counts), None) is not None:
                hashmap[tuple(counts)].append(word)
            else:
                hashmap[tuple(counts)] = [word]
            
        return list(hashmap.values())