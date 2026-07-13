class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = []
        for ix, numX in enumerate(nums):
            product = 1
            for iy, numY in enumerate(nums):
                if ix == iy:
                    continue
                product *= numY
            products.append(product)
        
        return products