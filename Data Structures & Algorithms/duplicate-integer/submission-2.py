class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

         #for loop to go through the array
        seen = []
        for num in nums:
            if num in seen:
                return True
            else:
                seen.append(num)
        return False
        
   