class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            soulmate = target - num
            sIx = seen.get(soulmate, None)
            if sIx is not None:
                return [min(i, seen[soulmate]), max(i, seen[soulmate])]

            seen[num] = i