class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for ix, numX in enumerate(nums):
            for iy,numY in enumerate(nums):
                if ix != iy and numX + numY == target:
                    return [min(ix, iy), max(ix, iy)]
        return [0]