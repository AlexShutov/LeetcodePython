class Solution:

    def __init__(self):
        self.vovels = ['a', 'e', 'i', 'o', 'u']

    def reverseVowels(self, s: str) -> str:
        left, right = 0, len(s) - 1
        result = [ch for ch in s]
        while left < right:
            if not self.isVovel(s[left]):
                left += 1
                continue
            if not self.isVovel(s[right]):
                right -= 1
                continue
            result[left] = s[right]
            result[right] = s[left]
            left += 1
            right -= 1
        return ''.join(result)

    def isVovel(self, char: str) -> bool:
        return char.lower() in self.vovels


def getTestData():
    return [
        "hello",
        "leetcode"
    ]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution()
    for string in getTestData():
        reversedVovelsString = solution.reverseVowels(string)
        print("String: " + string + " With reversed vovels is " + reversedVovelsString)
