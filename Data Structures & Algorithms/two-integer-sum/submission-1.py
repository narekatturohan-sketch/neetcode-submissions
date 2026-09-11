class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen: dict = {}

        for idx, num in enumerate(nums):
            complement: int = target - num

            if complement in seen:
                return [seen[complement], idx]
            
            seen[num] = idx