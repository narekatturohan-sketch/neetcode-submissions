class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n: int = len(s)
        m: int = len(t)

        if n != m:
            return False
        else:
            return True if sorted(s) == sorted(t) else False