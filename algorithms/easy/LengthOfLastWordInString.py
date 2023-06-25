class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = len(s)
        if length == 0:
            return 0
        right = length - 1
        while right >= 0 and s[right] == ' ':
            right -= 1
        if right == 0:
            return 1
        left = right
        while left >= 0 and s[left] != ' ':
            left -= 1

        return right - left


def getTestData():
    return [
        "a",
        "Hello World",
        "   fly me   to   the moon  ",
        "luffy is still joyboy"
    ]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution()
    for string in getTestData():
        lastWordLength = solution.lengthOfLastWord(string)
        print("For string " + string + " last word length is: " + str(lastWordLength))
