class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for val in nums:
            if val not in seen:
                seen.add(val)
            else:
                return True
        
        return False