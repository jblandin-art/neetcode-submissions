class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        # for ix, numX in enumerate(nums):
        #     for iy,numY in enumerate(nums):
        #         if ix != iy and numX + numY == target:
        #             return [min(ix, iy), max(ix, iy)]
        for i, num in enumerate(nums):
            print("started")
            soulmate = target - num
            sIx = seen.get(soulmate, None)
            if sIx is not None:
                print(soulmate, seen)
                return [min(i, seen[soulmate]), max(i, seen[soulmate])]

            # save nums as keys and index as values
            seen[num] = i