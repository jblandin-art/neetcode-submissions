class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for word in strs:
            counts = [0] * 26
            for char in word:
                counts[ord(char) - ord('a')] += 1 

            #group words
            hashmap[tuple(counts)].append(word)
            
        return list(hashmap.values())