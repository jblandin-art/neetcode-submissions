class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
         # save elements in a hash with number of occurences
         hashmap = defaultdict(int)
         for num in nums:
            hashmap[num] += 1
         # sort values before...
         sortedHash = sorted(hashmap.items(), key = lambda x: x[1], reverse=True)
         print(sortedHash)
         # return a list of the keys for the top k values
         return [sortedHash[i][0] for i in range(k)]

