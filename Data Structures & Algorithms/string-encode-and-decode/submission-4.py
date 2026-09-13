class Solution:

    def encode(self, strs: List[str]) -> str:
        result: str = ""

        for word in strs:
            result += word + '~'

        print(result)
        return result

    def decode(self, s: str) -> List[str]:
        result: list = []
        word: str = ""
        i: int = 0

        for char in s:
            if char != '~':
                word += char
            else:
                result.append(word)
                word = ""

        return result