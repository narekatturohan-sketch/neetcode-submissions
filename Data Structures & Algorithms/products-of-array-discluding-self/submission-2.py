import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n: int = len(nums)
        output: List = [1] * n

        prefix: int = 1
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]

        suffix: int = 1
        for i in range(n - 1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]

        return output