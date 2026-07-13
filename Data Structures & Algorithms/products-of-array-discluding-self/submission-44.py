class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []
        product = 1
        for i, num in enumerate(nums):
            if i == 0:
                prefix.append(1)
                continue
            product *= nums[i-1]
            prefix.append(product)
        #print("prefixes", prefix)
        product = 1
        #print("reversed list", list(reversed(nums)))
        for i, num in enumerate(reversed(nums)):
            if i == 0:
                suffix.append(1)
                continue
            product *= nums[len(nums) - i]
            suffix.append(product)
        suffix.reverse()
        #print("suffixes", suffix)
        products = []
        for i, num in enumerate(nums):
            products.append(suffix[i] * prefix[i])
        return products